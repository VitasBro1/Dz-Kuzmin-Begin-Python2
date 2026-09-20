X = float(input("Введите число X: "))
N = int(input("Введите число N: "))


m = 1.0  
fact = 1.0  
fact_2 = 1.0  

for c in range(1, N + 1):
    fact *= c  
    fact_2 *= X    
    m += fact_2 / fact  


print(X , "=" , m)
