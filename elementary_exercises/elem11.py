

total = 0

for k in range(1, 10**6):
    total += ((-1)**(k+1))/(2 * k-1)  
print(4*total)