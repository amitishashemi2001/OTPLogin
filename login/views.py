from random import randint
from django.shortcuts import render, redirect
from .forms import UserInfoForm, UserInfo
from kavaengar import *
def collect_user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info = form.save()
            kave_negar_token_send(user_info.phone, randint(1000, 9999) )
            return redirect('verify_code', user_info.pk)
    else:
        form = UserInfoForm()

    return render(request, 'login/collect_user_info.html', {'form': form})

def verify_verification_code(request, pk):
    user_info = UserInfo.objects.get(pk=pk)

    if request.method == 'POST':
        verification_code = request.POST['verification_code']
        if user_info.verification_code == verification_code:
            user_info.is_verified = True
            user_info.save()

            return redirect('index')
        else:
            error_message = "کد تأیید اشتباه است."
    else:
        error_message = None

    return render(request, 'login/verify_verification_code.html', {'error_message': error_message})

def kave_negar_token_send(receptor, token):
    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'receptor': receptor,
            'template': 'your_template',
            'token': token
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


