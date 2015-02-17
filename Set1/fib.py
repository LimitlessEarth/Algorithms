

a = [0]*201
a[0] = 0
a[1] = 1
for i in range(2,201):
    a[i] = a[i-1] + a[i-2]
    i+=1

print "a[200]: ", a[200]
