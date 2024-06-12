def fibo(n):
    match n:
        case 1:
            return 0
        case 2:
            return 1
        case 3:
            return 0+1 #es lo mismo que fibo(2)+fibo(1) o fibo(n-1)+fibo(n-2)
        case 4:
            return fibo(2)+fibo(3)
        

def fibo_simplif(n):
    match n:
        case 1:
            return 0
        case 2:
            return 1
    return fibo_simplif(n-2)+fibo_simplif(n-1)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

def alternativofactorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n*alternativofactorial(n-1)

print(fibo_simplif(5))
print(alternativofactorial(3))