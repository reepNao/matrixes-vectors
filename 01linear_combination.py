from matrix import Matrix, Vector

e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])

v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])

result1 = Vector.linear_combination([e1, e2, e3], [2, 3, 4])
print(result1)  # Expected output: Vector([[2.0], [3.0], [4.0]])

result4 = Vector.linear_combination([e1, e2, e3], [10, -2, 0.5])
print(result4)  # Expected output: Vector([[10.0], [-2.0], [0.5]])

result5 = Vector.linear_combination([v1, v2], [10, -2])
print(result5)  # Expected output: Vector([[10.0], [0.0], [230.0]])