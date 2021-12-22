# https://www.blog.pythonlibrary.org/2019/09/18/python-code-kata-fizzbuzz/

def fizz_buzz(n):
    THREE, FIVE = "Fizz", "Buzz"

    if n % 3 == 0 and n % 5 == 0:
        return f"{THREE}{FIVE}"
    elif n % 3 == 0:
        return THREE
    elif n % 5 == 0:
        return FIVE
    else:
        return n


for i in range(1, 101):
    print(fizz_buzz(i))