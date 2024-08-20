from matrix import Matrix, Vector

u = Matrix([[1., 2.],[3., 4.]])
v = Matrix([[7., 4.],[-2., 2.]])

print("Matrix addition, subtraction and scalar multiplication")
result = u.add(v)
print(result) # Matrix([[8.0, 6.0], [1.0, 6.0]])

result_sub = u.sub(v)
print(result_sub)  # Matrix([[-6.0, -2.0], [5.0, 2.0]])

result_scl = u.scl(2)
print(result_scl)  # Matrix([[2.0, 4.0], [6.0, 8.0]])


u1 = Vector([2., 3.])
v1 = Vector([5., 7.])

u3 = Vector([2., 3.])

print(" ")
print("Vector addition, subtraction and scalar multiplication")
result1 = u1.add(v1)
print(result1)  # Vector([7.0, 10.0])

result1_sub = u1.sub(v1)
print(result1_sub)  # Vector([-3.0, -4.0])

result1_scl = u3.scl(2)
print(result1_scl)  # Vector([4.0, 6.0])
