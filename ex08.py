
from matrix import Matrix

def ex1():
	u = Matrix([[0., 0.],[0., 0.]])
	print(u.trace()); # 0.0

	u = Matrix([[1., 0.],[0., 1.]])
	print(u.trace()); # 2.0

	u = Matrix([[1., 2.],[3., 4.]])
	print(u.trace()); # 5.0
	
	u = Matrix([[8., -7.],[4., 2.]])
	print(u.trace()); # 10.0

	u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
	print(u.trace()); # 3.0

def main():
	u = Matrix([[1., 0.],[0., 1.]]);
	print(u.trace()); # 2.0

	u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]]);
	print(u.trace()); # 9.0

	u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.]]);
	print(u.trace()); # -21.0

if __name__ == "__main__":
	ex1()
	#main()
