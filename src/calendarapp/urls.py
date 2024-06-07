from django.urls import re_path

from . import views

app_name = "calendarapp"

urlpatterns = [
    re_path(r"^$", views.calendar, name="index"),
    re_path(r"^/blank-schedule$", views.blank_schedule, name="blank-schedule"),
    re_path(r"^/clear-blank-schedule$", views.clear_blank_schedule, name="clear-blank-schedule"),
]
