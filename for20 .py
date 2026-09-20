N = int(input("Введите число N: "))
m = 0.0
fact = 1.0  

for c in range(1, N + 1):
    fact *= c  
    m += fact 

print(N , m)
