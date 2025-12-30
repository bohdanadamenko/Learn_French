from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"

class GuestLoginView(generic.RedirectView):
    url = reverse_lazy("core:index")

    def get(self, request, *args, **kwargs):
        # Get or create a guest user
        guest_user, created = User.objects.get_or_create(
            username='guest',
            defaults={
                'email': 'guest@example.com',
                'first_name': 'Guest',
                'last_name': 'User',
            }
        )
        if created:
            guest_user.set_unusable_password()
            guest_user.save()
        
        login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
        return super().get(request, *args, **kwargs)
