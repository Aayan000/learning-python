principal = float(input("Enter a principal amount: "))
time  = float(input("Enter a time amount(ine years): "))

five = principal * (1 + 0.05/1)**(1 * time)
seven = principal * (1 + 0.075/1)**(1 * time)
ten = principal * (1 + 0.1/1)**(1 * time)

output = f"""
At a interest of 5%, you wil have {five} in total.
At a interest of 7.5%, you will have {seven} in total.
At a interest of 10%, you will have {ten} in total.
"""
print(output)