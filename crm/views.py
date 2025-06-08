from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Client, Deal
from .forms import ClientForm, DealForm


def client_list(request):
    clients = Client.objects.all()  # Убрали фильтр по created_by
    return render(request, 'crm/client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:client_list')
    else:
        form = ClientForm()
    return render(request, 'crm/client_form.html', {'form': form})


def client_deals(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    deals = Deal.objects.filter(client=client)  # Убрали фильтр по created_by

    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        deals = deals.filter(status=status_filter)

    paginator = Paginator(deals, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'crm/client_deals.html', {
        'client': client,
        'page_obj': page_obj,
        'status_filter': status_filter,
        'status_choices': Deal.STATUS_CHOICES
    })


def deal_create(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.client = client
            deal.save()
            return redirect('crm:client_deals', client_id=client.id)
    else:
        form = DealForm()
    return render(request, 'crm/deal_form.html', {'form': form, 'client': client})


def deal_edit(request, pk):
    deal = get_object_or_404(Deal, id=pk)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('crm:client_deals', client_id=deal.client.id)
    else:
        form = DealForm(instance=deal)
    return render(request, 'crm/deal_form.html', {'form': form, 'deal': deal})


def deal_delete(request, pk):
    deal = get_object_or_404(Deal, id=pk)
    client_id = deal.client.id
    deal.delete()
    return redirect('crm:client_deals', client_id=client_id)


def client_delete(request, pk):
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect('crm:client_list')