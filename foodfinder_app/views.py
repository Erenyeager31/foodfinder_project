import json
from django.shortcuts import render,HttpResponse
from foodfinder_app.models import seller_details,user_detail
# Create your views here.
#hi
#hey whatsup ??
#Good morning
auth_customer = False
auth_seller = False
username = "null"

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
    
def login_processing(request):
    global auth_seller
    global auth_customer
    global username
    # auth_seller = False
    # auth_customer = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if(role == "Customer" or role == "Job seeker"):
            allusers = user_detail.objects.values()
            for i in allusers:
                if username == i.get("username"):
                    # print(i.get("password"))
                    if password == i.get("password"):
                        auth_customer = True
                        auth_seller = False
                        username = i.get("username")
                        data = {
                            "success":True,
                            "message":"Login Successfull",
                            }
                        return HttpResponse(json.dumps(data))
                    else:
                        data = {
                            "success":False,
                            "message":"Invalid Credentials",
                            }
                        return HttpResponse(json.dumps(data))
                else:
                    data = {
                            "success":False,
                            "message":"Invalid Credentials",
                            }
                    return HttpResponse(json.dumps(data))
        else:
            allusers = seller_details.objects.values()
            for i in allusers:
                if username == i.get("username"):
                    if password == i.get("password"):
                        auth_seller = True
                        auth_customer = False
                        data = {
                            "success":True,
                            "message":"Login Successfull",
                            }
                        return HttpResponse(json.dumps(data))
                    else:
                        data = {
                            "success":False,
                            "message":"Invalid Credentials",
                            }
                        return HttpResponse(json.dumps(data))
                else:
                    data = {
                            "success":False,
                            "message":"Invalid Credentials",
                            }
                    return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("Some error has occured ! Please try again")
    
def profile(request):
    global auth_customer
    global auth_seller
    global username

    # print(auth_seller)
    # print(auth_customer)
    # print(username)

    if(auth_seller == True):
        # print("hi")
        data = seller_details.objects.filter(username=username).values()
        return render(request,"profile_page.html",{'data':data})
    elif(auth_customer == True):
        return render(request,"AboutUs.html")
    else:
        return render(request,"Login.html")

def logout(request):
    global auth_customer
    global auth_seller
    auth_seller = False
    auth_customer = False
    return HttpResponse("You have been logged out Successfully")

def s_fill_details(request):
    global auth_seller
    if(auth_seller == True):
        data = seller_details.objects.filter(username=username).values()
        return render(request,"seller_fill_details.html",{'data':data})
    
#! handler to save the details of seller
def s_save_details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        shop_add = request.POST.get("shop_add")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        mobile_no = request.POST.get("mobile_no")
        bank_act_no = request.POST.get("bank_act_no")
        ifsc = request.POST.get("ifsc")
        branch_name = request.POST.get("branch_name")

        print(name+email+shop_add+city+state+zip+mobile_no+bank_act_no+ifsc+branch_name)
        user = seller_details.objects.get(email=email)
        # user(shop_add=shop_add,city=city,state=state,zip=zip,bank_act_no=bank_act_no,ifsc=ifsc,branch_name=branch_name)
        user.shop_add = shop_add
        user.city = city
        user.state = state
        user.zip = zip
        user.bank_act_no = bank_act_no
        user.ifsc = ifsc
        user.branch_name = branch_name
        user.save()
        return HttpResponse("Saved")
    
def uploadfood(request):
    return render(request,"upload_food.html")