def sum_of_digit(n):
    sum = 0
    while n != 0:
        last=n%10
        sum+=last
        n //=10
    return sum
if __name__ =="__main__":
    n=int(input())
    print(f"Sum of Digit is {sum_of_digit(n)}")
# Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
# Space Complexity: O(1) because we are using a constant amount of space to store the sum and the last digit.

#string Approach
def sum_of_digit(n):
    sum = 0
    for i in str(n):
        sum+=int(i)
    return sum
if __name__ =="__main__":
    n=int(input())
    print(f"Sum of Digit is {sum_of_digit(n)}")
# Time Complexity: O(d) where d is the number of digits in the input number, because we are iterating through each digit of the number.
# Space Complexity: O(1) because we are using a constant amount of space to store the sum.