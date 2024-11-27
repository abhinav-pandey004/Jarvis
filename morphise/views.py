from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ai.function import ai_model
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def blog(request):
    return render(request,'blog.html')
def services(request):
    return HttpResponse("this is services")
def about(request):
    return HttpResponse("this is about page ")
def signin(request):
    return render(request,"signin.html")
def signup(request):
    return render(request,"signup.html")
def mainpage(request):
    return render(request,"home.html")
def login_view(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        print(username,password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'signin.html')
 
def sign_up(request):
    if request.method=="POST":
        Username=request.POST.get('Username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(f"all details {Username},{email},{password}")
    else:
         messages.error(request, 'Invalid username or password')
    if User.objects.filter(username=Username).exists():
        messages.error(request, 'Username is already taken.')
    elif User.objects.filter(email=email).exists():
        messages.error(request, 'Email is already registered.')
    else:
        user = User.objects.create_user(username=Username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('mainpage')      
    return render(request,'signup.html')
def aioutput(request):
    if request.method =="POST":
        user_input=request.POST.get('user_input')
        print(user_input)
        output=ai_model(user_input)
        print(output)
        context={
            'value':output
        }
        return render(request,'home.html',context)
    return redirect('mainpage')

def test(request):
    context ={
        'value':ai_model("how to make cake")
    }
    return render(request,'test.html',context)