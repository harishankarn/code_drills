a = input()
a = a.split()

a=[eval(i) for i in a]

if 1<= a[0]<= 100:
	if 1<= a[1]<= 100:
		print(a[1]+a[0])
