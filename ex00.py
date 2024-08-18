from matrix import Matrix, Vector

u = Matrix([[2., 0.],[6., 0.]])
v = Matrix([[3., 8.],[5., 7.]])

print("Matrix addition, subtraction and scalar multiplication")
result = u.add(v)
print(result)  # Matrix([[5.0, 8.0], [11.0, 7.0]])

result_sub = u.sub(v)
print(result_sub)  # Matrix([[-1.0, -8.0], [1.0, -7.0]])

result_scl = u.scl(2)
print(result_scl)  # Matrix([[4.0, 0.0], [12.0, 0.0]])

#####################################
#                                   #
#		      4 Vectors             #
#                                   #
#####################################

u1 = Vector([1., 2., 3.])
v1 = Vector([4., 15., 6.])

print(" ")
print("Vector addition, subtraction and scalar multiplication")
result1 = u1.add(v1)
print(result1)  # Vector([[5.0, 17.0, 9.0]])

result1_sub = u1.sub(v1)
print(result1_sub)  # Vector([[-3.0, -13.0, -3.0]])

result1_scl = u1.scl(3)
print(result1_scl)  # Vector([[3.0, 6.0, 9.0]])
