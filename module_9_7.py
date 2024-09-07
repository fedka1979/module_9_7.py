def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f'Составное \n{result}'
        return f'Простое \n{result}'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result_ = sum_three(2, 3, 6)
print(result_)