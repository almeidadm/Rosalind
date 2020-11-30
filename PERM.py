import math

def permute(list, l, r):
  if l==r:
    for i in list:
      print(i, end = ' ')
    print()
  else:
    for i in range(l, r+1):
      list[l], list[i] = list[i], list[l]
      permute(list, l+1, r)
      list[l], list[i] = list[i], list[l]

def main():
  file = open('EnumeratingGeneOrders.txt', 'r')
  file = file.read()
  n = int(file[0])
  list = [i+1 for i in range(n)]
  print(math.factorial(n))
  permute(list, 0, n-1)

if __name__ == '__main__':
  main()
