def digit_sum(n):
    num = list(str(n))
    num = [int(i) for i in num]
    return sum(num)

print digit_sum(123)


