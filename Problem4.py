def balance(openingSum, interestRate, taxFreeLimit, taxRate, numMonths):
    """
    param openingSum: initial account balance
    param interestRate: percent of the monthly interest
    param taxFreeLimit: balance limit for taxation
    param taxRate: percent of the monthly tax
    param numMonths: how many months to calculate savings
    """
    balance = openingSum

    for x in range(0, numMonths):
        interest = balance * (interestRate / 100)

        if balance > taxFreeLimit:
            tax = (balance - taxFreeLimit) * (taxRate / 100)
        else:
            tax = 0

        balance += interest - tax

    return balance
