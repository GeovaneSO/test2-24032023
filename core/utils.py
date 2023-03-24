def calculator(consumer_type: str, distributor_tax: float, tax_type: str) -> tuple:

    counter = 0

    for number in consumption:
        counter += number

    average = float(counter) / len(consumption)

    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    if average < 10000:

        if tax_type == "Residencial":
            applied_discount = 0.18

        if tax_type == "Comercial":
            applied_discount = 0.16

        if tax_type == "Industrial":
            applied_discount = 0.12

        coverage = 0.9

    elif average > 10000 and average <= 20000:

        if tax_type == "Residencial":
            applied_discount = 0.22

        if tax_type == "Comercial":
            applied_discount = 0.18

        if tax_type == "Industrial":
            applied_discount = 0.15

        coverage = 0.95

    else:

        if tax_type == "Residencial":
            applied_discount = 0.25

        if tax_type == "Comercial":
            applied_discount = 0.22

        if tax_type == "Industrial":
            applied_discount = 0.18

        coverage = 0.99

    monthly_savings = (average * distributor_tax) * applied_discount * coverage

    annual_savings = monthly_savings * 12

    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )