def  rIn(arr):
        d = {}

	for i, s in enumerate(arr):
  	  #print(i,s)
	  
	  for ii, t in enumerate(s.split()):
	    if t not in d.values():
	      d[t] = (i,ii)
        print(sorted(d))



ai = "I have seen it , and i bought it"

arr = ai.split()

rIn(arr)







