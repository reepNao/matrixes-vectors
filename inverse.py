import numpy as np

class Matrix:
    def __init__(self, data):
        # data düz bir listeyse, onu liste içinde liste formatına dönüştür
        if isinstance(data, list) and all(isinstance(i, (int, float, complex)) for i in data):
            self.data = [[i] for i in data]  # Vektör, dikey bir vektör olarak tanımlanır
            self.shape = (len(data), 1)
            self.size = len(data)
        elif isinstance(data, list):
            # Eğer data liste içinde liste formatındaysa, onu bir matris olarak işle
            if all(isinstance(row, list) and all(isinstance(i, (int, float, complex)) for i in row) for row in data):
                row_lengths = [len(row) for row in data]
                if len(set(row_lengths)) != 1:
                    raise ValueError("All rows must have the same number of elements.")
                self.data = data
                self.shape = (len(data), row_lengths[0])
                self.size = len(data) * row_lengths[0]
            else:
                raise ValueError("Invalid form of list,", data)
        else:
            raise ValueError("Invalid form of data,", data)

    def __repr__(self):
        return f"Matrix({self.data})"
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("You can only add another Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("You can only subtract another Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return Matrix(result)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float, complex)):
            raise TypeError("The scalar multiplier must be a number.")
        result = [[self.data[i][j] * scalar for j in range(self.shape[1])]
                  for i in range(self.shape[0])]
        return Matrix(result)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def determinant(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix must be square for determinant.")
        if self.shape == (2, 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        n = self.shape[0]
        matrix_copy = [row.copy() for row in self.data]
        det = 1.0
        
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if matrix_copy[k][i] != 0:
                    if i != k:
                        matrix_copy[i], matrix_copy[k] = matrix_copy[k], matrix_copy[i]
                        det *= -1

                    pivot = matrix_copy[i][i]
                    det *= pivot
                    matrix_copy[i] = [elem / pivot for elem in matrix_copy[i]]

                    for j in range(i + 1, n):
                        factor = matrix_copy[j][i]
                        matrix_copy[k] = [x - y * factor for x, y in zip(matrix_copy[k], matrix_copy[i])]
                    break
        return det

    def row_echelon(self):
        pivot = 0
        for row in range(self.shape[0]):
            if pivot >= self.shape[1]:
                break
            while self.data[row][pivot] == 0:
                pivot += 1
                if pivot >= self.shape[1]:
                    return self
                for i in range(row + 1, self.shape[0]):
                    if self.data[i][pivot] != 0:
                        self.data[row], self.data[i] = self.data[i], self.data[row]
                        break
            divisor = self.data[row][pivot]
            self.data[row] = [elem / divisor for elem in self.data[row]]
            for i in range(self.shape[0]):
                if i != row:
                    multiplier = self.data[i][pivot]
                    self.data[i] = [elem - multiplier * self.data[row][j] for j, elem in enumerate(self.data[i])]
                pivot += 1
            return self

    def inverse(self):
        if self.shape[0] != self.shape[1]:
            raise TypeError("Inverse is undefined for non-square matrices.")
        
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible.")
        
        # Create an augmented matrix [A|I]
        augmented_matrix = [row[:] + [1.0 if i == j else 0.0 for j in range(self.shape[0])] for i, row in enumerate(self.data)]
        augmented_matrix = Matrix(augmented_matrix)

        # Apply Gauss-Jordan elimination to obtain the reduced row-echelon form
        rref_matrix = augmented_matrix.row_echelon()

        # Extract the inverse matrix [I|B]
        inverse_matrix_data = [row[self.shape[0]:] for row in rref_matrix.data]
        return Matrix(inverse_matrix_data)

class Vector(Matrix):
    def __init__(self, data):
        # data düz bir listeyse, onu liste içinde liste formatına dönüştür
        if isinstance(data, list) and all(isinstance(i, (int, float, complex)) for i in data):
            self.data = [[i] for i in data]  # Vektör, dikey bir vektör olarak tanımlanır
            self.shape = (len(data), 1)
            self.size = len(data)
        elif isinstance(data, list):
            # Eğer liste zaten liste içinde liste formatındaysa, direkt olarak işle
            if len(data) == 1 and isinstance(data[0], list) and all(isinstance(i, (int, float, complex)) for i in data[0]):
                self.data = data
                self.shape = (len(data[0]), 1)
                self.size = len(data[0])
            elif all(isinstance(elem, list) and len(elem) == 1 and all(isinstance(i, (int, float, complex)) for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), 1)
                self.size = len(data)
            else:
                raise ValueError("Invalid form of list,", data)
        else:
            raise ValueError("Invalid form of data,", data)

    def __repr__(self):
        return f"Vector({self.data})"
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float, complex)):
            raise TypeError("The scalar multiplier must be a number.")
        result = [[self.data[i][0] * scalar] for i in range(self.shape[0])]
        return Vector(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can only add another Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape.")
        result = [[self.data[i][0] + other.data[i][0]] for i in range(self.shape[0])]
        return Vector(result)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can only subtract another Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape.")
        result = [[self.data[i][0] - other.data[i][0]] for i in range(self.shape[0])]
        return Vector(result)
    
    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)
    

u = Matrix([[1., 0.],[0., 1.]])
print(u.inverse())# '[[1, 0], [0, 1]]'

u = Matrix([[2., 0.],[0., 2.]])
print(u.inverse())# '[[0.5, 0], [0, 0.5]]'

u = Matrix([[0.5, 0.],[0., 0.5]])
print(u.inverse())# '[[2, 0], [0, 2]]'

u = Matrix([[0., 1.],[1., 0.]])
print(u.inverse())# '[[0, 1], [1, 0]]'

u = Matrix([[1., 2.],[3., 4.]])
print(u.inverse())# '[[-2, 1], [1.5, -0.5]]'