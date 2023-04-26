def doc_it(func):
	def newFuc(*args, **kargs):
		res = func(*args, **kargs)
		print(args)
		print('res:', res)
		return res
	return newFuc




@doc_it
def add(a,b):
	return a + b




if __name__ == '__main__':
	z = add(11,77)
	print(z)








