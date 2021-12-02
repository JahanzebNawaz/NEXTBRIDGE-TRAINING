# “Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
# instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (str(i))
        
   
# ----------------------------------------------------------------------
#  reverse a string 

def reverse(word):
  return word[::-1]

# other way 
def reverse(n):
    if len(n) ==0:
        return n
    print(n[1:] + n[0])
    return n[1:] + n[0]
    
print(reverse(name))

# ----------------------------------------------------------------------
# sort a list of number including negative numbers 

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(new_list)
# ----------------------------------------------------------------------

# write a logic to get even numebrs  and odd numbers

for x in range(20):
    if x%2 != 0:
        # odd number
        print(x)
    if x%2 == 0:
        # even number
        print(x)
        
# ----------------------------------------------------------------------
# write a function to generate fabnocci series
# 0,1,1,2,3,5,8,13

def fib(n):
    a, b = 0, 1
    while a <= n:
        print(a)
        a, b = b, a+b
fib(5)


# ----------------------------------------------------------------------






