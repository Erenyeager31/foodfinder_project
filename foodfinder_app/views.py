import json
from django.shortcuts import render,HttpResponse
from foodfinder_app.models import seller_details,user_detail,food_detail,cart,business_location,review,shop_review
# Create your views here.
#hi
#hey whatsup ??
#Good morning
auth_customer = False
auth_seller = False
username = "null"

def index(request):
    food_list = food_detail.objects.values()
    # print(food_list)
    return render(request,'index.html',{'food_list':food_list})

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
                if email == i.get("email") or username == i.get("username"):
                    return HttpResponse("Email-ID or username is already taken !")

            myuser = user_detail(name=name,email=email,mobile_no=phone,username=username,password=password,role=role)
            myuser.save()
            return HttpResponse("Account created succesfully for"+" "+name+".\n"+"Please go to login page")

        else:
            allusers = seller_details.objects.values()
            for i in allusers:
                # print(i.get("email"))
                if email == i.get("email") or username == i.get("username"):
                    return HttpResponse("Email-ID or username is already taken !")

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
            allusers = seller_details.objects.values()
            user = user_detail.objects.filter(username=username).values()
            # print(user[0].get("password"))
            if user[0].get("password") == password:
                auth_seller = False
                auth_customer = True
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
            print(request.POST)
            allusers = seller_details.objects.values()
            seller = seller_details.objects.filter(username=username).values()
            # print(seller[0].get("password"))
            if seller[0].get("password") == password:
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
        return HttpResponse("Some error has occured ! Please try again")
    
def profile(request):
    global auth_customer
    global auth_seller
    global username
    print(auth_seller)
    print(auth_customer)
    print(username)
    if(auth_seller == True):
        # print("hi")
        data = seller_details.objects.filter(username=username).values()
        print(data)
        return render(request,"profile_page.html",{'data':data})
    elif(auth_customer == True):
        data = user_detail.objects.filter(username=username).values()
        return render(request,"customer_profile.html",{'data':data})
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
        business_name = request.POST.get("business_name")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        mobile_no = request.POST.get("mobile_no")
        bank_act_no = request.POST.get("bank_act_no")
        ifsc = request.POST.get("ifsc")
        branch_name = request.POST.get("branch_name")
        location = request.POST.get("location")

        print(name+email+shop_add+business_name+city+state+zip+mobile_no+bank_act_no+ifsc+branch_name)
        user = seller_details.objects.get(email=email)
        # user(shop_add=shop_add,city=city,state=state,zip=zip,bank_act_no=bank_act_no,ifsc=ifsc,branch_name=branch_name)
        user.shop_add = shop_add
        user.city = city
        user.state = state
        user.zip = zip
        user.bank_act_no = bank_act_no
        user.ifsc = ifsc
        user.branch_name = branch_name
        user.business_name = business_name    
        user.save()
        return HttpResponse("Saved")
    
def uploadfood(request):
    return render(request,"upload_food.html")

def food_upload_form(request):
    if request.method == "POST":
        dictionary = dict(request.POST.items())
    # print(dictionary)
    food_details = food_detail.objects.filter(username=dictionary['username'],food_name=dictionary['food_name'],food_cat=dictionary['food_cat']).values()
    print(dictionary['attempt'])
    if dictionary['attempt'] == '1':
        # print("inside attempt")
        if food_details.count() == 1:
            data = {
                "success":False,
                "message":"The food is already added"
            }   
        else:
            data = {
                "success":True,
                "message":"X"
            }
        return HttpResponse(json.dumps(data))
    else:
        if dictionary['attempt'] == '2':
            new_f_details = food_detail(
                username=dictionary['username'],
                food_name=dictionary['food_name'],
                food_cat=dictionary['food_cat'],
                price=dictionary['price'],
                description=dictionary['description'],
                img_url=dictionary['img_url'],
                )
            new_f_details.save()
            data = {
                    "success":True,
                    "message":"Food Detail saved Successfully"
                }
            return HttpResponse(json.dumps(data))
    
    return HttpResponse("Testing..")

def check_orders(request):
    return render(request,'SellerCheckOrders.html')

def upload_recipe(request):
    return render(request,'');

def add_to_cart(request):
    if request.method=='GET':
        username = request.GET.get("username")
        food_id = request.GET.get("id")
    
    existing_cart = cart.objects.filter(username = username,food_id=food_id).values()
    # print(existing_cart)
    if(existing_cart.count() == 0):
        new_cart = cart(username=username,food_id=food_id)
        new_cart.save()
        return HttpResponse("Food item added to cart successfully")
    else:
        return HttpResponse("Already added to the cart")
    
