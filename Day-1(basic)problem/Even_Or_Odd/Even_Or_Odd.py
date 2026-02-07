# Naive mode: O(1) time, O(1) space
def even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    if even_or_odd(n):
        print(f"{n} is even.") 
    else:
        print(f"{n} is odd.")

# Expect using bitwise operator: O(1) time, O(1) space
"""
In binary representation, even numbers always end with 0 and odd numbers always end with 1
which means the even number will be 0 and odd number will be 1 when we perform bitwise AND operation with 1."""
def even_or_odd_bitwise(number):
    if number & 1 == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    if even_or_odd_bitwise(n):
        print(f"{n} is even.") 
    else:
        print(f"{n} is odd.")