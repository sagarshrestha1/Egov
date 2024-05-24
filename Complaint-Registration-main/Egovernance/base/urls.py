from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),#login as user
    path('logout/',views.logout_view,name="logout"), 
    path('signup/',views.signup,name="signup"), #register user
    path('register',views.register_complaint,name="register-complaint"), #register complaint
    path('complaint',views.view_complaint,name="view"), #view complaint
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)