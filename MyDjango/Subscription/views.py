from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from Subscription.models import UserInfo


def index(request):
    return render(request, 'Subscription.html',)


def check(request):
    try:
        user_account = request.POST['User_Account']
    except:
        return render(request, 'Subscription.html', {
            'check_message': "POST failed",
        })
    try:
        get_object_or_404(UserInfo, pk=user_account)
        return render(request, 'Subscription.html', {
            'check_message': "This account had been used. Please try other account.",
        })
    except:
        check_message = 'GOOD'
        return render(request, 'Subscription.html', {
            'check_message': check_message,
        })

