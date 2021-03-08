"""POS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from projectpos import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [

    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.Login),
    url(r'Forgetpassword', views.Forgetpassword),
    url(r'Repassword', views.Repassword),
    url(r'Tableroom', views.Tableroom),
    url(r'Kitchen', views.Kitchen),
    url(r'^Raw/', views.Raw),
    url(r'Rawmaterial/', views.Rawmaterial),
    
    #end Tong
    url(r'AddFood', views.AddMenu),
    url(r'DeleteDrink', views.DeleteDrink),
    url(r'DeleteFood', views.DeleteFood),
    url(r'Deleteice', views.Deleteice),
    url(r'Drink', views.Drink),
    url(r'Food/', views.Food),
    url(r'Ice_Cream', views.Ice_Cream),
    url(r'SellectCategory', views.SellectCategory),
    #end top
    url(r'Cash', views.Cash),
    url(r'Cash_Success', views.Cash_Success),
    url(r'Transfer', views.Transfer),
    url(r'Transfer_Success', views.Transfer_Success),
    #end Frong
    url(r'Add_Employee', views.Add_Employee),
    url(r'Edit_Employee', views.Edit_Employee),
    url(r'Edit_Food', views.Edit_Food),
    url(r'Employee_list', views.Employee_list),
    url(r'View_Employee', views.View_Employee),
    #end Tomtam
    url(r'Orderhis', views.Orderhis),
    url(r'Report', views.Report),
    url(r'Tipsd', views.Tipsd),
    #end Bank
]
urlpatterns += staticfiles_urlpatterns()
