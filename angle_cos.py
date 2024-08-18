import math

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

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The argument must be a Vector.")
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for dot product.")
        result = sum(self.data[i][0] * other.data[i][0] for i in range(self.shape[0]))
        return result
    
    def norm(self):
        return math.sqrt(sum(x[0] ** 2 for x in self.data))
    
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

# Test
v = Vector([[8.], [7.]])
u = Vector([[3.], [2.]])
print(Vector.angle_cos(u, v))  # Örnek: 0.9914542955425437

v = Vector([[1.], [1.]])
u = Vector([[1.], [1.]])
print(Vector.angle_cos(u, v))  # 1.0

v = Vector([[4.], [2.]])
u = Vector([[1.], [1.]])
print(Vector.angle_cos(u, v))  # Örnek: 0.9486832980505138
