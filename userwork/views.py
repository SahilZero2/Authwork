from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.storage import FileSystemStorage
# Create your views here.
def createaccount(request):
    if request.method == 'POST':
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
        try:
            profile_pic = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name,profile_pic)
            pro.profile_picture = filename
            pro.save()
        except Exception as e:
            print('*'*50)
            print(e)    
            print('*'*50)

    
        # return render(request,"signup.html",{
        #     'title':'Create Account',
        #     'msg' : 'Registred Successfully!'
        #     }
        #     )
        return redirect('login')


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


