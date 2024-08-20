from matrix import Matrix, Vector

# Test
v = Vector([[1.], [0.]])
u = Vector([[1.], [0.]])
print(Vector.angle_cos(u, v))  # Expected: 1.0

v = Vector([[1.], [0.]])
u = Vector([[0.], [1.]])
print(Vector.angle_cos(u, v))  # Expected: 0.0

v = Vector([[-1.], [1.]])
u = Vector([[1.], [-1.]])
print(Vector.angle_cos(u, v))  # Expected: -1.0

v = Vector([[2.], [1.]])
u = Vector([[4.], [2.]])
print(Vector.angle_cos(u, v))  # Expected: 1.0

v = Vector([[1.], [2.], [3.]])
u = Vector([[4.], [5.], [6.]])
print(Vector.angle_cos(u, v))  # Expected: 0.9746318461970762