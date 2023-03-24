from django.shortcuts import render
import pandas as pd
from .models import Consumer
from .serializers import ConsumerSerializer
from .forms import UploadFileForm, ConsumerForm, RulesForm
import ipdb
from django import http

# Create your views here.
# Todo: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            serializer = ConsumerSerializer(data=form.cleaned_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            list = Consumer.objects.all()

        return render(request, "register.html", {"list": list})

    if request.method == "GET":
        form = ConsumerForm()
        form_2 = RulesForm()
        list = Consumer.objects.all()
        return render(request, "register.html", {"form": form, "form_2": form_2, "list": list})


def upload(request):
    if request.method == "GET":
        form = UploadFileForm()

        return render(request, "upload.html", {"form": form})

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_data = pd.read_excel(file)

        consumer_list = [
            {   
                # "pk": index,
                "name": row["Nome"],
                "document": row["Documento"],
                "city": row["Cidade"],
                "state": row["Estado"],
                "consumption": row["Consumo(kWh)"],
                "coverage": row["Cobertura(%)"],
                "consumer_type": row["Tipo"],
                "distributor_tax": row["Tarifa da Distribuidora"],
            }
            for index, row in file_data.iterrows()
        ]

        Consumer.objects.bulk_create([Consumer(**data) for data in consumer_list])

        list = Consumer.objects.all()

        for consumer in list:
           serializer = ConsumerSerializer(data=form.cleaned_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return render(request, "upload_success.html", {"list": list})


# Todo: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass
