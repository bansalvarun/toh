def Towers(height, start, target, help,R):
    if height>=1:
        Towers(height-1,start,help,target,R)
        print "Move disk %s from %s to %s" %(R[height-1]-1,start, target)
        Towers(height-1,help,target,start,R)



x = input("Enter number of disks")

R=range(x)
for i in range(x):
    R[i]+=1

Rev=R[::-1]

A='A'
B='B'
C='C'

Towers(x,A,B,C,Rev)

