import math
import numpy as np

def mySine(x):
    #handle case where angle is too large
    if(abs(x) > 10**9):
        return float('nan')
    
    #handle case where angle is less than system epsilon
    if(x**2 <= np.finfo(float).eps):
        return x

    #reduce the input so its in the range [-pi/2, pi/2]
    x = x % (2 * math.pi)

    if(x > math.pi):
        x -= 2 * math.pi
    
    if(x > math.pi / 2):
        x = math.pi - x
    elif(x < -math.pi / 2):
        x = -math.pi - x
    
    result = 0
    for i in range(11):
        term = ((-1)**i) * (x**(2 * i+1)) / math.factorial(2 * i+1)
        result += term

    return result

if __name__ == '__main__':
    print(mySine(1.0e-08))      #1e-08
    print(mySine(0.00001))      #9.999999999833334e-06
    print(mySine(0))            #0
    print(mySine(math.pi/2))    #1.0000000000000002
    print(mySine(math.pi))      #-0.0
    print(mySine(100))          #-0.5063656411097555
    print(mySine(-1000))        #-0.8268795405320125
    print(mySine(999999999))    #-0.4101372630100049
    print(mySine(-1000000001))  #nan