def save_location(request):
    # old_location = business_location.objects.filter(username=request.GET.get("username")).values()
    if request.method == 'GET':
        try:
            old_location = business_location.objects.get(username=request.GET.get("username"))
            old_location.location = request.GET.get("location")
            old_location.save()
            data = {
                "message":"Location updated Succesfully"
            }
        except:
            username = request.GET.get("username")
            business_name = request.GET.get("business_name")
            location = request.GET.get("location")
            new_location = business_location(username=username,business_name=business_name,location=location)
            new_location.save()
            data = {
                "message":"Location saved Succesfully"
            }
        # print(shop.location)
        shop = seller_details.objects.get(username=request.GET.get("username"))
        shop.location = request.GET.get("location")
        shop.save()
    return HttpResponse(json.dumps(data))

def showmaps(request):
    data = {
        "message":"Debugging in process"
    }
    return render(request,"show_maps.html",{'data':data})

def showcart(request):
    global username
    cart_values = cart.objects.filter(username=username).values()
    # print(cart_values)
    food_id = []
    for i in cart_values:
        food_id.append(i.get("food_id"))
    food_list = food_detail.objects.filter(id__in = food_id).values()
    print(food_list)
    food_count = food_list.count()
    total_price = 0
    for i in food_list:
        total_price = total_price + i.get("price")
    
    # print(price_list)
    # total_price = sum(price_list)
    return render(request,"cartt.html",{'cart_values':{'food_list':food_list,'count':food_count,'price':total_price}})

def delete_cart(request):
    if request.method == "GET":
        id = request.GET.get("id")
    print(id)
    cart_list = cart.objects.filter(food_id=id)

    # remove the comment afterwards
    cart_list.delete()
    global username
    cart_values = cart.objects.filter(username=username).values()
    # print(cart_values)
    food_id = []
    for i in cart_values:
        food_id.append(i.get("food_id"))
    food_list = food_detail.objects.filter(id__in = food_id).values()
    # print(food_list)
    food_count = food_list.count()
    total_price = 0
    for i in food_list:
        total_price = total_price + i.get("price")
    return HttpResponse(json.dumps({
            'cart_values':{
                'food_list':list(food_list),
                'count':food_count,
                'price':total_price
                }
            ,
            "status":"Data removed Successfully"
        }
    ))

def checkout(request):
    return render(request,"checkout.html")

def fetch_location(request):
    b_location = business_location.objects.values()
    location = []
    business_name = []
    print(b_location)
    for i in b_location:
        loc = i.get("location")
        array = loc.split(',')
        #!Obtaining the string, performing split and appending into the list
        location.append({'lat':float(array[0]),'lng':float(array[1])})
        business_name.append(i.get("business_name"))
    
    # print(location)
    # json_loc = json.dumps(location)
    # json_name = json.dumps(business_name)
    response_data = {
        'locations':location,
        'name':business_name
    }
    json_resp = json.dumps(response_data)
    return HttpResponse(json_resp, content_type='application/json')

def search_filter(request):
    food_list = food_detail.objects.values()
    return render(request,'search_filter.html',{'food_list':food_list})

def listShop(request):
    sellers = seller_details.objects.values()
    # print(sellers)
    food_list = []
    seller_list = list(sellers)
    for i in seller_list:
        food = food_detail.objects.filter(username = i['username']).values()
        # print(food)
        food_list.extend(food)
    
    data = {
        "seller":seller_list,
        "foods":list(food_list)
    }
    # json_shop = json.dumps(seller_list)
    return HttpResponse(json.dumps(data),content_type='application/json')

def review_page(request):
    food_list = food_detail.objects.values()
    return render(request,'review_page.html',{'food_list':food_list})

def submit_review(request):
    # print(request.POST)
    if request.method == 'POST':
        req_data = request.POST
        print(req_data)
        try:
            existing_review = review.objects.get(food_id=req_data['food_id'],username=req_data['username'])
            existing_review.rating = req_data['rating']
            existing_review.review = req_data['review']
            existing_review.save()
            return HttpResponse("Review Updated Succesfully")
        except Exception as e:
            print(e)
            try:
                new_review = review(food_id=req_data['food_id'],rating=req_data['rating'],review=req_data['review'],username=req_data['username'])
                new_review.save()
                return HttpResponse("Review added Succesfully")
            except Exception as e:
                return HttpResponse("Some error ocurred ! Please try again later")

def shop_review(request):
    # print(request.POST)
    if request.method == 'POST':
        req_data = request.POST
        print(req_data)
        try:
            existing_review = shop_review.objects.get(business_name=req_data['business_name'],username=req_data['username'])
            existing_review.rating = req_data['rating']
            existing_review.review = req_data['review']
            existing_review.save()
            print("above")
            return HttpResponse("Review Updated Succesfully")
        except Exception as e:
            print(e)
            try:
                new_review = shop_review(business_name=req_data['business_name'],rating=req_data['rating'],review=req_data['review'],username=req_data['username'])
                new_review.save()
                return HttpResponse("Review added Succesfully")
            except Exception as e:
                print(e)
                return HttpResponse("Some error ocurred ! Please try again later")
