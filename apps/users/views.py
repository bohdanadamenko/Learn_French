from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
    """Form for updating user profile information."""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


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


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """Display user profile information."""
    template_name = "users/profile.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Check if user is connected via Google
        is_google_user = user.socialaccount_set.filter(provider='google').exists() if hasattr(user, 'socialaccount_set') else False
        
        # Check if user is a guest
        is_guest = user.username == 'guest'
        
        context['is_google_user'] = is_google_user
        context['is_guest'] = is_guest
        context['initials'] = self._get_initials(user)
        return context

    def _get_initials(self, user):
        """Generate user initials for avatar."""
        if user.first_name and user.last_name:
            return f"{user.first_name[0]}{user.last_name[0]}".upper()
        elif user.first_name:
            return user.first_name[:2].upper()
        elif user.username:
            return user.username[:2].upper()
        return "U"


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Allow users to update their profile information."""
    model = User
    form_class = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("users:profile")
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        return self.request.user
