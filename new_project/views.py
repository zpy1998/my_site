from django.shortcuts import render
from new_project.models import Sell48Simple
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    limit=1
    simple=Sell48Simple.objects[:200]
    panginater=Paginator(simple,limit)
    page=request.GET.get("page",1)
    loaded=panginater.page(page)
    context={
        "simlple":loaded
    }
    return render(request,"new_index.html",context)

def blog(request):
    return render(request,"blog.html")

def UI1(request):
    limit=3
    temp=Sell48Simple.objects[:200]
    DuliData=Paginator(temp,limit)
    ChuanSongWay=request.GET.get("page",1)
    DuliPage=DuliData.page(ChuanSongWay)
    context={
        "obs":DuliPage
    }
    return render(request,"semanticUI1.html",context)

def item_page(requset):
    limit=4
    simple=Sell48Simple.objects
    page_data=Paginator(simple,limit)
    page_way=requset.GET.get("page",1)
    load=page_data.page(page_way)
    context={
        "obs":load,
        "counts":simple.count()

    }
    return render(requset,"item_page.html",context)