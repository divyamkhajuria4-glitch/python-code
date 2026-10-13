t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    both = [ ]
    only2 = [ ]
    only3 = [ ]
    neither = [ ]

    for x in a:

        # is divisible by both 2 anfd 3
        if x % 6 == 0:
            both.append(x)

        #x is divisible  by 2 only:
        elif x % 2 == 0:
            only2.append(x)  

        #x is divisible by 3 only:
        elif x % 3 == 0:
            only3.append(x)

        ##Divisible by neither 
        else:
            neither.append(x)

    answer = both + only2 + neither + only3

    print(*answer)            
