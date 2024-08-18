from matrix import Matrix

def ex1():
	u = Matrix([[0., 0.],[0., 0.]])
	print(u.rank()) # 0

	u = Matrix([[1., 0.],[0., 1.]])
	print(u.rank()) # 2

	u = Matrix([[2., 0.],[0., 2.]])
	print(u.rank()) # 2

	u = Matrix([[1., 1.],[1., 1.]])
	print(u.rank()) # 1

	u = Matrix([[0., 1.],[1., 0.]])
	print(u.rank()) # 2

	u = Matrix([[1., 2.],[3., 4.]])
	print(u.rank()) # 2

	u = Matrix([[-7., 5.],[4., 6.]])
	print(u.rank()) # 2

def main():
	u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
	print(u.rank()) # 3
	u = Matrix([[ 1., 2., 0., 0.],[ 2., 4., 0., 0.],[-1., 2., 1., 1.]])
	print(u.rank()) # 2
	u = Matrix([[ 8., 5., -2.],[ 4., 7., 20.],[ 7., 6., 1.],[21., 18., 7.]])
	print(u.rank()) # 3

if __name__ == "__main__":
	ex1()
	#main()