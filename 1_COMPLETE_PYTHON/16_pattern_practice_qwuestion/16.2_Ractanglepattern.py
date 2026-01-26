def generate_rectangle(n, m):
    rectangle = []
    for i in range(n):
        rectangle.append('*' * m)
    return rectangle

result=generate_rectangle(4,5)
print(result)