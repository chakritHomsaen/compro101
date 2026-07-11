def calculate(income):
    tex_total = 0
    tex = 0
    table_tex = [(      0, 0.00,  150000), ( 150001, 0.05,  300000),
                 ( 300001, 0.10,  500000), ( 500001, 0.15,  750000),
                 ( 750001, 0.20, 1000000), (1000001, 0.25, 2000000),
                 (2000001, 0.30, 5000000), (5000001, 0.35,    None),]
    
    for min, rate, max in table_tex:
        if max is None or income > max:
            if max is None:
                tex = rate * (income - (min-1))
                print(f"tex {min :,.2f} - {income :,.2f} = {tex :,.2f}")

            else:
                tex = rate * (max - (min-1))
                print(f"tex {min :,.2f} - {max :,.2f} = {tex :,.2f}")

            tex_total += tex
        
        elif income <= max:
            tex = rate * (income - (min-1))
            print(f"tex {min :,.2f} - {income :,.2f} = {tex :,.2f}")
            tex_total += tex
            break

    return tex_total


income = int(input("put income :"))
tex_total = calculate(income)

print()
print(f"Tex total :{tex_total :,.2f}")
print(f"Net income : {income - tex_total :,.2f}")
print(f"Effective Tax Rate : {tex_total / income * 100 :,.2f} %")