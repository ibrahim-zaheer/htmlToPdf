from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
import pdfkit
from .models import User

#point it where the exe file is stored
config = pdfkit.configuration(wkhtmltopdf=r"D:/programming tools/wkhtml/wkhtml/bin/wkhtmltopdf.exe")

def home(request):
    return render(request, 'home.html')
# this url will be use to select the current html and turn it into pdf
def generatePdf(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('home')), False, configuration=config)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "file_name.pdf"'
    return response


# this url will be use to select the current html based on specific and turn it into pdf
def generateUserPdf(request,pk):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('SingleUser',args=[pk])), False, configuration=config)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "file_name.pdf"'
    return response
#for listing all the users
def ListUser(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request,'user.html',context)

#for listing specific user
def SingleUser(request,pk):
    user = User.objects.filter(pk = pk)
    context = {'user':user}
    return render(request,'singleuser.html',context)