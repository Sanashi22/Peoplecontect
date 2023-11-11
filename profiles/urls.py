from django.urls import path
from .views import user_login,signup, update_profile, get_profile, user_logout, ProfileDetailView, get_all_user
 
app_name="profiles"
urlpatterns=[
    path('login',user_login, name="login"),
    path('signup',signup,name="signup"),
    path('update-profile',update_profile, name="update-profile"),
    path('', get_profile, name="profile"),
    path('logout',user_logout, name="logout"),
    path("<int:pk>/profile", ProfileDetailView.as_view(), name="profile-detail"),
    path('peoples', get_all_user, name='peoples')
]