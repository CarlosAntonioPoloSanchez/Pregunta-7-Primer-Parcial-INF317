from multiprocessing import Pool

def pi(n):
    s=1
    if((str(n)[len(str(n))-1]=="3" or str(n)[len(str(n))-1]=="7")and (n<10 or int(str(n)[len(str(n))-2])%2==0)):
        s=-1
    if((str(n)[len(str(n))-1]=="1" or str(n)[len(str(n))-1]=="5" or str(n)[len(str(n))-1]=="9")and(n>10 and int(str(n)[len(str(n))-2])%2!=0)):
        s=-1
    
    if(n % 2 == 0):
        return 0
    else:
        return s*4/n

if __name__ == '__main__':
    print("ingrese precision")
    a=int(input())
    b=[]
    for i in range(1,a+1):
        b.append(i)
    x=(Pool().map(pi,b))
    y=0
    for i in x:
        y=y+i
    print(y)