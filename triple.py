src = [1,0,-1, 2,4,-6,1,2,5]

cnt = 0 

for i in  range(0,len(src)):
    for k in  range(i + 1, len(src)):
    	for l in range(i + 2, len(src)):

		print(src[i],src[k],src[l])
		cnt+=1
		print("n = ",cnt)



