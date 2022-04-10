from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'index.html')    # to render html

def about_terms_and_conditions(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'about_terms_and_conditions.html')    # to render html
def career(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'career.html')    # to render html
def diet_clinic(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'diet_clinic.html')    # to render html
def medicin_inquiry(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'medicin_inquiry.html')    # to render html
def out_products(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'out_products.html')    # to render html
def why_sirmanojpharma(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'why_sirmanojpharma.html')    # to render html

def contact(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'contact.html')    # to render html


