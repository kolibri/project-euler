sum = 0
for number in range(0, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum = sum + number

print(sum)
