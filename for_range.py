sum = 0
for x in range (0,101,2):    
    sum += x
    if x % 2 == 1:
        continue
    print(x)
print("1부터 100까지의 짝수의 합:",sum)