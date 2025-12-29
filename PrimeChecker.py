def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
try:
    num = float(input("Enter the number to check:  "))

    if not num.is_integer():
        print("Decimal number cannot be prime.")

    else:
        print( is_prime(int(num)))

except ValueError:
    print("The entered number is invalid.")