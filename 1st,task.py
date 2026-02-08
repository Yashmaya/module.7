seasons = ("winter", "spring", "summer", "autumn")

month_number = int(input("enter numbers of months (1-12):"))

if month_number in (12,1,2):
   print(f"month number {month_number} comes in {seasons[0]}")
elif month_number in (3,4,5):
     print(f"month number {month_number} comes in {seasons[1]}")
elif month_number in (6,7,8):
     print(f"month number {month_number} comes in {seasons[2]}")
elif month_number in (9,10,11):
     print(f"month number{month_number} comes in {seasons[3]}")

else:
     print("invalid input")