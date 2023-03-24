from django.db import models

# Create your models here.

RESIDENTIAL = "Residencial"
COMMERCIAL = "Comercial"
INDUSTRIAL = "Industrial"


class ConsumerTypeChoices(models.TextChoices):
    RESIDENTIAL = ("Residencial",)
    COMMERCIAL = ("Comercial",)
    INDUSTRIAL = ("Industrial",)


class ConsumptionRangeChoices(models.TextChoices):
    Range_1 = "< 10.000 kWh"
    Range_2 = ">= 10.000 kWh e <= 20.000 kWh"
    Range_3 = "> 20.000 kWh"


class CoverValueChoices(models.TextChoices):
    Cover_1 = 0.90
    Cover_2 = 0.95
    Cover_3 = 0.99


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    coverage = models.IntegerField(null=True)
    consumer_type = models.CharField(
        max_length=50, choices=ConsumerTypeChoices.choices, null=True
    )
    #  create the foreign key for discount rule model here
    discount_rule = models.ForeignKey(
        "core.DiscountRules",
        on_delete=models.CASCADE,
        related_name="consumers",
        null=True,
    )


class DiscountRules(models.Model):
    RESIDENTIAL = "Residencial"
    COMMERCIAL = "Comercial"
    INDUSTRIAL = "Industrial"
    ConsumerTypeChoices = (
        (RESIDENTIAL, "Residencial"),
        (COMMERCIAL, "Comercial"),
        (INDUSTRIAL, "Industrial"),
    )

    tax_type = models.CharField(choices=ConsumerTypeChoices, max_length=20)
    min_consumption = models.IntegerField()
    max_consumption = models.IntegerField()
    discount = models.FloatField()
    coverage = models.FloatField()


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
