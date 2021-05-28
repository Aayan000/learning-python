hour = input("Enter however many hours: ")
minutes = input("Enter however many minutes: ")

hour_sec = int(hour)* int(60) * int(60)
minute_sec = int(minutes) * int(60)

combiened = int(hour_sec) + int(minute_sec)

print(hour,"hours and",minutes,"minutes is",combiened,"seconds")

