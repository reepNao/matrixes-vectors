
import numpy as np
from matrix import Vector

def ex1():
	u = Vector([[0., 0., 0.]]);
	v = Vector([[0., 0., 0.]]);
	print(Vector.cross_product(u, v)); # [0.][0.][0.]

	u = Vector([[1., 0., 0.]]);
	v = Vector([[0., 0., 0.]]);
	print(Vector.cross_product(u, v)); # [0.][0.][0.]

	u = Vector([[1., 0., 0.]]);
	v = Vector([[0., 1., 0.]]);
	print(Vector.cross_product(u, v)); # [0.][0.][1.]

	u = Vector([[8., 7., -4.]]);
	v = Vector([[3., 2., 1.]]);
	print(Vector.cross_product(u, v)); # [15.][-20.][-5.]

	u = Vector([[1., 1., 1.]]);
	v = Vector([[0., 0., 0.]]);
	print(Vector.cross_product(u, v)); # [0.][0.][0.]

	u = Vector([[1., 1., 1.]]);
	v = Vector([[1., 1., 1.]]);
	print(Vector.cross_product(u, v)); # [0.][0.][0.]

def main():
	u = Vector([[0., 0., 1.]]);
	v = Vector([[1., 0., 0.]]);
	print(Vector.cross_product(u, v)); # [0.][1.][0.]
	#print(np.cross([0., 0., 1.], [1., 0., 0.]))

	u = Vector([[1., 2., 3.]]);
	v = Vector([[4., 5., 6.]]);
	print(Vector.cross_product(u, v)); # [-3.][6.][-3.]

	u = Vector([[4., 2., -3.]]);
	v = Vector([[-2., -5., 16.]]);
	print(Vector.cross_product(u, v)); # [17.][-58.][-16.]

if __name__ == "__main__":
	ex1()
	#main()
