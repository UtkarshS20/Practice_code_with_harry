#recursion- using function inside function
#n! = n * n-1 * n-2.....1
#n! = n * (n-1)!
def factorial_iterative(n):
    """
    :param n: integer
    :return: n * n-1 * n-2.....1
    """
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
number=int(input())
print(factorial_iterative(number))

def factorial_recursive(n):
    """
    :param n: integer
    :return: n * n-1 * n-2.....1
    """
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(number))

def fibbonaci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)

print(fibbonaci(number))