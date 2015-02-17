

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


r = [1,2,5,6]
t = [3,4,7,8]
c = Median(4, r, t)
print c
