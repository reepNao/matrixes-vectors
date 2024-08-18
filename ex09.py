from matrix import Matrix

def ex1():
	u = Matrix([[0., 0.],[0., 0.]])
	print("transposed:", u.T()) # '[[0, 0], [0, 0]]'

	u = Matrix([[1., 0.],[0., 1.]])
	print("transposed:", u.T()) # '[[1, 0], [0, 1]]'

	u = Matrix([[1., 2.],[3., 4.]])
	print("transposed:", u.T()) # '[[1, 3], [2, 4]]'

	u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
	print("transposed:", u.T()) # '[[1, 0, 0], [0, 1, 0], [0, 0, 1]]'

def main():
	m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
	print("original:", m1)
	print("transposed:", m1.T()) # Output: Matrix([[0., 2., 4.], [1., 3., 5.]])

	print()
	m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
	print("original:", m1)
	print("transposed:", m1.T()) # Output: Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

if __name__ == "__main__":
	ex1()
	#main()