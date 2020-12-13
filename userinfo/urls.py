from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'userinfo'
urlpatterns = [
    path('userinfo/',views.index, name='index'),
    path('userinfo/detail/',views.detail,name='detail'),
    path('userinfo/Inputcompares/',views.inputCompares,name='inputCompares'),
    path('userinfo/Inputcompares/compares/',views.Compares,name='Compares'),
    path('',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='userinfo/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='userinfo/logout.html'),name='logout'),
    #path('redirect/',views.redirect_view,name='redirect_view')
]
