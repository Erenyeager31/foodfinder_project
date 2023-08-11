from django.shortcuts import render

# Create your views here.
#hi
#hey whatsup ??
#Good morning

def index(request):
    return render(request,'index.html')