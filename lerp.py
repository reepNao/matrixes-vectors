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
        return f"Vector({self.data})"
    
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
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        if not (isinstance(t, (int, float)) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        if any(isinstance(u, accepted_type) for accepted_type in [int, float, complex, Vector, Matrix]):
            return u + (v - u) * t 
        else:
            raise TypeError("Invalid input: unsupported type")


        
print("Test 1 - int:")
print(Matrix.lerp(0, 10, 0.5))  # Beklenen çıktı: 5.0

print("Test 2 - float:")
print(Matrix.lerp(1.0, 4.0, 0.25))  # Beklenen çıktı: 1.75

print("Test 3 - complex:")
print(Matrix.lerp(1+1j, 2+2j, 0.5))  # Beklenen çıktı: (1.5+1.5j)

e1 = Vector([1., 2., 3.])
e2 = Vector([4., 5., 6.])
print("Test 4 - Vector:")
print(Vector.lerp(e1, e2, 0.5))  # Beklenen çıktı: Vector([[2.5, 3.5, 4.5]])

m1 = Matrix([[1., 2.], [3., 4.]])
m2 = Matrix([[5., 6.], [7., 8.]])
print("Test 5 - Matrix:")
print(Matrix.lerp(m1, m2, 0.5))  # Beklenen çıktı: Matrix([[3.0, 4.0], [5.0, 6.0]])

print("Test 6 - t = 0:")
print(Matrix.lerp(5, 15, 0.4))  # Beklenen çıktı: 9.0

print("Test 7 - t = 1.0:")
print(Matrix.lerp(5, 15, 1))  # Beklenen çıktı: 15.0
