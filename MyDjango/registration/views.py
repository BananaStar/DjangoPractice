from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from registration.models import UserInfo


def check_available(request, user_account):
    try:
        get_object_or_404(UserInfo, pk=user_account)
        # 302 Found
        return HttpResponse(status=302)
    except:
        # 404 Not found
        return HttpResponse(status=404)


def submit_account(request):
    new_user = UserInfo()
    new_user.userAccount = request.POST['userAccount']
    new_user.userPassword = request.POST['userPassword']
    new_user.userName = request.POST['userName']
    new_user.userSex = request.POST['userSex']
    new_user.userBirth = request.POST['userBirth']
    new_user.FillInRegDate()
    new_user.save()
    # 201 Created
    return HttpResponse(status=201)


def index(request):
    if request.method == 'POST':
        return submit_account(request)
    # 404 Not found
    return HttpResponse(status=404)


def test(request):
    return render(request,'query_response.html',None)