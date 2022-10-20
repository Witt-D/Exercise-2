def isprime(x):
    if x == 1:
        return(False)
    if x == 2:
        return(True)
    else:
        for i in range(int(x**0.5)+1,1,-1):
            if x % i == 0:
                return(False)
        return(True)
       

