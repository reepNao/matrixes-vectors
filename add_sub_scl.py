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

    def __repr__(self):
        return f"Vector({self.data})"

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




######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


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
#		    for Vectors             #
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

result1_scl = v1.scl(3)
print(result1_scl)  # Vector([[3.0, 6.0, 9.0]])
