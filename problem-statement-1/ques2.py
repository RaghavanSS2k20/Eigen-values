n=int(input())

from functools import reduce


 

def factors(n):

    return list(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

k=factors(n)

count=0

for a in list(range(len(k)-1))[::2]:

    if (k[a]+k[a+1])%2==0:

        count=count+1

print(count)
