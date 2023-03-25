from django.urls import path
from . import views
urlpatterns = [
    # path('login/', views.Login1, name='login'),
    path('regester/',views.Regester,name='regester'),
    path('accounts/login/',views.loginion,name='login'),
    path('',views.Home,name='home'),
    path('logout/',views.logoutUser,name='logout'),
    path('store/',views.Store,name='store'),
    path('cart/',views.Cart,name='cart'),
    path('checkout/',views.Checkout,name='checkouts'),
    path('update_data/',views.updateData,name='update_data'),
    path('process_order/',views.processOrder,name='process_order'),
    # path('about_us/',views.about_us,name='aboutus')
     ]