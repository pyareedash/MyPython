k = input('Enter numbers (first and second) : ')
numbers = list(map(int, k.split()))
    
print(numbers)

n = input('Enter no. of iterations : ')

m = int(n)

for i in range(0,m):
    c = numbers[i] + numbers[i+1]
    numbers.append(c)

print(numbers)