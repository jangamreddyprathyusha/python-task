# 153--armstrong number
# find length of number 3
# separate each number 1,5,3
# 1 pow len of number--->1pow3+5pow3+3pow3
# sum
# check condition 

n=153
sum=0
length=len(str(n))
r=n
while n>0:
    temp=n%10
    sum+=temp**length
    n//=10
if sum==r:
    print(r,"Armstrong number")
else:
    print(r,"Not an Armstrong number")