import numpy as np

class Matrix:

    def __repr__(self):
        return f"Matrix({self.data})"

    def __init__(self, data):
        if isinstance(data, list) and all(isinstance(row, list) for row in data):
            self.data = data
            self.shape = (len(data), len(data[0])) 
        elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(dim, int) for dim in data):
            self.data = [[0] * data[1] for _ in range(data[0])]
            self.shape = data
        else:
            raise ValueError("Invalid form of data:", data)

    def add(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The argument must be a Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
                for i in range(self.shape[0])]
        return Matrix(result)
    
    def sub(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The argument must be a Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] 
                for i in range(self.shape[0])]
        return Matrix(result)
    
    def scl(self, other):
        if not isinstance(other, (int, float, complex)):
            raise TypeError("The scalar multiplier must be a number.")
        result = [[self.data[i][j] * other for j in range(self.shape[1])]
                for i in range(self.shape[0])]
        return Matrix(result)
    
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
    
    @staticmethod
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        if not (isinstance(t, (int, float)) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        if any(isinstance(u, accepted_type) for accepted_type in [int, float, complex, Vector, Matrix]):
            return u + (v - u) * t 
        else:
            raise TypeError("Invalid input: unsupported type")

    def mul_vec(self, other):
        if isinstance(other, Vector):
            if self.shape[1] != len(other.data[0]):
                raise ValueError("Matrix columns must match vector size.")
            result = []
            for row in self.data:
                sum_product = 0
                for col in range(len(other.data[0])):
                    sum_product += row[col] * other.data[0][col]
                result.append([sum_product])
            return Vector(result)
        else:
            raise TypeError("Invalid type of input value.")

    def trace(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix must be square for trace.")
        result = 0.0
        for i in range(self.shape[0]):
            result = result + self.data[i][i]
        return result

    def transpose(self):
        transposed_matrix = []
        for j in range(self.shape[1]):
            row = []
            for i in range(self.shape[0]):
                row.append(self.data[i][j])
            transposed_matrix.append(row)
        return Matrix(transposed_matrix)

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


# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbattal <rbattal@student.42kocaeli.com.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/20 01:16:01 by rbattal           #+#    #+#              #
#    Updated: 2024/08/20 01:16:02 by rbattal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Vector(Matrix):
    def __repr__(self):
        return f"Vector({self.data})"
    
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
                self.shape = (1, len(data[0]))
                self.size = len(data[0])
            elif all(isinstance(elem, list) and len(elem) == 1 and all(isinstance(i, (int, float, complex)) for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), 1)
                self.size = len(data)
            else:
                raise ValueError("Invalid form of list,", data)
        else:
            raise ValueError("Invalid form of data,", data)

    # Override the add method to return a Vector instead of a Matrix
    def add(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The argument must be a Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = [[self.data[i][0] + other.data[i][0]] for i in range(self.shape[0])]
        return Vector(result)

    # Override the sub method to return a Vector instead of a Matrix
    def sub(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The argument must be a Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        result = [[self.data[i][0] - other.data[i][0]] for i in range(self.shape[0])]
        return Vector(result)

    # Override the scl method to return a Vector instead of a Matrix
    def scl(self, scalar):
        if not isinstance(scalar, (int, float, complex)):
            raise TypeError("The scalar multiplier must be a number.")
        result = [[self.data[i][0] * scalar] for i in range(self.shape[0])]
        return Vector(result)
    
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
    
    @staticmethod
    def linear_combination(lst_vectors, coefs):
        if not all(isinstance(lst, list) for lst in [lst_vectors, coefs]):
            raise ValueError("Invalid form of list")
        if not all(isinstance(v, Vector) for v in lst_vectors):
            raise TypeError("Invalid input: list should contain only Vectors.", lst_vectors)
        if not all(v.size == lst_vectors[0].size for v in lst_vectors):
            raise TypeError("Invalid input: list of Vectors should contain Vectors of the same shape.", lst_vectors)
        if len(coefs) != len(lst_vectors) or not all(type(i) in [int, float] for i in coefs):
            raise TypeError("Invalid input: unsupported type or incompatible length with list of Vectors", coefs)
        
        # Başlangıçta sıfır vektörü, lst_vectors'teki vektörlerle aynı boyutta oluşturuluyor
        v_size = lst_vectors[0].size
        v = Vector([[0.0] for _ in range(v_size)])  # Dikey bir vektör oluşturuldu
        
        for vector, coef in zip(lst_vectors, coefs):
            v += vector * coef
        return v
    
    @staticmethod
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        if not (isinstance(t, (int, float)) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        if any(isinstance(u, accepted_type) for accepted_type in [int, float, complex, Vector, Matrix]):
            return u + (v - u) * t 
        else:
            raise TypeError("Invalid input: unsupported type")
        
    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The argument must be a Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for dot product.")
        result = sum(self.data[i][0] * other.data[i][0] for i in range(self.shape[0]))
        return result

    def norm(self):
        square_result = 0.0
        vector_data = np.reshape(self.data, (1, -1))[0]
        for element in vector_data:
            square_result += element ** 2
        square_root = square_result ** 0.5
        return square_root

    
    def norm_1(self):
        result = 0.0
        vector_data = np.reshape(self.data, (1, -1))[0]
        for element in vector_data:
            if element < 0:
                result -= element
            else:
                result += element
        return result
    
    def norm_inf(self):
        abs_value = 0.0
        max_abs_value = float('-inf')
        lst_data = np.reshape(self.data, (1, -1))[0]
        for elem in lst_data:
            if elem >= 0:
                abs_value = elem
            else:
                abs_value = -elem
            if abs_value > max_abs_value:
                max_abs_value = abs_value
        return max_abs_value

    @staticmethod
    def angle_cos(u, v):
        if not isinstance(u, Vector) or not isinstance(v, Vector):
            raise TypeError("Both arguments must be instances of the Vector class.")
        if u.shape != v.shape:
            raise ValueError("Vectors must have the same shape.")
        dot_product = u.dot(v)
        u_norm = u.norm()
        v_norm = v.norm()
        if u_norm == 0 or v_norm == 0:
            raise ValueError("Vectors must have non-zero norms.")
        cos_theta = dot_product / (u_norm * v_norm)
        return cos_theta

    def cross_product(u, v):
        if len(u.data[0]) != 3 or len(v.data[0]) != 3:
            raise ValueError("Both vectors must have a size of 3 for cross product.")
        [x1, y1, z1] = u.data[0]
        [x2, y2, z2] = v.data[0]
        result_x, result_y, result_z = y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2
        return Vector([[result_x, result_y, result_z]])
