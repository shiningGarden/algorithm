import sys
waveList = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    default = 9
    if n <= 10:
        print(waveList[n-1])
    else:
        temp1,temp2,answer = waveList[-3], waveList[-2], waveList[-1]
        while True:

            if default+1 == n:
                print(answer)
                break
            temp = temp1+temp2
            temp1= temp2
            temp2 = answer
            answer = temp
            default+=1
