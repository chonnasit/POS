# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owners
from .models import Table

# Create your views here.
#Start Tong
i = 0
log= []
def Login(request):
    return render(request,'Login.html')
def Forgetpassword(request):
    return render(request,'Forgetpassword.html')
def Repassword(request):
    return render(request,'Repassword.html')
def Re(request):
    email=request.POST['email']
    password= request.POST['password']
    passwordnew = request.POST['passwordnew']
    passwordnewre = request.POST['passwordnewre']
    
    return render(request,'Login.html')
def Tableroom(request):
    i = 0
    if i == 0:
        email=request.POST['email']
        password= request.POST['password']
        if Owners.objects.filter(email=email,password=password).exists():
            i = 1
            tables = Table.objects.all()
            return render(request,'Tableroom.html',{'tables':tables})
        else:

            return render(request,'Login.html')
    else :
        return render(request,'Tableroom.html')
def Kitchen(request):
    return render(request,'Kitchen.html')
def Raw(request):
    return render(request,'Raw.html')
def Rawmaterial(request):
    return render(request,'Rawmaterial.html')
#End  Tong

#Start Top
def AddFood(request):
    return render(request,'addFood.html')
def DeleteDrink(request):
    return render(request,'deleteDrink.html')
def DeleteFood(request):
    return render(request,'deleteFood.html')
def Deleteice(request):
    return render(request,'deleteice.html')
def Drink(request):
    return render(request,'Drink.html')
def Food(request):
    return render(request,'food.html')
def Ice_Cream(request):
    return render(request,'Ice cream.html')
def SellectCategory(request):
    return render(request,'sellectCategory.html')
#End top

#Start Frong
def Cash(request):
    return render(request,'Cash.html')
def Cash_Success(request):
    return render(request,'Cash_Success.html')
def Transfer(request):
    return render(request,'Transfer.html')
def Transfer_Success(request):
    return render(request,'Transfer_Success.html')
#End Frong

#start Tomtam
def Add_Employee(request):
    return render(request,'Add_Employee.html')
def Edit_Food(request):
    return render(request,'edit_food.html')
def Edit_Employee(request):
    return render(request,'edit_Employee.html')
def Employee_list(request):
    return render(request,'Employee_list.html')
def View_Employee(request):
    return render(request,'view_Employee.html')
#End Tomtam

#Start Bank
def Orderhis(request):
    return render(request,'Orderhis.html')
def Report(request):
    return render(request,'Report.html')
def Tipsd(request):
    return render(request,'Tipsd.html')
#Stop Bank
