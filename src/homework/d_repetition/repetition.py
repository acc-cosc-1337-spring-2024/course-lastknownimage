def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return  factorial
def sum_odd_numbers(num):
    result = 0
    for i in range(1, num +1, 2):
        result += i
    return result