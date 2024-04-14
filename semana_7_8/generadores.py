# Secuencia Fibonacci 
def fib(): 
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a+b
        
for f in fib():
    if f > 50:
        break
    
    print(f)
