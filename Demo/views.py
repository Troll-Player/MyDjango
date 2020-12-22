from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Demo.models import Book, Publisher, User_data


def addbooks(request):
    bookname = request.GET.get('bookname')
    books = Book()
    books.bname = bookname
    books.save()
    return HttpResponse('添加成功 %s' % books.bname)


def addpub(request):
    pubname = request.GET.get('pubname')
    publish = Publisher()
    publish.pname = pubname
    publish.save()
    return HttpResponse('添加成功 %s' % publish.pname)

def bind_pub(request):
    books = Book.objects.get(pk=12)
    publish = Publisher.objects.get(pk=6)
    books.pub = publish
    books.save()
    return HttpResponse('绑定成功')

def selectdata(request):
    i = request.GET.get('i')
    pub = Publisher.objects.get(pk=i)
    books = pub.book.all()
    return render(request, 'showdata.html', context=locals())

def upload(request):
    if request.method == "GET":
        return render(request, 'uploads.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        picture = request.FILES.get('picture')
        user = User_data()
        user.uname = username
        user.icon = picture
        user.save()
        return redirect(reverse("Demo:mine", kwargs={"username": user.uname}))

def mine(request, username):
    user = User_data.objects.get(uname=username)
    data = {
        "username": username,
        "icon_url": "/static/uploads/" + user.icon.url,
    }
    return render(request, 'mine.html', context=data)
