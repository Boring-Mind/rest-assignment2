from django.urls import path
import user.views as userviews

app_name = 'user'

urlpatterns = [
    path('', userviews.HomeView.as_view(), name='home'),
    # path('login/', userviews.LoginView.as_view(), name='login'),
]
