import math

file = open("rosalind_pper.txt").read().split(' ')
n = int(file[0])
k = int(file[1])
print(n, k)

sol = math.factorial(n)/math.factorial(n-k)
print(sol%1000000)
