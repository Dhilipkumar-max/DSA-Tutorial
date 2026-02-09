def isPower(x, y):
    if x == 1:
        return y == 1

    pow = 1
    while pow < y:
        pow *= x

    return pow == y

if __name__ == '__main__':
    print(isPower(10, 1))
    print(isPower(1, 20))
    print(isPower(2, 128))
    print(isPower(2, 30))