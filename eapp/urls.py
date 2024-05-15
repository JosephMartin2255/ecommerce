from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logincreate',views.logincreate,name='logincreate'),
    path('logout',views.logout,name='logout'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addcategory1',views.addcategory1,name='addcategory1'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('addproducts1',views.addproducts1,name='addproducts1'),
    path('viewproducts',views.viewproducts,name='viewproducts'),
    path('deleteproducts/<int:id>',views.deleteproducts,name='deleteproducts'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('deleteusers/<int:id>',views.deleteusers,name='deleteusers'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('usersignup1',views.usersignup1,name='usersignup1'),
    path('userhomepage',views.userhomepage,name='userhomepage'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
    path('categorypage/<int:id>',views.categorypage,name='categorypage'),
    path('cart/<int:product_id>/', views.cart, name='cart'),
    path('cartde',views.cartde, name='cartde'),
    path('increase/<int:k>', views.increase, name='increase'),
    path('decrease/<int:k>', views.decrease, name='decrease'),
    path('remove/<int:k>', views.remove, name='remove'),
   
    


    path('checkoutpage',views.checkoutpage,name='checkoutpage'),
    

    
]