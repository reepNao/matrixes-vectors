from matrix import Vector

def ex1():
	u = Vector([[0., 0.]]);
	v = Vector([[0.], [0.]]);
	print(u.dot(v)); # 0.0

	u = Vector([[1., 0.]]);
	v = Vector([[0.], [0.]]);
	print(u.dot(v)); # 0.0

	u = Vector([[1., 0.]]);
	v = Vector([[1.], [0.]]);
	print(u.dot(v)); # 1.0

	u = Vector([[1., 0.]]);
	v = Vector([[0.], [2.]]);
	print(u.dot(v)); # 0.0

	u = Vector([[1., 1.]]);
	v = Vector([[1.], [1.]]);
	print(u.dot(v)); # 2.0

	u = Vector([[4., 2.]]);
	v = Vector([[2.], [1.]]);
	print(u.dot(v)); # 10.0

def main():
	u = Vector([[0., 0.]]);
	v = Vector([[1.], [1.]]);
	print(u.dot(v)); # 0.0

	u = Vector([[1., 1.]]);
	v = Vector([[1.], [1.]]);
	print(u.dot(v)); # 2.0

	u = Vector([[-1., 6.]]);
	v = Vector([[3.], [2.]]);
	print(u.dot(v)); # 9.0

if __name__ == "__main__":
	ex1()