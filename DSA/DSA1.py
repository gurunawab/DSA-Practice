import math

def isprime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= math.sqrt(n):
        if n % i ==0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    n = 7
    if(isprime(n)):
        print("true")
    else:
        print("false")    



def sieve(n):

    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:

            for i in range(p * p, n + 1, p):
                prime[i] = False

        p += 1

    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)

    return res

if __name__ == "__main__":
  n = 35  
  res = sieve(n)
  for ele in res:
      print(ele, end=' ')     