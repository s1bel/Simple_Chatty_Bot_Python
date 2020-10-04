number1 = int(input())
number2 = int(input())


def min_max(num1, num2):
    if num1 > num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)


min_max(number1, number2)
