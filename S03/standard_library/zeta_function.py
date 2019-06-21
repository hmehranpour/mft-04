import math
import time


out = 0
i = 1
epsilon = 10e-8

t1 = time.time()
while True:
    out = out + 1/i**2
    pi_computed = math.sqrt(out*6)
    err = abs(pi_computed - math.pi)/math.pi
    if err < epsilon:
        break
    i += 1

t2 = time.time()
print("Elapsed time = ", (t2-t1)*1000, " (ms)")
print(pi_computed)
print(math.pi)
print("iterations = ", i)
