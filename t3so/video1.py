"How to find average of N numbers in Python"

how_many = int(input("How many value? "))

total = 0

for _ in range(how_many):
    number = float(input("Values? "))
    total += number

avg = total / how_many

print(avg)