if __name__ == '__main__':

	arr = [1,1,2,3,1,2,2,3,4,4]

	s = set(arr)

	a = [arr.count(x) for x in s]

	z = max(list(filter(lambda x: a.count(x) == 2,a)))

	print(z)
	

