import math

number = 73939133

i = 2
is_prime = True

while i < math.sqrt(number):
    if number % i == 0:
        is_prime = False
        break

    i = i + 1


print(number, is_prime, i)


