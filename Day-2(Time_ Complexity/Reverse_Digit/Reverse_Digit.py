def Reverse_Digit(n):
    rev=0
    while n>0:
        last=n%10
        rev=rev*10+last
        n //=10
    return rev
if __name__ =="__main__":
    n=int(input())
    print(f"Reverse of Digit is {Reverse_Digit(n)}")
# Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
# Space Complexity: O(1) because we are using a constant amount of space to store the reverse and the last digit.

#string Approach
def Reverse_Digit(n):
    rev=0
    for i in str(n):
        rev=rev*10+int(i)
    return rev
if __name__ =="__main__":
    n=int(input())
    print(f"Reverse of Digit is {Reverse_Digit(n)}")