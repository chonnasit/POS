# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owners
from .models import Table
from django.core.mail import send_mail
from .models import Order
from .models import Tip
from .models import Q
from .models import Employee
# Create your views here.
# Start Tong
log = []


def Login(request):
    return render(request, 'Login.html')


def Forgetpassword(request):
    email = request.POST.get('email', "x")
    idcard = request.POST.get('idcard', "x")
    return render(request, 'Forgetpassword.html')


def sub(request):
    email = request.POST.get('email')
    idcard = request.POST.get('idcard')

    p = Owners.objects.get(email=email, ID_card=idcard)
    print(p)
    if p:
        send_mail('Thank you for registering to our site', p.password,
                  'chonnasit.s@ku.th', ['tong25658@gmail.com'], fail_silently=False)
    return render(request, 'Login.html')


def Repassword(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    passwordnew = request.POST.get('passwordnew', "d")
    passwordnewre = request.POST.get('passwordnewre')
    if passwordnew == passwordnewre:
        p = Owners.objects.get(email=email, password=password)
        p.password = passwordnew
        p.save()
    return render(request, 'Repassword.html')


def removeq(request):
    removeq = request.POST.get('listQ')
    res = request.POST.get('Qg', None)
    print(removeq)
    print(res)
    if removeq != None:
        tables = Table.objects.get(number=res)
        tables.Order_id = res
        tables.status_table = "Y"
        tables.save()
        q = Q.objects.get(id=removeq)
        q.delete()
    if Owners.objects.filter(email=log[0], password=log[1]).exists():
        tables = Table.objects.all()
        q = Q.objects.all()
        return render(request, 'Tableroom.html', {'tables': tables, 'q': q})


def Tableroom(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email != None:
        log.append(email)
        log.append(password)
    if Owners.objects.filter(email=log[0], password=log[1]).exists():
        tables = Table.objects.all()

        q = Q.objects.all()
        return render(request, 'Tableroom.html', {'tables': tables, 'q': q})
    else:
        log.remove(log[0])
        log.remove(log[0])
        return render(request, 'Login.html',  {'alert_flag': True})


def Kitchen(request):
    return render(request, 'Kitchen.html')


def Raw(request):
    return render(request, 'Raw.html')


def Rawmaterial(request):
    return render(request, 'Rawmaterial.html')
# End  Tong

# Start Top


def AddMenu(request):
    return render(request, 'AddMenu.html')


def DeleteDrink(request):
    return render(request, 'deleteDrink.html')


def DeleteFood(request):
    return render(request, 'deleteFood.html')


def Deleteice(request):
    return render(request, 'deleteice.html')


def Drink(request):
    return render(request, 'Drink.html')


def Food(request):
    tableadd = request.POST.get('product', "No Table")
    Q = request.POST.get('Q', " None")
    typeorder = request.POST.get('typeorder', "Restaurant")
    print(tableadd)
    print(Q)
    print(typeorder)
    return render(request, 'food.html')


def Ice_Cream(request):
    return render(request, 'Ice cream.html')


def SellectCategory(request):
    return render(request, 'sellectCategory.html')
# End top

# Start Frong


def Cash(request):
    return render(request, 'Cash.html')


def Cash_Success(request):
    return render(request, 'Cash_Success.html')


def Transfer(request):
    return render(request, 'Transfer.html')


def Transfer_Success(request):
    return render(request, 'Transfer_Success.html')
# End Frong


def Delete_employee(request):
    id = request.POST['delete']
    delete_em = Employee.objects.get(id=id)
    delete_em.delete()

    data_all = Employee.objects.all()
    return render(request, 'Employee_list.html', {'data': data_all})


def Add_Employee(request):
    return render(request, 'Add_Employee.html')


def add_database(request):
    fname = request.POST['fname']
    lname = request.POST['lname']

    ID_card_number = request.POST['ID_card_number']
    ID_Employee = request.POST['ID_Employee']
    user = request.POST['user']
    password = request.POST['password']

    House_No = request.POST['House_No']
    Village_No = request.POST['Village_No']
    Sub_area = request.POST['Sub_area']
    Area = request.POST['Area']
    Province = request.POST['Province']

    address = House_No + " "+"หมู่ที่"+" "+Village_No+" "+"ตำบล" + \
        " "+Sub_area+" "+"เอาเภอ"+" "+Area+" "+"จังหวัด"+" "+Province

    position = request.POST['position']
    salary = request.POST['salary']
    email = request.POST['email']
    phone = request.POST['phone']
    bank = request.POST['bank']
    Bankaccount = request.POST['Bankaccount']
    emp = Employee.objects.create(
        firstname=fname,
        Lastname=lname,

        ID_card=ID_card_number,
        ID_job=ID_Employee,
        User=user,
        password=password,

        address=address,


        jobposition=position,
        Salary=salary,
        email=email,
        phone=phone,
        Bank=bank,
        ID_bank=Bankaccount
    )
    emp.save()
    data_all = Employee.objects.all()
    return render(request, 'Employee_list.html', {'data': data_all})


def Edit_Employee(request):
    id = request.POST['edit']
    edit_em = Employee.objects.get(id=id)
    n = edit_em.address
    x = n.split()
    return render(request, 'edit_Employee.html', {'edit_em': edit_em,
                                                  'x1': x[0],
                                                  'x2': x[2],
                                                  'x3': x[4],
                                                  'x4': x[6],
                                                  'x5': x[8]
                                                  })


def update_Employee(request):

    House_No = request.POST['House_No']
    Village_No = request.POST['Village_No']
    Sub_area = request.POST['Sub_area']
    Area = request.POST['Area']
    Province = request.POST['Province']
    address = House_No + " "+"หมู่ที่"+" "+Village_No+" "+"ตำบล" + \
        " "+Sub_area+" "+"เอาเภอ"+" "+Area+" "+"จังหวัด"+" "+Province

    id = request.POST['update']
    update_em = Employee.objects.get(id=id)

    update_em.firstname = request.POST['fname']
    update_em.Lastname = request.POST['lname']
    update_em.ID_card = request.POST['ID_card_number']
    update_em.ID_job = request.POST['ID_Employee']
    update_em.User = request.POST['user']
    update_em.password = request.POST['password']
    update_em.address = address
    update_em.jobposition = request.POST['position']
    update_em.Salary = request.POST['salary']
    update_em.email = request.POST['email']
    update_em.phone = request.POST['phone']
    update_em.Bank = request.POST['bank']
    update_em.ID_bank = request.POST['Bankaccount']

    update_em.save()

    data_all = Employee.objects.all()
    return render(request, 'Employee_list.html', {'data': data_all})


def Employee_list(request):
    data_all = Employee.objects.all()
    return render(request, 'Employee_list.html', {'data': data_all})


def View_Employee(request):
    id = request.POST['view']
    view_em = Employee.objects.get(id=id)
    n = view_em.address
    x = n.split()
    return render(request, 'view_Employee.html', {'view_em': view_em,
                                                  'x1': x[0],
                                                  'x2': x[2],
                                                  'x3': x[4],
                                                  'x4': x[6],
                                                  'x5': x[8]
                                                  })


# End Tomtam

# Start Bank


def Orderhis(request):
    order = Order.objects.all()
    return render(request, 'Orderhis.html', {'order': order})


def Report(request):
    # Query Data From Model
    report = Owners.objects.all()
    return render(request, 'Report.html', {'report': report})


def Tipsd(request):
    tips = Tip.objects.all()
    return render(request, 'Tipsd.html', {'tips': tips})
# Stop Bank

# start Kris


def AddMenu(request):
    return render(request, 'AddMenu.html')


def AddTable(request):
    return render(request, 'AddTable.html')


def BillSetting(request):
    return render(request, 'BillSetting.html')


def BuyFoodBackHome(request):
    return render(request, 'BuyFoodBackHome.html')


def BuyMoreFood(request):
    return render(request, 'BuyMoreFood.html')


def ChangeFood(request):
    return render(request, 'ChangeFood.html')


def DeleteTable(request):
    return render(request, 'DeleteTable.html')


def listCustomer(request):
    data = ListCustomer.objects.all()
    return render(request, 'listCustomer.html', {'posts': data})

# End Kris
