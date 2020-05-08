n = int(input())  #get value from user for limit


# method one using while loop
def fibonacci(n):
  a, b = 0, 1
  # print(a)
  while a <= n:
    print(a)
    a, b = b, a+b
  
fibonacci(n)
  
# method two using for loop
def fibonacci_fun(n):
  a, b = 0, 1
  print(a)
  print(b)
  for x in range(2, n):
    a, b = b, a+b
    print(b)

fibonacci_fun(n)


# another way

def fibonacci_fun(n):
  a, b = 0, 1
  for x in range(2, n):
    print('%s' % a)
    a, b = b, a+b
    

fibonacci_fun(n)
