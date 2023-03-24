import ipdb
import pandas as pd
from rest_framework import serializers

from core.models import Consumer


def create():
    file_data = pd.read_excel("test2-24032023/consumers.xlsx")

    consumer_list = [
        {
            "name": row["Nome"],
            "document": row["Documento"],
            "city": row["Cidade"],
            "state": row["Estado"],
            "consumption": row["Consumo(kWh)"],
            "coverage": row["Cobertura(%)"],
            "distributor_tax": row["Tarifa da Distribuidora"],
        }
        for index, row in file_data.iterrows()
    ]

    ipdb.set_trace()

    return Consumer.objects.bulk_create(consumer_list)
