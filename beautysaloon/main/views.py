from django.shortcuts import render
from .models import Visits
from .forms import VisitsForm, PriceFilterForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VisitsSerializer

# Create your views here.


class VisitsView(APIView):
    def get(self, request):
        products = Visits.objects.all()
        serializer = VisitsSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request):
        products = request.data.get('product')
        serializer = VisitsSerializer(data=products)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})



def index(request):
    error = ''
    if request.method == 'POST':
        form = VisitsForm(request.POST)
        if form.is_valid():
            form.save()

    visits = Visits.objects.all()
    formsort = PriceFilterForm(request.GET)

    if formsort.is_valid():
        if formsort.cleaned_data['price_min']:
            visits = visits.filter(price__gte=formsort.cleaned_data['price_min'])

        if formsort.cleaned_data['price_max']:
            visits = visits.filter(price__lte=formsort.cleaned_data['price_max'])

    form = VisitsForm()
    context = {
        'visits': visits,
        'formsort': formsort,
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context)
