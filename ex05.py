
from matrix import Vector

def ex1():
	v = Vector([[8., 7.]]);
	u = Vector([[3., 2.]]);
	print(Vector.angle_cos(u, v)); # '0.9914542955425437'

	v = Vector([[1., 1.]]);
	u = Vector([[1., 1.]]);
	print(Vector.angle_cos(u, v)); # 1.0

	v = Vector([[4., 2.]]);
	u = Vector([[1., 1.]]);
	print(Vector.angle_cos(u, v)); # '0.9486832980505138'

	v = Vector([[-7., 3.]]);
	u = Vector([[6., 4.]]);
	print(Vector.angle_cos(u, v)); # '-0.5462677805469223'

def main():
	v = Vector([[1., 0.]]);
	u = Vector([[1., 0.]]);
	print(Vector.angle_cos(u, v)); # 1.0

	u = Vector([[1., 0.]]);
	v = Vector([[0., 1.]]);
	print(Vector.angle_cos(u, v)); # 0.0

	u = Vector([[-1., 1.]]);
	v = Vector([[ 1., -1.]]);
	print(Vector.angle_cos(u, v)); # -1.0

	u = Vector([[2., 1.]]);
	v = Vector([[4., 2.]]);
	print(Vector.angle_cos(u, v)); # 1.0

	u = Vector([[1., 2., 3.]]);
	v = Vector([[4., 5., 6.]]);
	print(Vector.angle_cos(u, v)); # 0.974631846

if __name__ == "__main__":
	ex1()
	#main()
