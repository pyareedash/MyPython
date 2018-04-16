m = input('Enter set number :')
n = int(m)

l = input('Enter combination number (less/equal than set) :' )
k = int(l)
a = 1
b = 1
c = 1

for x in range(0,n):
    a = a * (n-x)

for x in range(0,k):
    b = b * (k-x)
    
g = n - k

for x in range(0,g):
    c = c * (g-x)

sum = a/(b * c)

print('{}!/{}!{}! = {}'.format(n,k,g,sum))