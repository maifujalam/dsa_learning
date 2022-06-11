from decorators.logger import loger

@loger
def add(a, b):
    return a + b


@loger
def subtract(a, b):
    return a - b


@loger
def multiply(a, b):
    return a * b


@loger
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot be divided by zero")
    return a // b


if __name__ == '__main__':
    print(add(1, 2))
    print(multiply(3, 2))
    print(subtract(1, 2))
    print(divide(10, 3))
