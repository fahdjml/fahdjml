import math
print ― The four digit perfect square with even digits are:‖,\n
for i in range (1000,10000):
num= int (math.sqrt(i))
if (num * num==1):
n=i
while (n !=0):
r= n%10
n=n//10
if (r%2!=0):
break
OUTPUT
else:
print(i)
