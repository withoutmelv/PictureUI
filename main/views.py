import base64
import json

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from User_model.settings import MEDIA_URL
from main.tools import read_directory
from users.MyForms import ProfileForm
from users.models import UserProfile

from . import Classifier

@login_required
def main(request):
    if request.method == "POST":
        picStream = request.POST.get("picStream")
        picStream_data = str(picStream).split(';base64,')[1]
        data = base64.b64decode(picStream_data)
        print(data)
        ret = {"status": 0, 'url': ''}
        ret['status'] = 1
        ret['url'] = '/index/'
        return HttpResponse(json.dumps(ret))
    return render(request, 'main/main.html')

# 测试成功(该测试在后台调用classify_factory进行预测)
def classify_test(request):
    Classifier.classify_factory.predict_test()
    return render(request, 'main/classify.html')


def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/mainProfile.html', {'user': user, 'url': url})


def classify(request, pk):
    user = get_object_or_404(User, pk=pk)
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/mainClassify.html', {'user': user, 'url': url})


def classifilePerson(request, pk):
    user = get_object_or_404(User, pk=pk)
    listPicname = read_directory("static/"+user.username+"/照片/person")
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/person.html', {'user': user, 'url': url, 'listPicname': listPicname})


def classifilePoint(request, pk):
    user = get_object_or_404(User, pk=pk)
    listPicname = read_directory("static/" + user.username + "/照片/point")
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/point.html', {'user': user, 'url': url, 'listPicname': listPicname})


def classifileVideo(request, pk):
    user = get_object_or_404(User, pk=pk)
    listPicname = read_directory("static/" + user.username + "/照片/video")
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/video.html', {'user': user, 'url': url, 'listPicname': listPicname})


def classifileScenery(request, pk):
    user = get_object_or_404(User, pk=pk)
    listPicname = read_directory("static/" + user.username + "/照片/scenery")
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/scenery.html', {'user': user, 'url': url, 'listPicname': listPicname})


def classifileCutScreen(request, pk):
    user = get_object_or_404(User, pk=pk)
    listPicname = read_directory("static/" + user.username + "/照片/cutScreen")
    url = MEDIA_URL + user.profile.portrait.name
    return render(request, 'main/cutScreen.html', {'user': user, 'url': url, 'listPicname': listPicname})


def personInfo(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(UserProfile, user=user)
    url = MEDIA_URL + user.profile.portrait.name
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            img = request.FILES.get("filepic")
            user_profile.portrait = img
            user_profile.save()

            return HttpResponseRedirect(reverse('main:mainProfile', args=[user.id]))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
                        'org': user_profile.org, 'telephone': user_profile.telephone}
        form = ProfileForm(default_data)
    return render(request, 'main/mainPersonInfo.html', {'form': form, 'user': user, 'url': url})


