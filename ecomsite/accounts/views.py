from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    request.session.clear()
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentails')
            return redirect('/account/login')

    return render(request, 'accounts/login.html')
def  register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username exists')
                return redirect('/account/register')
            else:
                user=User.objects.create_user(first_name=name,username=username, email=email, password=password1)
                user.save()
                return redirect('/account/login')
        else:
            messages.info(request,'password did not match')
            return redirect('/account/register')
    return render(request, 'accounts/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    