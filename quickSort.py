def qs(array):
  if len(array) < 2:
  	return array
  else:	
     pivot = array[0]
     less = [i for i in array[1:] if i <= pivot]	
     greater = [i for i in array[1:] if i > pivot]

     return qs(less) + [pivot] + qs(greater)


if __name__ == '__main__':
   print(qs([10,5,2,3]))
