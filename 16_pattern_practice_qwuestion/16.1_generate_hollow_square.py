def generate_hollow_square(n):
    square = []

    if n == 1:
        return ['*']

    square.append('*' * n)

    for i in range(n - 2):
        square.append('*' + ' ' * (n - 2) + '*')

    square.append('*' * n)

    return square



result=generate_hollow_square(5)
print(result)
