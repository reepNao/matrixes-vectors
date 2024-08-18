from matrix import Matrix

def ex1():
	u = Matrix([[ 0., 0.],[0., 0.]]);
	print(u.determinant()); # 0.0

	u = Matrix([[ 1., 0.],[0., 1.]]);
	print(u.determinant()); # 1.0

	u = Matrix([[ 2., 0.],[0., 2.]]);
	print(u.determinant()); # 4.0

	u = Matrix([[ 1., 1.],[1., 1.]]);
	print(u.determinant()); # 0.0

	u = Matrix([[ 0., 1.],[1., 0.]]);
	print(u.determinant()); # -1.0

	u = Matrix([[ 1., 2.],[3., 4.]]);
	print(u.determinant()); # -2.0

	u = Matrix([[ -7., 5.],[4., 6.]]);
	print(u.determinant()); # -62.0

	u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]);
	print(u.determinant()); # 1.0

def main():
	u = Matrix([[ 1., -1.],[-1., 1.]]);
	print(u.determinant()); # 0.0

	u = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]]);
	print(u.determinant()); # 8.0

	u = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]]);
	print(u.determinant()); # -174.0

	u = Matrix([[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]]);
	print(u.determinant()); # 1032

if __name__ == "__main__":
	ex1()