import random

f=open("integers.txt","r")
sum=0
for line in f.readlines():
    sum=sum+int(line)

print(sum)
print("thank you")
f.close()