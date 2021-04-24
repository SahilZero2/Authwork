from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
# Create your views here.
def createaccount(request):
    if request.method == 'POST':
        try:
            obj = User(
                first_name = request.POST.get('name'),
                last_name = request.POST.get('last'),
                username = request.POST.get("username"),   
                email = request.POST.get('email'),
                )
            obj.save()
            obj.set_password(request.POST.get('Password'))
            obj.save()

            pro = Profile.objects.create(user = obj)
            #saving image
            
            profile_pic = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name,profile_pic)
            pro.profile_picture = filename
            pro.save()
            return redirect('login')
        except IntegrityError:
            return render(request,"signup.html",{'error':'This user name has already been taken , please chose another one !'})  
        
    else:
        return render(request,"signup.html",{'title':'Create Account'})



def profile(request):
    pro = Profile.objects.get(user__id = request.user.id)
    return render(
        request,
        'profile.html',
        {
         'title' : f'{request.user.first_name}',
         'msg' : 'Welcome to your Profile !',
         'pro' : pro 
         }
    )


