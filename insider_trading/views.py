from django.db import connection
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from .models import InsiderTrading

def display_data(request):
    search_query = request.GET.get('search', '')
    if search_query:
        data = InsiderTrading.objects.filter(
            Q(ticker__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(insider_name__icontains=search_query) |
            Q(title__icontains=search_query) |
            Q(trade_type__icontains=search_query) |
            Q(form4_url__icontains=search_query)
        )
    else:
        data = InsiderTrading.objects.all()
    page_number = request.GET.get('page', 1)
    items_per_page = 100
    paginator = Paginator(data, items_per_page)
    try:
        current_page_data = paginator.page(page_number)
    except EmptyPage:
        # If the page is out of range, return the last page's data
        current_page_data = paginator.page(paginator.num_pages)
    context = {
        'data': current_page_data,
        'search_query': search_query,
    }
    return render(request, 'home.html', context)
