def multiplication(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    multiplication(n)

#Using Recursion

def multiplication(n, i=1):
    if i==11:
        return
    print(f"{n} x {i} = {n*i}")
    multiplication(n, i+1)
if __name__ == "__main__":    
    n=int(input("Enter a number: "))
    multiplication(n)