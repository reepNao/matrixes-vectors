from matrix import Matrix, Vector


u = Matrix([[0., 0.],[0., 0.]])
print("transposed:", u.transpose()) # '[[0, 0], [0, 0]]'

u = Matrix([[1., 0.],[0., 1.]])
print("transposed:", u.transpose()) # '[[1, 0], [0, 1]]'

u = Matrix([[1., 2.],[3., 4.]])
print("transposed:", u.transpose()) # '[[1, 3], [2, 4]]'

u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
print("transposed:", u.transpose()) # '[[1, 0, 0], [0, 1, 0], [0, 0, 1]]'

u = Matrix([[1., 5., 9.],[2., 4., 6.],[3., 6., 7.]])
print("transposed:", u.transpose()) # '[[1, 2, 3], [5, 4, 6], [9, 6, 7]]'
