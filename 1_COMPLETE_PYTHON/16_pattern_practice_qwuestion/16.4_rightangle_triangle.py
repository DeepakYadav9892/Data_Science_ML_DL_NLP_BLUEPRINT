def generate_triangle(n):
    triangle = []
    for i in range(1, n + 1):
        triangle.append('*' * i)
    return triangle

triangle=generate_triangle(4)
print(triangle)