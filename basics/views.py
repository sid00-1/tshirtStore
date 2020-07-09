from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TestM, ContactM
from core.models import Item
from django.views.generic import ListView
from .forms import ProductForm
# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
# imports
from core.models import Item, OrderItem, Order, Address, Coupon, Refund, UserProfile, Payment
from .models import TestM, Review
import random
from random import randint
import string
from django.http.response import HttpResponse


def about_view(request):
    return render(request, 'basics/about.html', {})

# def review(request):
#     context = {
#         'reviews' :
#     }
#     return context


def contact_view(request):
    try:
        # form = ContactForm(request.POST or None)
        # req = None
        # context = {
        #     'form': form
        # }
        if request.method == 'POST':
            # if form.is_valid():
            #     print(form.cleaned_data)
            #     req = form.cleaned_data
            print(request.POST)
            req = request.POST
            contact_info = ContactM()
            contact_info.message = req.get('review')
            contact_info.name = req.get('name')
            contact_info.email = req.get('email')
            contact_info.save()
            print(contact_info)
            print('contact info received successfully!')
            messages.info(request, 'info sent successfully! thank you!')
    except Exception:
        print('something went wrong!')
    return render(request, 'basics/contact.html', {})


def teston_view(request):
    context = {
        'test_list': TestM.objects.all()
    }
    try:

        if request.method == 'POST':
            print(request.POST)
            req = request.POST
            test_info = TestM()
            test_info.message = req.get('review')
            test_info.name = req.get('name')
            test_info.email = req.get('email')
            test_info.save()
            print(test_info)
            print('contact info received successfully!')
            messages.info(request, 'info sent successfully! thank you!')

    except Exception:
        print('something went wrong!')
    return render(request, 'basics/teston.html', context)


class SearchProductView(ListView):
    template_name = "basics/search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(
            *args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)  # method_dict['q']
        if query is not None:
            return Item.objects.search(query)
        return Item.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''


@login_required
def customize_view(request, slug):
    try:
        item = get_object_or_404(Item, slug=slug)
        if request.method == 'POST':
            req = request.POST
            print(req)
            item.size = req.get('size')
            item.custom_design = req.get('custom_design')
            item.color = req.get('color')
            item.print_text = req.get('print_text')
            item.instruction = req.get('instruction')
            item.textcolor = req.get('fgcolor')
            item.shape = req.get('shape')
            item.bgcolor = req.get('bgcolor')
            item.save()
            print(item)
            messages.info(
                request, "your customizations are added to the product .")
            return redirect("core:product", slug=slug)

    except Exception:
        messages.info(
            request, "your customizations were not added to the product .")
        return redirect("basics:customize", slug=slug)
    finally:
        context = {
            'item': item
        }
    return render(request, 'basics/custom.html', context)


def create_view(request, *args, **kwargs):
    if request.method == 'POST':
        req = request.POST
        print(req)
        sluggy = f'custom-shirt-{int(random.randint(1,100))}'
        shirt = Item(
            title=sluggy,
            price=500,
            discount_price=475,
            category='outwear',
            label='primary',
            slug=sluggy,
            description='custom T-shirt',
            image='shirt.jpeg',
            featured=False,
            active=True,
            iscustom=True,
            custom_design=req.get('custom_design'),
            print_text=req.get('print_text'),
            size=req.get('size'),
            color=req.get('color'),
            instruction=req.get('instruction'),
            textcolor=req.get('fgcolor'),
            shape=req.get('shape'),
            bgcolor=req.get('bgcolor')
        )
        print(shirt)
        shirt.save()
        messages.info(
            request, "your customizations are added to the product .")
        return redirect("core:product", slug=shirt.slug)

    context = {}
    return render(request, 'basics/create.html', context)


def dashboard_view(request, *args, **kwargs):

    context = {}
    return render(request, 'basics/dashboard.html', context)
