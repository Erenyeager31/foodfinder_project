from django.shortcuts import render,HttpResponse
from foodfinder_app.models import seller_details,user_detail
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

def signup_processing(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("user")
        
        if(role == "Customer" or role == "Job seeker"):
        
            allusers = user_detail.objects.values()
            for i in allusers:
            # print(i.get("email"))
                if email == i.get("email"):
                    return HttpResponse("Email-ID alredy exists")

            myuser = user_detail(name=name,email=email,mobile_no=phone,username=username,password=password,role=role)
            myuser.save()
            return HttpResponse("Account created succesfully for"+" "+name+".\n"+"Please go to login page")

        else:
            allusers = seller_details.objects.values()
            for i in allusers:
                # print(i.get("email"))
                if email == i.get("email"):
                    return HttpResponse("Email-ID alredy exists")

            myuser = seller_details(name=name,email=email,mobile_no=phone,username=username,password=password,role=role)
            myuser.save()
            return HttpResponse("Account created succesfully for"+" "+name+".\n"+"Please go to login page")
    else:
        return HttpResponse("Sorry ! could not process the data")