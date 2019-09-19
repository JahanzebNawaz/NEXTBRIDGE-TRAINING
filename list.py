#Even number

even = []
for num in range(1,40):
    if num%2==0:
        even.append(num)
        print(even)

#with list comprehension
print([num for num in range(1,20) if num%2==0 ])

even = []
[even.append(num) for num in range(1,30) if num%2==0]
even


#2d list
lst = [[x for x in range(3)] for y in range(5)]
lst
