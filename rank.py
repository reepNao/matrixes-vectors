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

    def rank(self):
        if self.shape[0] == 0 or self.shape[1] == 0:
            return 0

        # Copy the matrix to avoid modifying the original matrix
        matrix_copy = [row.copy() for row in self.data]
        num_rows, num_cols = self.shape
        rank = 0

        for col in range(num_cols):
            # Find the pivot row for the current column
            pivot_row = None
            for row in range(rank, num_rows):
                if matrix_copy[row][col] != 0:
                    pivot_row = row
                    break

            if pivot_row is None:
                continue
            
            # Swap current row with the pivot row
            if pivot_row != rank:
                matrix_copy[rank], matrix_copy[pivot_row] = matrix_copy[pivot_row], matrix_copy[rank]

            # Eliminate all other entries in this column
            for row in range(num_rows):
                if row != rank:
                    multiplier = matrix_copy[row][col] / matrix_copy[rank][col]
                    matrix_copy[row] = [matrix_copy[row][i] - multiplier * matrix_copy[rank][i] for i in range(num_cols)]
            
            # Move to the next row
            rank += 1

        return rank

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

u = Matrix([[0., 0.],[0., 0.]])
print(u.rank()) # 0

u = Matrix([[1., 0.],[0., 1.]])
print(u.rank()) # 2

u = Matrix([[2., 0.],[0., 2.]])
print(u.rank()) # 2

u = Matrix([[1., 1.],[1., 1.]])
print(u.rank()) # 1

u = Matrix([[0., 1.],[1., 0.]])
print(u.rank()) # 2

u = Matrix([[1., 2.],[3., 4.]])
print(u.rank()) # 2