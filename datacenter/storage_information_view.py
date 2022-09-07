from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration



def storage_information_view(request):
    non_closed_visits = []
    not_end_visit = Visit.objects.filter(leaved_at__isnull=True)
    for visit in not_end_visit:
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
