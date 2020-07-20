from django.urls import path
import user.views as userviews

app_name = 'user'

urlpatterns = [
    path('', userviews.HomeView.as_view(), name='home'),
    path(
        'api/register/',
        userviews.RegisterAPIView.as_view(),
        name='api-register'
    ),
    path(
        'register_user/',
        userviews.RegisterFormView.as_view(),
        name='form-register'
    ),
]
