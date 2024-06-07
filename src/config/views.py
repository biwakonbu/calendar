from django.shortcuts import render
from allauth.account.views import LoginView, LogoutView
from django.urls import reverse
from django_htmx.http import HttpResponseClientRedirect


class CalendarLoginView(LoginView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        if request.user.is_authenticated:
            return HttpResponseClientRedirect(reverse("calendarapp:index"))
        return render(
            self.request,
            "utility/toast/error.html",
            {"message": "メールアドレスかパスワードが一致しません"},
        )


class CalendarLogoutView(LogoutView):
    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return HttpResponseClientRedirect(reverse("signin"))
