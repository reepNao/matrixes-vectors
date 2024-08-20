from matrix import Matrix, Vector

print("Test 1:")
print(Matrix.lerp(0., 1., 0.))  # Expected output: 0.0

print("Test 2:")
print(Matrix.lerp(0., 1., 1.))  # Expected output: 1.0

print("Test 3 - complex:")
print(Matrix.lerp(1+1j, 2+2j, 0.5))  # Expected output: (1.5+1.5j)

print("Test 4 - Vector:")
e1 = Vector([2., 1.])
e2 = Vector([4., 2.])
print(Vector.lerp(e1, e2, 0.3))  # Expected output: Vector([[2.6], [1.3]])

print("Test 5 - Matrix:")
m1 = Matrix([[2., 1.], [3., 4.]])
m2 = Matrix([[20., 10.], [30., 40.]])
print(Matrix.lerp(m1, m2, 0.5))  # Expected output: Matrix([[11., 5.5], [16.5, 22.]])
