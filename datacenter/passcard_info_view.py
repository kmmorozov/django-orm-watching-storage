from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long
from django.utils.timezone import localtime
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    onwer_name = get_object_or_404(Passcard, passcode=passcode)
    visit_from_passcard = get_list_or_404(Visit, passcard=onwer_name)
    this_passcard_visits = []
    for visit in visit_from_passcard:
        entered_date = localtime(visit.entered_at).date()
        entered_time = localtime(visit.entered_at).time()
        entered_at = f'дата: {entered_date}   время: {entered_time}'
        long_visit = is_visit_long(visit)
        duration = get_duration(visit)
        formated_duration = format_duration(duration)
        this_passcard_visits.append(
            {
            'entered_at': '{}'.format(entered_at),
            'duration': '{}'.format(formated_duration),
            'is_strange': '{}'.format(long_visit)
        }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
