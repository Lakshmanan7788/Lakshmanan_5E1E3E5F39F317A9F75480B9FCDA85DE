#find a factorial of given number
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)
num =int(input("Enter tha number:"))
r = factorial(num)
print("factorial of",num, "s",r)