from django.shortcuts import render

# Create your views here.
#hi
#hey whatsup ??
#Good morning

def index(request):
    return render(request,'index.html')

def create_act(request):
    return render(request,'CreateAccount.html')

def sign_in(request):
    return render(request,'login.html')

def aboutus(request):
    return render(request,'AboutUs.html')

def contactus(request):
    return render(request,'ContactUs.html')