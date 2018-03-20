sum=0
for x in range(1,101):
	x=x**2
	sum+=x
	x+=1
print(sum)
sum1=0	
for y in range(1,101):
	sum1+=y
	y+=1

z=sum1**2
print(z)
a=z-sum

print(a)