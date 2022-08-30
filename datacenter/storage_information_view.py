from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    not_end_visit = Visit.objects.filter(leaved_at=None)
    for visit in not_end_visit:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        moscow_entered_time = f'{localtime(visit.entered_at).date()} {localtime(visit.entered_at).time()} '
        visit_info = {
            'who_entered': '{}'.format(visit.passcard.owner_name),
            'entered_at': '{}'.format(moscow_entered_time),
            'duration': '{}'.format(formatted_duration),
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
