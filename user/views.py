from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status

from .forms import RegisterForm
from .models import UserProfile
from .serializers import ProfileSerializer, UserSerializer


class HomeView(generic.TemplateView):
    template_name = "html/base.html"


class RegisterAPIView(generics.CreateAPIView):
    """POST /api/register/."""

    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def init_from_dict(self, data: dict):
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password1')
        self.password2 = data.get('password2')
        self.photo = data.get('photo')

    def post(self, request, *args, **kwargs):
        if len(request.POST) > 1:
            form = RegisterForm(request.POST)
            if form.is_valid():
                self.init_from_dict(request.POST)
                self.photo = request.FILES.get('photo')
            else:
                return render(request, 'html/register.html', {'form': form})
        else:
            self.init_from_dict(request.data)

        new_user = UserProfile.objects.create(
            username=self.username,
            email=self.email,
            password=self.password,
            photo=self.photo
        )
        return Response({
            'data': ProfileSerializer(new_user).data,
            'status': status.HTTP_201_CREATED
        })


class RegisterFormView(FormView):
    """GET /register_user/."""

    form_class = RegisterForm
    template_name = 'html/register.html'
    success_url = reverse_lazy('user:home')


class ListUsersAPIView(generics.ListAPIView):
    """GET list_users/."""

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list_view(request):
    qs = UserProfile.objects.select_related('user').only(
        'user__id', 'user__username', 'user__email', 'photo'
    )
    data = []
    for profile in list(qs):
        data.append({
            'id': profile.user.id,
            'username': profile.user.username,
            'email': profile.user.email,
            'photo': profile.photo
        })
    return render(request, 'html/list_users.html', {'data': data})
