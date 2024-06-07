from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from django.utils import timezone

from dateutil.relativedelta import relativedelta
import calendar as cal

cal.setfirstweekday(cal.SUNDAY)


@login_required
@require_http_methods(["GET"])
def calendar(request):
    days = ["日", "月", "火", "水", "木", "金", "土"]
    date = request.GET.get("date")
    if date:
        today = timezone.datetime.strptime(date, "%Y-%m-%d")
    else:
        today = timezone.now()
    prev_month = today.replace(day=1) - relativedelta(months=1)
    next_month = today.replace(day=1) + relativedelta(months=1)

    params = {
        "days": days,
        "today": today,
        "prev": prev_month,
        "next": next_month,
        "calendar": cal.monthcalendar(today.year, today.month),
    }
    
    if request.htmx:
        return render(request, "calendarapp/boost/calendar.html", params)
    return render(request, "calendarapp/index.html", params)

@login_required
@require_http_methods(["GET"])
def blank_schedule(request):
    return render(request, "calendarapp/blank_schedule.html")

@login_required
@require_http_methods(["GET"])
def clear_blank_schedule(request):
    return render(request, "calendarapp/clear_blank_schedule.html")
