from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    onwer_name = get_object_or_404(Passcard, passcode=passcode)
    visits_from_passcard = get_list_or_404(Visit, passcard=onwer_name)
    this_passcard_visits = []
    for visit in visits_from_passcard:
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': onwer_name,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
