"""expensemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home

#from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('api/income/', include('income.urls')),
    path('api/daybook/', include('daybook.urls')),
    path('api/users/', include('users.urls')),
    path('', home, name= 'home'),

]

admin.site.index_title = 'Site Admin'               
admin.site.site_title = 'Expense Manager'



