from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from datetime import datetime, timedelta
import json
from typing import Dict,Union, List
from django.views.decorators.csrf import csrf_exempt 
from .models import Post
from .models import Contacts

# Create your views here.
@csrf_exempt

def home(request:HttpRequest):
    if request.method=='GET':
        posts = Post.objects.all()
        contacts = Contacts.objects.all() 
        return render(request, 'home.html',{"data":posts,"data2":contacts})
    elif request.method=='POST':
        body= json.loads(request.body)
        title = body.get("title")
        print(title)
        post = Post(title=title)
        post.save()
        return JsonResponse({"title":title},status = 201)



    
    
@csrf_exempt
def contacts(request:HttpRequest):
    if request.method=='GET':
        contacts = Contacts.objects.all() 
        return render(request,'contacts.html',{"data":contacts})
    elif request.method=='POST':
        body = json.loads(request.body)
        firstname = body.get("firstname")
        lastname = body.get("lastname")
        email = body.get("email")
        phonenumber = body.get("phonenumber")
        text = body.get("text")
        contact = Contacts(firstName=firstname,lastName=lastname,email=email,phoneNumber=phonenumber,text=text)
        contact.save()
        return JsonResponse({"firstname":firstname},status=201)


def about(request):
    return render(request,'about.html')
def hw(request):
    current_time = datetime.now()
    return render(request,'hw.html',context={"current_time":current_time})
def mult_table(request):
    table = []
    for i in range(1,11):
        row = []
        for j in range(1,11):
            row.append(i*j)
        table.append(row)
    return render(request,'table.html',context={"table":table})
def programer_day(request):
    current_year = datetime.now().year
    start_of_year = datetime(current_year, 1, 1)
    programmer_day = start_of_year + timedelta(days=255)
    return render(request,'programer_day.html',context={"programmer_day":programmer_day})
    