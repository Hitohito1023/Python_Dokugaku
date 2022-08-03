# x = 100

# def f():
# 	global x
# 	x += 1
# 	print(x)

# f()

# print(x)


# n = input("数字を入れてください")

# print(n)

# a = input("type a number:")
# b = input("type another")
# a = int(a)
# b = int(b)
# try:
# 	print(a / b)
# except ZeroDivisionError:
# 	print("b cannot be zero.")

# Question1
# def q1(x):
# 	return x**2

# # Question2
# def q2(string):
# 	print(string)

# q2("こんにちは")

# Question3
# def q3(a, b, c, d = 0, e = "デフォルト"):
# 	a = str(a)
# 	b = str(b)
# 	c = str(c)
# 	d = str(d)
# 	print(a + b + c + d + e)

# q3(10, 5, 10)

# Question4
# def num1(n):
# 	s =  n // 2
# 	num2(s)

# def num2(s):
# 	print(s * 2)

# num2(10)

# Question5
def q5(x):
	try:
		return float(x)
	except ValueError:
		print("数字のみでお願いします")
q5("aiueo")
q5(19)