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

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")
        if self.shape != other.shape:
            raise ValueError(f"Invalid input: addition requires matrices of the same shape.")
        
        # Toplama işlemini yap
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]
        
        return Matrix(result)


    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The argument must be a Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] 
                for i in range(self.shape[0])]
        return Matrix(result)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("The scalar multiplier must be a number.")
        result = [[self.data[i][j] * scalar for j in range(self.shape[1])]
                for i in range(self.shape[0])]
        return Matrix(result)
    
    @staticmethod
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("u and v must be of the same type.")
        if not (isinstance(t, float) and 0 <= t <= 1):
            raise ValueError("t must be a float between 0 and 1.")
        if isinstance(u, (int, float, complex)):
            return u + (v - u) * t
        elif isinstance(u, Matrix):
            return Matrix([[cell_u + (cell_v - cell_u) * t for cell_u, cell_v in zip(row_u, row_v)]
                           for row_u, row_v in zip(u.data, v.data)])
        else:
            raise TypeError("Unsupported type for u and v. Supported types are int, float, complex, and Matrix.")

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

    def mul_mat(self, other):
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Matrices cannot be multiplied, dimensions don't match.")
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])])
                       for i in range(self.shape[0])] for j in range(other.shape[1])]
            return Matrix(result)
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
        result = self.data.copy()
        rows, cols = self.shape
        for i in range(min(rows, cols)):
            if result[i][i] == 0:
                for j in range(i + 1, rows):
                    if result[j][i] != 0:
                        result[i], result[j] = result[j], result[i]
                        break
            if result[i][i] == 0:
                continue
            for j in range(i + 1, rows):
                factor = result[j][i] / result[i][i]
                for k in range(i, cols):
                    result[j][k] -= factor * result[i][k]
        return Matrix(result)
    """
    def row_echelon(self):
        # Satır ve sütun sayıları
        rows, cols = self.shape
        row = 0  # İşlem yapılacak satır

        for col in range(cols):
            # Bulunduğumuz sütunda sıfır olmayan bir eleman arayın
            pivot_row = None
            for r in range(row, rows):
                if self.data[r][col] != 0:
                    pivot_row = r
                    break
            
            if pivot_row is None:
                continue  # Eğer geçerli bir pivot bulunamazsa, devam edin
            
            # Pivot satır ile mevcut satırı değiştirin
            if pivot_row != row:
                self.data[row], self.data[pivot_row] = self.data[pivot_row], self.data[row]

            # Pivot elemanını 1 yapın
            pivot = self.data[row][col]
            for j in range(col, cols):
                self.data[row][j] /= pivot
            
            # Diğer satırlardaki bu sütunu sıfırlayın
            for r in range(rows):
                if r != row:
                    factor = self.data[r][col]
                    for j in range(col, cols):
                        self.data[r][j] -= factor * self.data[row][j]

            row += 1
            if row >= rows:
                break
        
        return self
    """
    
    """
    def row_echelon(self):
		# gaussian elimination with back-substitution for reduced row echelon from
		pivot = 0
		for row in range(self.shape[0]):
			if pivot >= self.shape[1]:
				break
			# find a non-zero pivot element in the current pivot
			while self.data[row][pivot] == 0:
				pivot += 1
				if pivot >= self.shape[1]:
					return self
			# swap the current row with a row containing a non-zero pivot element
			for i in range(row + 1, self.shape[0]):
				if self.data[i][pivot] != 0:
					self.data[row], self.data[i] = self.data[i], self.data[row]
					break
			# scale the current row to make the pivot element 1
			divisor = self.data[row][pivot]
			self.data[row] = [elem / divisor for elem in self.data[row]]

			# perform the row operations to eliminate other non-zero elements in the current column
			for i in range(self.shape[0]):
				if i != row:
					multiplier = self.data[i][pivot]
					self.data[i] = [elem - multiplier * self.data[row][j] for j, elem in enumerate(self.data[i])]
			pivot += 1
		return self
    """



# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbattal <rbattal@student.42kocaeli.com.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/16 12:42:12 by rbattal           #+#    #+#              #
#    Updated: 2024/08/16 12:42:13 by rbattal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rbattal <rbattal@student.42kocaeli.com.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/16 12:42:12 by rbattal           #+#    #+#              #
#    Updated: 2024/08/16 12:42:13 by rbattal          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Vector(Matrix):

    def __init__(self, data):
        self.data = []
		# when data is a list
        if isinstance(data, list):
			# initialize a list of a list of floats : Vector([[0.0, 1.0, 2.0, 3.0]])
            if len(data) == 1 and isinstance(data[0], list) and len(data[0]) > 0 and all(type(i) in [int, float, complex] for i in data[0]):	
                self.data = data
                self.shape = (1, len(data[0]))
                self.size = len(data[0])
            elif all(isinstance(elem, list) and len(elem) == 1 and all(type(i) in [int, float, complex] for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), 1)
                self.size = len(data)
            else:
                raise ValueError("Invalid form of list,", data)
        else:
            raise ValueError("Invalid form of data,", data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))
        if self.shape != other.shape:
            raise ValueError("Invalid input: __add__ requires vectors of the same shape.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(result)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))
        if self.shape != other.shape:
            raise ValueError("Invalid input: __sub__ requires vectors of the same shape.")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(result)
    
    def __mul__(self, other):
        if any(isinstance(other, scalar_type) for scalar_type in [int, float, complex]):
            result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        elif isinstance(other, Vector):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Vectors cannot be multiplied, dimensions don't match.")
            result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        elif isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Matrices cannot be multiplied, dimensions don't match.")
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Matrix(result)
        else:
            raise TypeError("Invalid type of input value.")
    
    @staticmethod
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        if not (isinstance(t, float) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        if any(isinstance(u, accepted_type) for accepted_type in [int, float, complex, Vector, Matrix]):
            return u + (v - u) * t 
        else:
            raise TypeError("Invalid input: unsupported type")
        
    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The argument must be a Vector.")
        result = 0.0
        if self.size != other.size:
            raise ValueError("Vectors must have the same size for dot product.")
    
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
    
    def angle_cos(u, v):
        if not isinstance(u, Vector) or not isinstance(v, Vector):
            raise TypeError("Both arguments must be instances of the Vector class.")
        if u.size != v.size:
            raise ValueError("Vectors must have the same size.")
        if u.size == 0 or v.size == 0:
            raise ValueError("Vectors must have at least one element.")
        dot_product = u.dot(v) #or v.dot(v)
        u_norm = u.norm()
        v_norm = v.norm()
        cos_theta = dot_product / (u_norm * v_norm)
        return cos_theta
    
    def cross_product(u, v):
        if len(u.data[0]) != 3 or len(v.data[0]) != 3:
            raise ValueError("Both vectors must have a size of 3 for cross product.")
        [x1, y1, z1] = u.data[0]
        [x2, y2, z2] = v.data[0]
        result_x, result_y, result_z = y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2
        return Vector([[result_x, result_y, result_z]])
    
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
        

    
    
    
