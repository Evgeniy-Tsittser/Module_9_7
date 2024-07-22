import math


def is_prime(func):
    def wrapper(*args):
        summ_ = func(*args)
        for i in range(2, int(summ_+1)//2):
            if summ_ % 2 == 0 and summ_ != i and summ_ % i != 0:
                res = 'Составное число!'
            else:
                res = 'Простое число!'
        return res
    return wrapper


@is_prime
def sum_three(*args):
    print(sum(args))
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

