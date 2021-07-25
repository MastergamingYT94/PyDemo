from django.urls import path
<<<<<<< HEAD
from .views import welcome

urlpatterns = [
    path('', welcome, name='welcome')
=======
from .screens import views
from .screens import manage

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('Home', views.home, name='home'),
    path('manage', manage.manage, name='manage'),
    path('manage/products', manage.manage_products, name='manage_products'),
    path('manage/products/edit/<int:product_Id>',
         manage.product_edit, name='product_edit'),
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
]
