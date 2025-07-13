#6c2=(6*5*4*3*2*1)/(2*1)(4*3*2*1)
#6c2=6!/(2!*(6-2)!)
#6c2=6*5/2*1--1
def nCrCal(n,c):
#from 1
    res=1
    for i in range(c):
        res=res*(n-i)
        res=res/(i+1)
    return res
print(nCrCal(6,2))