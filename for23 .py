X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))


m = 0.0
num_1 = X 
fact = 1      
num_2 = X         


for c in range(N + 1):
    if c > 0:
        
        num_2 *= X * X
        
        fact *= 2 * c * (2 * c + 1)
        
        num_1 = num_2 / fact
        if c % 2 == 1:  
            num_1 = -num_1
    m += num_1

print(X , "+-" , m) 
