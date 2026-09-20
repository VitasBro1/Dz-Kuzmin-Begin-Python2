N = int(input("Введите число N: "))


fact = 1.0  
m = 1.0  

for i in range(1, N + 1):
    m *= i  
    fact += 1 / m  


print(N , "=" , fact)
print(fact)
