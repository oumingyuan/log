# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from log.picture.tool import get_girl
import socket
from django.http import FileResponse


@csrf_exempt
def download_vue(request):
    url_address = request.GET['url_address']

    byte_array = get_girl.download(url_address)

    return HttpResponse(byte_array)


def file_down(request):
    filename = request.GET['filename']

    print("filename: " + filename)

    file = open(filename, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'

    zip_name = filename[-28:]

    response['Content-Disposition'] = 'attachment;filename=' + zip_name
    return response
