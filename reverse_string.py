def reverse(a):
  str = ''
  if len(a) == 0:
    return a
  else:
    return reverse(a[1:]) + a[0]
  
print(reverse('Hello world'))

