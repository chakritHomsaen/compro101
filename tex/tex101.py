def calculate(income):
    tex =0
    print(f"0-150,000 you pay tex : {tex}")
    
    if income >= 150001:
        texin = (income - 150000) * 0.05
        tex = texin
        
        if income > 300000:
            texin = 7500
            
        print(f"150,001-300,000 you pay tex : {texin}")
    
    if income >= 300001:
        texin = (income - 300000) * 0.1
        tex = 7500 + texin
        
        if income > 500000:
            texin = 20000
            
        print(f"300,001-500,000 you pay tex : {texin}")
    
    if income >= 500001:
        texin = (income - 500000) * 0.15
        tex = 7500+ 20000 + texin
        
        if income > 750000:
            texin = 37500
            
        print(f"500,001-750,000 you pay tex : {texin}")

    if income >= 750001:
        texin = (income - 750000) * 0.2
        tex = 7500+ 20000 + 37500 + texin
        
        if income > 750000:
            texin = 50000
            
        print(f"150,001-300,000 you pay tex : {texin}")

    if income >= 1000001:
        texin = (income - 1000000) * 0.25
        tex = 7500+ 20000 + 37500 + 50000 + texin
        
        if income > 2000000:
            texin = 250000
            
        print(f"1,000,001-2,000,000 you pay tex : {texin}")

    if income >= 2000001:
        texin = (income - 2000000) * 0.30
        tex = 7500+ 20000 + 37500 + 50000 + 250000 + texin
        
        if income > 5000000:
            texin = 900000
            
        print(f"2,000,001-5,000,000 you pay tex : {texin}")

    if income >= 5000001:
        texin = (income - 5000000) * 0.35
        tex = 7500+ 20000 + 37500 + 50000 + 250000 + 900000 + texin
        
        print(f"5,000,001 to more you pay tex : {texin}")
    
    return tex
 
    
income = int(input("input your income :"))

tex = calculate(income)
net_income = income - tex
effective = tex / income * 100

print(f"Sum tex : {tex}")
print(f"Net income : {net_income}")
print(f"Effective Tax Rate : {effective:.2f}")