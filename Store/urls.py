from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from Store import views

urlpatterns = [
                  path('404', views.ERROR404, name='404'),
                  path('', views.INDEX, name='home'),
                  path('about', views.About, name='about'),
                  path('contact', views.Contact, name='contact'),
                  path('product', views.PRODUCT, name='product'),
                  path('account/my_account', views.My_Account, name='my_account'),
                  path('base/', views.BASE, name='base'),
                  path('product/<slug:slug>', views.Product_Details, name='product_detail'),
                  path('product/filter-data', views.filter_data, name="filter-data"),
                  path('account/register', views.REGISTER, name='handleregister'),
                  path('account/login', views.LOGIN, name='handlelogin'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/profile', views.PROFILE, name='profile'),
                  path('account/update/profile', views.UPDATE_PROFILE, name='update_profile'),

                  # cart url

                  path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
                  path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
                  path('cart/item_increment/<int:id>/',
                       views.item_increment, name='item_increment'),
                  path('cart/item_decrement/<int:id>/',
                       views.item_decrement, name='item_decrement'),
                  path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
                  path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

                  path('checkout/checkout',views.Check,name='checkout')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
