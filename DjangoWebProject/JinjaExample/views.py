from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html',{'card_img': 'https://i.gifer.com/3Pm1.gif' ,'card_name' : 'Снег в июле','card_hash' : '#Атмосфера  #Люблютакуюпогоду'})

def add_card(request):
    return render(request, 'home/posts.html',{'card_img': 'https://99px.ru/sstorage/86/2018/09/image_861809181516444694427.gif' ,'card_name' : 'Дождь','card_hash' : '#Атмосфера'})

def to_post(request):
    return render(request,'home/post.html',{'card_img': 'https://99px.ru/sstorage/86/2018/09/image_861809181516444694427.gif' ,'card_name' : 'Дождь','card_hash' : '#Атмосфера'})