from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from .models import Domestic, International, Hotel, Bus, Car, Testimonial, Header
from marketing.models import Signup
from .filters import DomesticFilter


def bus(request):
    bus_list = Bus.objects.filter(featured=True)
    context = {
        'bus_list' : bus_list
    }
    return render(request, 'bus.html', context)

def car(request):
    car_list = Car.objects.filter(featured=True)
    context = {
        'car_list' : car_list
    }
    return render(request, 'car.html', context)


def search_hotel(request):
    queryset = Hotel.objects.all()
    query = request.GET.get('q')
    if query: 
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'search_hotel.html', context)



def search_int(request):
    queryset = International.objects.all()
    query = request.GET.get('q')
    if query: 
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'search_int.html', context)



def search(request):
    queryset = Domestic.objects.all()
    query = request.GET.get('q')
    if query: 
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'search_result.html', context)



def get_dom_tag_count():
    queryset = Domestic.objects.values('tag')
    return queryset

def get_dom_inclusion_count():
    queryset = Domestic.objects.values('inclusiones__title').annotate(Count('inclusiones__title'))
    return queryset


def home(request):
    latest = Domestic.objects.order_by('-timestamp') [0:3]
    recent_list = International.objects.order_by('-timestamp') [0:3]
    testimonial_list = Testimonial.objects.filter(featured=True)
    header_list = Header.objects.filter(featured=True)
    context = {
        'latest' : latest,
        'recent_list' : recent_list,
        'testimonial_list' : testimonial_list,
        'header_list' : header_list
    }
    return render(request, 'home.html', context)

def domestic(request):
    instagram_feeds = Domestic.objects.order_by('-timestamp') [0:6]
    dom_tag_count = get_dom_tag_count()
    dom_inclusion_count = get_dom_inclusion_count()
    object_list = Domestic.objects.filter(featured=True)
    myFilter = DomesticFilter(request.GET, queryset=object_list)
    object_list = myFilter.qs
    paginator = Paginator(object_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try : 
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator, num_pages)

    most_recent = Domestic.objects.order_by('-timestamp') [0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'myFilter' : myFilter,
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'most_recent' : most_recent,
        'dom_inclusion_count' : dom_inclusion_count,
        'dom_tag_count' : dom_tag_count,
        'instagram_feeds' : instagram_feeds,

    }
    return render(request, 'domestic.html', context)


def domestic_detail(request, slug):
    instagram_feeds = Domestic.objects.order_by('-timestamp') [0:6]
    domestic = get_object_or_404(Domestic, slug=slug)
    dom_inclusion_count = get_dom_inclusion_count()
    dom_tag_count = get_dom_tag_count()
    most_recent = Domestic.objects.order_by('-timestamp') [0:3]
    context = {
        'instagram_feeds' : instagram_feeds,
        'domestic' : domestic,
        'dom_inclusion_count' : dom_inclusion_count,
        'dom_tag_count' : dom_tag_count,
        'most_recent' : most_recent,
    }

    return render(request, 'domestic_detail.html', context)






def get_int_tag_count():
    queryset = International.objects.values('tag')
    return queryset

def get_int_inclusion_count():
    queryset = International.objects.values('inclusiones__title').annotate(Count('inclusiones__title'))
    return queryset



def international(request):
    instagram_feeds = International.objects.order_by('-timestamp') [0:6]
    int_tag_count = get_int_tag_count()
    int_inclusion_count = get_int_inclusion_count()
    object_list = International.objects.filter(featured=True)
    paginator = Paginator(object_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try : 
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator, num_pages)

    most_recent = International.objects.order_by('-timestamp') [0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'most_recent' : most_recent,
        'int_inclusion_count' : int_inclusion_count,
        'int_tag_count' : int_tag_count,
        'instagram_feeds' : instagram_feeds,

    }
    return render(request, 'inter.html', context)


def international_detail(request, slug):
    instagram_feeds = International.objects.order_by('-timestamp') [0:6]
    international = get_object_or_404(International, slug=slug)
    int_tag_count = get_int_tag_count()
    int_inclusion_count = get_int_inclusion_count()
    most_recent = International.objects.order_by('-timestamp') [0:3]
    context = {
        'instagram_feeds' : instagram_feeds,
        'international' : international,
        'int_inclusion_count' : int_inclusion_count,
        'int_tag_count' : int_tag_count,
        'most_recent' : most_recent,
    }

    return render(request, 'inter-detail.html', context)






def get_tag_count():
    queryset = Hotel.objects.values('tag')
    return queryset

def get_inclusion_count():
    queryset = Hotel.objects.values('inclusiones__title').annotate(Count('inclusiones__title'))
    return queryset


def hotel(request):
    instagram_feeds = Hotel.objects.order_by('-timestamp') [0:6]
    tag_count = get_tag_count()
    inclusion_count = get_inclusion_count()
    object_list = Hotel.objects.filter(featured=True)
    paginator = Paginator(object_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try : 
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator, num_pages)

    most_recent = Hotel.objects.order_by('-timestamp') [0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'most_recent' : most_recent,
        'inclusion_count' : inclusion_count,
        'tag_count' : tag_count,
        'instagram_feeds' : instagram_feeds,

    }
    return render(request, 'hotel.html', context)

def hotel_detail(request, slug):
    tag_count = get_tag_count()
    inclusion_count = get_inclusion_count()
    instagram_feeds = Hotel.objects.order_by('-timestamp') [0:6]
    hotel = get_object_or_404(Hotel, slug=slug)
    int_tag_count = get_int_tag_count()
    int_inclusion_count = get_int_inclusion_count()
    most_recent = Hotel.objects.order_by('-timestamp') [0:3]
    context = {
        'inclusion_count' : inclusion_count,
        'tag_count' : tag_count,
        'instagram_feeds' : instagram_feeds,
        'hotel' : hotel,
        'int_inclusion_count' : int_inclusion_count,
        'int_tag_count' : int_tag_count,
        'most_recent' : most_recent,
    }

    return render(request, 'hotel-detail.html', context)