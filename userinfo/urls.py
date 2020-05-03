from django.urls import path
from . import views

app_name = 'userinfo'
urlpatterns = [
    path('userinfo/',views.index, name='index'),
    path('userinfo/detail/',views.detail,name='detail'),
    path('',views.signup,name='signup'),
    #path('redirect/',views.redirect_view,name='redirect_view')
]
