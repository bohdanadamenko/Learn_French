from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"
