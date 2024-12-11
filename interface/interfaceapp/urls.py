from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    
    path('', views.shop_list, name='shop_list'),
    path('signup/',views.sign_up, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add-shop/', views.add_shop, name='add_shop'),
    path('shop_search/', views.shop_search, name='shop_search'),
    path('shop_detail/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('shop/<int:shop_id>/submit_review/', views.submit_review, name='submit_review'),
    path('cantact', views.Cantact_User, name='cantact'),
    path('succuess',views.succuess,name ='succuess'),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)