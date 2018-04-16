n = int(input('Enter a number: '))
net = []

for x in range(2,n):
    if n % x ==0:
        net.append('N')
    net.append('Y')

if 'N' not in net:
    print('The number is a prime')
else:
    print('The number is NOT a prime')
    

