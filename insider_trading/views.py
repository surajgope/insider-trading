from django.shortcuts import render
from django.db import connection
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from .models import InsiderTrading

# def display_data(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM insider_trading order by time desc;")
#         rows = cursor.fetchall()
#         # Get column names from cursor description
#         columns = [col[0] for col in cursor.description]

#     # Create a list of dictionaries containing the results
#     data = [dict(zip(columns, row)) for row in rows]
#     print(type(data), len(data), data[0])
#     page_number = request.GET.get('page', 1)
#     items_per_page = 100
#     paginator = Paginator(data, items_per_page)
#     try:
#         current_page_data = paginator.page(page_number)
#     except EmptyPage:
#         # If the page is out of range, return the last page's data
#         current_page_data = paginator.page(paginator.num_pages)
#     print(f'current_page_data: {current_page_data}, dir(current_page_data = {dir(current_page_data)}')
#     return render(request, 'home.html', {'data': current_page_data})


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

    context = {
        'data': data,
        'search_query': search_query,
    }
    return render(request, 'home.html', context)
