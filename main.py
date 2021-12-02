import random

def create(b,low,high,i,n):
    if i<n:
        b.append(random.randint(low, high))
        create(b,low,high,i+1,n)

def found0(b,m):
        if b[m]==0:
            return mult(b,m+1,1)
        elif m==len(b)-1:
            return 'Немає нулів'
        if m < len(b):
            return found0(b,m+1)

def max(imax,nmax,a,i):
    if i>len(a)-1:
        return imax
    else:
        if a[i] > nmax:
            nmax = a[i]
            imax = i
        return max(imax,nmax, a, i + 1)

def mult(b,i,v):
    v*=b[i]
    if i==len(b)-1:
        return '1 нуль'
    if b[i+1]!=0:
        return mult(b,i+1,v)
    else:
        return 'Добуток='+str(v)

def shift(b,i,k):
    if len(b)%2==1:
        t=0
    else:
        t=-1
    if i<=len(b)//2+t and k<=len(b)//2+t:
        b[i], b[i+k] = b[i+k], b[i]
        shift(b,i+1,k+1)

def main():
    b=[]
    n = (int(input('n=')))
    low = (int(input('low=')))
    high = (int(input('high=')))
    create(b,low,high,0,n)
    print(b)
    print('N='+str(max(0, b[0], b, 0)+1))
    print(found0(b,0))
    shift(b, 1, 1)
    print(b)

if __name__=='__main__':
    main()
