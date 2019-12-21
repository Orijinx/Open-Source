from django.shortcuts import render
from .forms import qr_service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from feed.models import Articles
import datetime
from .QR import QR_GEN, QR_DEG



def micro(request):
    return render(request, 'micro/microservice.html')


def qr_serv(request):
    form = qr_service(request.POST or None)
    if form.is_valid():

        img = form.cleaned_data.get("img_url")
        qr_im = form.cleaned_data.get("qr_img")
        if (qr_im != ''):
         #   deg = QR_DEG(img)
            im = 'data:image/jpeg;base64,' + QR_GEN(img)
            link = img
            context = {'form': form,
                       'src': im,
                       'link': link,
                      # 'deg': deg
                       }

        else:
            context = {'form': form,
                       'src': im,
                       'link': link}

        # s = Articles(img_url=img,
        #              title=tit,
        #              about=abo,
        #              tag=tag,
        #              date=datetime.datetime.now())
        # s.save()

        return render(request, 'includes/QR.html', context)

        # user= authenticate(username=uservalue, password=passwordvalue)
        # if user is not None:
        #     login(request, user)
        #     context= {'form': form,
        #               'error': 'The login has been successful'}

        #     return render(request, 'includes/index.html', context)
        # else:
        #     context= {'form': form,
        #               'error': 'The username and password combination is incorrect'}

        #     return render(request, 'users/accounts.html', context )

    else:
        context = {'form': form}
        return render(request, 'includes/QR.html', context)

# def qr_deg(request):
#      form_deg = qr_degenerate(request.POST or None)
#      if form_deg.is_valid():
#         img = form_deg.cleaned_data.get("qr_img")
#         context = {'form': form_deg,
#                    'link': qr_degenerate(img)}

#         return render(request, 'includes/QR.html', context)
#      else:
#         context = {'form': form_deg}
#         return render(request, 'includes/QR.html', context)


def web_cam(request):
    return render(request, 'includes/vidpot.html')