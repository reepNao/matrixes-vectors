from matrix import Matrix, Vector

u = Vector([[0.], [0.]])
v = Vector([[1.], [1.]])
print(u.dot(v)) # Expected: 0.0

u = Vector([[1.], [1.]])
v = Vector([[1.], [1.]])
print(u.dot(v)) # Expected: 2.0

u = Vector([[-1.], [6.]])
v = Vector([[3.], [2.]])
print(u.dot(v)) # Expected: 9.0

u = Vector([[8.], [3.]])
v = Vector([[0.], [4.]])
print(u.dot(v)) # Expected: 12.0

u = Vector([[1.], [9.]])
v = Vector([[2.], [3.]])
print(u.dot(v)) # Expected: 29.0