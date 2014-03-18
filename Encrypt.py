import sys
rl = lambda:sys.stdin.readline()
n = int(rl())
result = []
for i in range(n):
    s1 = ''
    s2 = ''
    inputS = str(rl())
    for i in range(len(inputS)):
        if(i%2 == 0) :
            s1 += inputS[i]
        else :
            s2 += inputS[i]
    result.append(s1.strip()+s2.strip())

for s in result:
    print(s)
