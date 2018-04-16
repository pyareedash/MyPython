k = input('Enter a number : ')
l = int(k)

print(l)

a = 1

for x in range(0,l):
    a = a * (l - x)
    
print ('{}! = {}'. format(k,a))
