from matrix import Matrix, Vector


u = Vector([[8.], [3.]])
v = Vector([[0.], [4.]])
print(u.dot(v)) # Expected: 12.0

u = Vector([[1.], [9.]])
v = Vector([[2.], [3.]])
print(u.dot(v)) # Expected: 29.0