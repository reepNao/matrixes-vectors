from matrix import Matrix, Vector


u = Vector([[0.]]);
print(u.norm_1(), u.norm(), u.norm_inf()); # 0.0, 0.0, 0.0

u = Vector([[1., 2., 3.]]);
print(u.norm_1(), u.norm(), u.norm_inf()); # 6.0, 3.7416573867739413, 3.0

u = Vector([[-1., -2.]]);
print(u.norm_1(), u.norm(), u.norm_inf()); # 3.0, 2.23606797749979, 2.0

u = Vector([[1., 0.]]);
print(u.norm_1(), u.norm(), u.norm_inf()); # 1.0, 1.0, 1.0
