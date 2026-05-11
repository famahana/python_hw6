from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from datetime import datetime, timedelta
import json
from typing import Dict,Union, List
from django.views.decorators.csrf import csrf_exempt 
from .models import Post
from .models import Contacts
from .models import Restraunt

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
def song_en(request):
    context = {
        "title": "English",
        "song": "Yesterday, all my troubles seemed so far away\nNow it looks as though they're here to stay\nOh, I believe in yesterday"
    }
    return render(request,'song.html',context)
def song_fr(request):
    context = {
        "title": "French",
        "song": "Hier, toutes mes peines semblaient si lointaines\nMaintenant, il semble que elles sont ici pour rester\nOh, je crois en hier"
    }
    return render(request,'song.html',context)
def song_de(request):
    context = {
        "title": "German",
        "song": "Gestern, all meine Sorgen schienen so weit weg\nJetzt sieht es so aus, als würden sie hier bleiben\nOh, ich glaube an gestern"
    }
    return render(request,'song.html',context)
def song_es(request):
    context = {
        "title": "Spanish",
        "song": "Ayer, todas mis preocupaciones parecían tan lejanas\nAhora parece que están aquí para quedarse\nOh, creo en ayer"
    }
    return render(request,'song.html',context)
@csrf_exempt
def registration_form(request):
        if request.method == 'POST':
           data_json = json.loads(request.body)
           data = {
                "first_name": data_json.get("first_name"),
                "last_name": data_json.get("last_name"),
                "age": data_json.get("age"),
                "email": data_json.get("email"),
                "gender": data_json.get("gender"),
                "address": data_json.get("address"),
                "subscribe": data_json.get("subscribe")
           }
           return JsonResponse(data)
        elif(request.method == 'GET'):
             return render(request,'registration_form.html')
        
@csrf_exempt
def restraunt_(request:HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body.get("name")
        specialization = body.get("specialization")
        adress = body.get("adress")
        web_url = body.get("web_url")
        phone_number = body.get("phone_number")
        restraunt = Restraunt(name=name,specialization=specialization,adress=adress,web_url=web_url,phone_number=phone_number)
        restraunt.save()
        return JsonResponse({"name":name},status=201)
    elif request.method == 'GET':
        restraunts = Restraunt.objects.all() 
        return render(request,'restraunt.html',{"data":restraunts})
@csrf_exempt
def delete_restraunt(request:HttpRequest,id):
    if request.method == 'POST':
        try:
            restraunt = Restraunt.objects.get(id=id)
            restraunt.delete()
            return JsonResponse({"message": "Ресторан видалено"}, status=200)
        except Restraunt.DoesNotExist:
            return JsonResponse({"message": "Ресторан не знайдено"}, status=404)
@csrf_exempt
def update_restraunt(request:HttpRequest,id):
    if request.method == 'POST':
        body = json.loads(request.body)
        restraunt = Restraunt.objects.get(id=id)
        restraunt.name = body.get("name")
        restraunt.specialization = body.get("specialization")
        restraunt.adress = body.get("adress")
        restraunt.web_url = body.get("web_url")
        restraunt.phone_number = body.get("phone_number")
        restraunt.save()
        return JsonResponse({"status": "updated"})
@csrf_exempt    
def search_restraunt(request):
    query = request.GET.get("q", "")

    results = Restraunt.objects.filter(
        specialization__icontains=query
    )

    data = []
    for r in results:
        data.append({
            "id": r.id,
            "name": r.name,
            "specialization": r.specialization,
            "adress": r.adress,
            "web_url": r.web_url,
            "phone_number": r.phone_number,
        })

    return JsonResponse(data, safe=False)