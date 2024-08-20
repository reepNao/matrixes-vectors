from matrix import Matrix, Vector



        
print("Test 1 - int:")
print(Matrix.lerp(0, 10, 0.5))  # Beklenen çıktı: 5.0

print("Test 2 - float:")
print(Matrix.lerp(1.0, 4.0, 0.25))  # Beklenen çıktı: 1.75

print("Test 3 - complex:")
print(Matrix.lerp(1+1j, 2+2j, 0.5))  # Beklenen çıktı: (1.5+1.5j)

print("Test 4 - Vector:")
e1 = Vector([1., 2., 3.])
e2 = Vector([4., 5., 6.])
print(Vector.lerp(e1, e2, 0.5))  # Beklenen çıktı: Vector([[2.5, 3.5, 4.5]])

print("Test 5 - Matrix:")
m1 = Matrix([[1., 2.], [3., 4.]])
m2 = Matrix([[5., 6.], [7., 8.]])
print(Matrix.lerp(m1, m2, 0.5))  # Beklenen çıktı: Matrix([[3.0, 4.0], [5.0, 6.0]])

print("Test 6 - t = 0:")
print(Matrix.lerp(5, 15, 0.4))  # Beklenen çıktı: 9.0

print("Test 7 - t = 1.0:")
print(Matrix.lerp(5, 15, 1))  # Beklenen çıktı: 15.0

print("Test 8 - t  = 1.1:")
print(Matrix.lerp(5, 15, 1.1))  # Beklenen çıktı: ValueError
