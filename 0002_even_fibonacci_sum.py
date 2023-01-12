previous, fib_number = 0, 1
even_sum = 0
while fib_number < 4000000:
    previous, fib_number = fib_number, previous + fib_number
    if 0 == fib_number % 2:
        even_sum = even_sum + fib_number

print(even_sum)
