
from matrix import Matrix, Vector

def ex1():
	u = Matrix([[0., 0.], [0., 0.]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [0.][0.]

	u = Matrix([[1., 1.], [1., 1.]]);
	print(u.mul_vec(v)); # [6.][6.]

	u = Matrix([[2., 0.],[0., 2.]]);
	v = Vector([[2., 1.]]);
	print(u.mul_vec(v)); # [4.][2.]

	u = Matrix([[0.5, 0.], [0., 0.5]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [2.][1.]

def main():
	u = Matrix([[1., 0.], [0., 1.]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [4.][2.]

	u = Matrix([[2., 0.],[0., 2.]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [8.][4.]

	u = Matrix([[2., -2.],[-2., 2.]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [4.][-4.]

	u = Matrix([[1., 0.],[0., 1.]]);
	v = Matrix([[1., 0.],[0., 1.]]);
	print(u.mul_mat(v)); # [1., 0.][0., 1.]

	u = Matrix([[1., 0.],[0., 1.]]);
	v = Matrix([[2., 1.],[4., 2.]]);
	print(u.mul_mat(v)); # [2., 1.][4., 2.]

	u = Matrix([[3., -5.],[6., 8.]]);
	v = Matrix([[2., 1.],[4., 2.]]);
	print(u.mul_mat(v)); # [-14., -7.][44., 22.]

if __name__ == "__main__":
	ex1()
	#main()
