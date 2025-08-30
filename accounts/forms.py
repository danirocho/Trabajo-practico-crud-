from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _

class CustomSignupForm(SignupForm):
    captcha = CaptchaField(label=_("verificación"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
