N = input()

count = 0
i = 0
while i <2:
    print(N)
    if len(N) < 2:
        N = N+'0'
    
    first = int(N[0]) + int(N[1])
    first = str(first)
    
    second = N[-1] + first[-1]

    N = second


    i+=1
