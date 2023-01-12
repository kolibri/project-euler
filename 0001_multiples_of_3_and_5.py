def is_divisible_by(dividend: int, divisors: [int]) -> bool:
    for divisor in divisors:
        if 0 == dividend % divisor:
            return True

    return False


total_sum = 0
for current_number in range(0, 1000):
    if is_divisible_by(current_number, [3, 5]):
        total_sum = total_sum + current_number

print(total_sum)
