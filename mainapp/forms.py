from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField()
