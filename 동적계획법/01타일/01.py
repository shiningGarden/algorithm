import sys

n = int(sys.stdin.readline().strip())
temp1 = 1
temp2 = 2
for i in range(1,n+1):
    if i == 1:
        answer = temp1
    elif i == 2:
        answer = temp2
    else:
        answer = (temp1+temp2)%15746
        temp1 = temp2
        temp2 = answer

print(answer)
