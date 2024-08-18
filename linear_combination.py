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

e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])


v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])


result1 = Vector.linear_combination([e1, e2, e3], [2, 3, 4])
print(result1)  # Expected output: Vector([[2.0, 3.0, 4.0]])

result2 = Vector.linear_combination([v1, v2], [1, 2])
print(result2)  # Expected output: Vector([[1.0, 22.0, -197.0]])

result3 = Vector.linear_combination([e1, v1, v2], [1, 0.5, -0.1])
print(result3)  # Expected output: Vector([[1.0, 7.0, -7.7]])


result4 = Vector.linear_combination([e1, e2, e3], [10, -2, 0.5])
print(result4)  # Expected output: Vector([[10.0, -2.0, 0.5]])

result5 = Vector.linear_combination([v1, v2], [10, -2])
print(result5)  # Expected output: Vector([[1.0, 22.0, -197.0]])