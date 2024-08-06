from django.urls import path
from userlogsapp.views import login_page, signup_page,logout_page

urlpatterns = [
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),
    path('signup-page/', signup_page, name='signup_page'),
]
