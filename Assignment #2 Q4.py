name = input("Enter your name: ")
weight = input("Enter your weight(in Kg): ")

mercury = float(weight) * float(0.38)
venus = float(weight) * float(0.91)
earth = float(weight) * float(1)
mars = float(weight) * float(0.38)
jupiter = float(weight) * float(2.6)
saturn = float(weight) * float(1.1)
uranus = float(weight) * float(0.90)
neptune = float(weight) * float(1.1)
pluto = float(weight) * float(0.07)

output = f"""
{name}, your weight on: 
Earth is {earth} Kg
Mercury will be {mercury} Kg
Venus will be {venus} Kg
Mars will be {mars} Kg
Jupiter will be {jupiter} Kg
Saturn will be {saturn} Kg
Uranus will be {uranus} Kg
Neptune will be {neptune} Kg
Pluto will be {pluto} Kg
"""
print(output)

