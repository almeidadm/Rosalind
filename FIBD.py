def fib(months, mortality):
  F = [0 for i in range(months)]
  F[0] = 1
  F[1] = 1
  for i in range(2, months):
    if i < mortality:
      F[i] = F[i-1]+F[i-2]
    elif i == mortality:
      F[i] = F[i-1]+F[i-2] - 1
    else:
      F[i] = F[i-1]+F[i-2]-F[i-mortality-1]
  return F[-1]

def main():
  file_name ='MortalFibonacciRabbits.txt'
  file = open(file_name, 'r')
  file = file.read()
  file = file.split(' ')
  print(fib(int(file[0]), int(file[1])))

if __name__ == '__main__':
  main()
