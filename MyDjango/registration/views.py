from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from registration.models import UserInfo


def check_available(request, user_account):
    try:
        get_object_or_404(UserInfo, userAccount=user_account)
        # 302 Found
        return HttpResponse(status=302)
    except:
        # 404 Not found
        return HttpResponse(status=404)


def submit_account(request):
    try:
        user = UserInfo.objects.create_user(
            userAccount=request.POST['userAccount'],
            userName=request.POST['userName'],
            password=request.POST['userPassword'], )
        user.userSex = request.POST['userSex']
        user.userBirth = request.POST['userBirth']
        user.save()
        # 201 Created
        return HttpResponse(status=201)
    except:
        # 409 Conflict
        return HttpResponse(status=409, content='Account existed')


def index(request):
    if request.method == 'POST':
        return submit_account(request)
    # 404 Not found
    return HttpResponse(status=404)


# For testing
def test(request):
    return render(request, 'query_response.html', None)


def test2(request):
    return render(request, 'registration.html', None)