from matrix import Vector

def ex1():
	u = Vector([[0.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 0.0, 0.0, 0.0

	u = Vector([[1.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 1.0, 1.0, 1.0

	u = Vector([[0., 0.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 0.0, 0.0, 0.0

	u = Vector([[1., 0.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 1.0, 1.0, 1.0

	u = Vector([[2., 1.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 3.0, 2.236067977, 2.0

	u = Vector([[4., 2.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 6.0, 4.472135955, 4.0

	u = Vector([[-4., -2.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 6.0, 4.472135955, 4.0

def main():
	u = Vector([[0., 0., 0.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 0.0, 0.0, 0.0

	u = Vector([[1., 2., 3.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 6.0, 3.74165738, 3.0

	#u = Vector([[1.], [2.], [3.]]);
	#print(u.norm_1(), u.norm(), u.norm_inf());

	u = Vector([[-1., -2.]]);
	print(u.norm_1(), u.norm(), u.norm_inf()); # 3.0, 2.236067977, 2.0

if __name__ == "__main__":
	ex1()
	#main()