from django.contrib import admin
from django.urls import path
from morphise import views

urlpatterns = [
    path("",views.index,name="morphise"),
    path("index",views.index,name="index"),
    path("blog",views.blog,name="blog"),
    path("blog",views.blog,name="services"),
    path("about",views.about,name="about"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("mainpage",views.mainpage,name="mainpage"),
    path("services",views.services,name="services"),
    path("login_view",views.login_view,name="login_view"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("aioutput",views.aioutput,name="aioutput"),
    path("test",views.test,name="test")
]