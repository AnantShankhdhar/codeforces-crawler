from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'userinfo'
urlpatterns = [
    path('',views.index, name='index'),
    path('detail/',views.detail,name='detail'),
    path('compares/',views.Compares,name='Compares'),
    path('teamrating/',views.teamrate,name='teamrate'),
    # path('',views.signup,name='signup'),
    # path('login/',auth_views.LoginView.as_view(template_name='userinfo/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='userinfo/logout.html'),name='logout'),
    #path('redirect/',views.redirect_view,name='redirect_view')
]
