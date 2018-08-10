from django.shortcuts import render

# Create your views here.
from appThree.models import User
def index(request):
    return render(request,"appThree/index.html")

def users(request):
    user_list=User.objects.order_by("first name")
    user_dict={"users":user_list}
    return render(request,"appThree/users.html",context=user_dict)
