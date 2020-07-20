from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import status

from .forms import RegisterForm
from .models import UserProfile
from .serializers import ProfileSerializer


class HomeView(generic.TemplateView):
    template_name = "html/base.html"


class RegisterAPIView(generics.CreateAPIView):
    """
    POST /api/register/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        photo = request.data.get('photo')

        if not all((username, email, password)):
            return Response(
                data={
                    'message': 'Fill all required fields!'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        new_user = UserProfile.create(
            username=username,
            email=email,
            password=password,
            photo=photo
        )
        return Response(
            data=ProfileSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )


class RegisterFormView(FormView):
    """
    GET /register_user/
    """
    form_class = RegisterForm
    template_name = 'html/register.html'
    success_url = reverse_lazy('user:home')
