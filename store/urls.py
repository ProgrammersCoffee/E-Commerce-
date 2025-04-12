"""
URL configuration for clothing_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import product_list
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# add the path of the image

urlpatterns = [
    path('admin/', admin.site.urls),  # مسار صفحة الإدارة
    path('products/', product_list, name='product_list'),
    path('',product_list,name='home') ,# مسار عرض المنتجات
    # THIS will make django know how to send images to users
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
