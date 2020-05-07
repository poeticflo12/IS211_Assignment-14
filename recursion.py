
def fibonacci(number):
  if number <= 1:
    return number
  else:
    return fibonacci(number-1) + fibonacci(number-2)

def main():
    number=int(input("Enter integer number: "))
    print("The nth element of the Fibonnaci sequence is : {}".format(fibonacci(number)))

if __name__ == "__main__":
    main()