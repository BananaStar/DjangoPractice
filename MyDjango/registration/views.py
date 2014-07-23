from django.shortcuts import render, get_object_or_404
from registration.models import UserInfo


def index(request):
    return render(request, 'registration.html', )


def check(request):
    try:
        user_account = request.POST['User_Account']

    except:
        return render(request, 'registration.html', {
            'check_message': "POST failed",
        })
    try:
        get_object_or_404(UserInfo, pk=user_account)
        return render(request, 'registration.html', {
            'check_message': "This account had been used. Please try other account.",
        })
    except:
        return render(request, 'registration.html', {
            'check_message': "Good",
            'user_account': user_account,
        })


def submit_account(request):

    new_user = UserInfo()
    new_user.userAccount = request.POST['User_Account']
    new_user.userPassword = request.POST['User_Password']
    new_user.userName = request.POST['User_Name']
    new_user.userSex = request.POST['User_Sex']
    new_user.userBirth = request.POST['User_Birth']
    new_user.FillInRegDate()
    new_user.save()

    return render(request, 'reg_result.html', {
        'check_message': 'Welcome '+new_user.userName+', your account had been created.',
    })
