# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner

# Create your views here.
#Start Tong
def Login(request):
    return render(request,'Login.html')
def Forgetpassword(request):
    return render(request,'Forgetpassword.html')
def Repassword(request):
    return render(request,'Repassword.html')
def Tableroom(request):
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
    #Query Data From Model
    data = Owner.objects.all()
    return render(request,'Report.html',{'posts':data})
def Tipsd(request):
    return render(request,'Tipsd.html')
#Stop Bank
