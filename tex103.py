def calculate(income):
    table_tax = [(      0, 0.00,  150000), ( 150001, 0.05,       300000),
                 ( 300001, 0.10,  500000), ( 500001, 0.15,       750000),
                 ( 750001, 0.20, 1000000), (1000001, 0.25,      2000000),
                 (2000001, 0.30, 5000000), (5000001, 0.35, float("inf"))]
    progressive_tax = [(f"{low:,} - {high:,} rate {rate*100:,}% tax", ((min(income, high) - (low-1)) * rate))
                       for low, rate, high in table_tax if income >= low]
    
    return progressive_tax

income = float(input("put income : "))
progressive_tax = calculate(income)

tax_total = sum(tax for _, tax in progressive_tax)
print("\n" .join(f"{label} = {tax:,.2f}" for label, tax in progressive_tax if tax >= 0))
print()
print(f"income = {income:,.0f}")
print(f"sum tax = {tax_total:,.2f}")
print(f"Net income {income:,.0f} - {tax_total:,.2f} = {income - tax_total:,.2f}")
print(f"Effective Tax Rate : {tax_total / income * 100:,.2f}%")
print()