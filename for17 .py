A = float(input("Введите чичло A: "))
N = int(input("Введите число N: "))


n= 1.0 
m= 1.0  


for c in range(1, N + 1):
    m *= A  
    n += m  


print(N , n)
