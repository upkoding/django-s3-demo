import uuid
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import File
from .forms import UploadForm


def index(request):
    return render(request, 'sharing/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            formfile = form.save(commit=False)
            uid = uuid.uuid1()
            formfile.uid = str(uid)
            formfile.save()
            return HttpResponseRedirect('/' + formfile.uid)

    return render(request, 'sharing/index.html')


def download(request, uid):
    file = get_object_or_404(File, uid=uid)
    return render(request, 'sharing/download.html', {'dl_url': file.file.url, 'filename': file.file.name.split('/')[-1]})
