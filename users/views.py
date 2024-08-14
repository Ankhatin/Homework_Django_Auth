import secrets
import string
import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView


from users.forms import UserRegisterForm
from users.models import User



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        user.token = token
        user.save()
        url = f'http://{host}/users/email-confirm/{token}'
        send_to = form.cleaned_data['email']
        send_mail('Верификация почты',
                  f'Подтвердите свою электронную почту {url}',
                  None,
                  [send_to],
                  fail_silently=False)
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(8))
        user.password = make_password(password)
        user.save()
        send_mail('Сброс пароля',
                  f'Ваш новый пароль {password}',
                  None,
                  [user.email],
                  fail_silently=False)
        return redirect(reverse('users:login'))
    return render(request, 'users/reset_password.html')

