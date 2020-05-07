

def gcd(a, b):
    if b == 0:
        return a
    else:
        r= a % b
        return gcd(b, r)

def main():
    a=int(input("Enter the first integer: "))
    b=int(input("Enter the second integer: "))
    print("The GCD is {} ".format(gcd(a,b)))

if __name__ == "__main__":
    main()