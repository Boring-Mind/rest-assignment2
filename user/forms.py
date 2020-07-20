from django.contrib.auth.forms import AuthenticationForm
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from django.conf import settings


# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         """Initialize crispy forms."""
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'id-LoginForm'
#         self.helper.form_class = 'form-group'
#         self.form_method = 'post'
#         self.helper.form_action = reverse_lazy(settings.LOGIN_URL)

#         self.helper.layout = layout.Layout(
#             layout.HTML('<h4 class="text-center">Login</h4>'),
#             'username',
#             'password',
#             layout.Div(
#                 layout.Submit(
#                     'login',
#                     'Login',
#                     css_class='btn-success my-2 px-4'
#                 ),
#                 css_class='text-center'
#             ),
#             layout.Hidden('next', '')
#         )
