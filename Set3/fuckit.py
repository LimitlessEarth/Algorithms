def Wordsort() :
	f = []
	with open('wordlst.txt') as my_file :
	f = my_file.readlines()


	d = []
	e = []
	a = 0
	b = len(f)/2
	while a < b :
		d[a] = f[a]
		e[a] = f[a+b]
		a += 1 




	Median(b, d, e)


def Median(n, d = [], e = []) :
	if d[0] > e[n-1] :
		return (d[0] + e[n-1])/2
	elif d[n-1] < e[0] :
		return (d[n-1] + e[n])/2
	else :
		a = 0
		b = n-1
		while(a < b) :
			mid = (a + b + 1)/2
			if (e[mid] < d[n - mid -1]) :
				a = mid
			elif (e[mid] > d[n-mid-1]) :
				b = mid - 1
				mid = b
			else :
				break
		if (min(d[n - mid - 1], e[mid + 1]) > max (d[n - mid - 2], e[mid])) :
			return max (d[n - mid - 2], e[mid])
			
		else :
			return min(d[n - mid - 1], e[mid + 1])

