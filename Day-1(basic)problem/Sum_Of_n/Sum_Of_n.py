def sum_of_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    print(f"The sum of first {n} numbers is: {sum_of_n(n)}")
    #Time complexity: O(n) and Space complexity: O(1)

#Expecting using formula: O(1) time, O(1) space
def sum_of_n_formula(n):
    return n*(n+1)//2
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    print(f"The sum of first {n} numbers is: {sum_of_n_formula(n)}")