N=int(input())

for i in range(N):
	M = float(input())
	d =0
	if(M>1):
		while(M>1):
			d = d+1
			#print(d)
			M = M/2
	print(d, "dias")

