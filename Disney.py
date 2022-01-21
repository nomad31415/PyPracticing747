inp =[ "started,job_id=1,job_name=ls", "end,job_id=1,job_time=90", "started,job_id=2,job_name=cp","end,job_id = 2, job_time=50" ]



d = {}
out = []

for i in inp:
	if "started" in  i:
		tmp = i.split(",")
                for ii in  tmp[1:]:
			k,v = ii.split("=")
			out.append(v)
	elif "end" in i:
	        tmp = i.split(",")
		for ii in tmp[1:]:
			k,v = ii.split("=")
			if k.strip() == "job_time":
				out.append(v)
		s = out[0]	
	        d[s] = out
		out = []




print( sorted(d.items(), key=lambda item: int((item[1])[2]),reverse=True))
#print(d)
#print( {k: v for k, v in sorted(d.items(), key=lambda item: int((item[0])),reverse=True)})
