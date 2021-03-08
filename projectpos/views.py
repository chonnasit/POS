# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owners
from .models import Table

# Create your views here.
#Start Tong
log= []
def Login(request):
    return render(request,'Login.html')
def Forgetpassword(request):
    return render(request,'Forgetpassword.html')
def Repassword(request):
    email=request.POST.get('email')
    password= request.POST.get('password')
    passwordnew = request.POST.get('passwordnew')
    passwordnewre = request.POST.get('passwordnewre')
    print(email)
    return render(request,'Repassword.html')
def Tableroom(request):
    email=request.POST.get('email')
    password= request.POST.get('password')
    if email != None:
        log.append(email)
        log.append(password)
        print(log)
    if Owners.objects.filter(email=log[0],password=log[1]).exists():
        tables = Table.objects.all()
        return render(request,'Tableroom.html',{'tables':tables})
    else:
        return render(request)

def Kitchen(request):
    return render(request,'Kitchen.html')
def Raw(request):
    return render(request,'Raw.html')
def Rawmaterial(request):
    return render(request,'Rawmaterial.html')
#End  Tong

#Start Top
    fn=request.POST.get('abcdef',False)
    print(request)
    print(fn)
    if(fn != False):
        addtypefood=AddTypeFood.objects.create(Ftype = fn)
        addtypefood.save()
    
    data=AddTypeFood.objects.all()
    return render(request,'addFood.html',{'posts':data})
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
    data = Owners.objects.all()
    return render(request,'Report.html',{'post':data})
def Tipsd(request):
    return render(request,'Tipsd.html')
#Stop Bank

#start Kris
def AddMenu(request):
    return render(request,'AddMenu.html')
def AddTable(request):
    return render(request,'AddTable.html')
def BillSetting(request):
    return render(request,'BillSetting.html')
def BuyFoodBackHome(request):
    return render(request,'BuyFoodBackHome.html')
def BuyMoreFood(request):
    return render(request,'BuyMoreFood.html')
def ChangeFood(request):
    return render(request,'ChangeFood.html')
def DeleteTable(request):
    return render(request,'DeleteTable.html')
def listCustomer(request):
    data=ListCustomer.objects.all()
    return render(request,'listCustomer.html',{'posts':data})

#End Kris
