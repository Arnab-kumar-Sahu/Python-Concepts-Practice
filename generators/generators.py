def genfibo(FE,SE,n):
    while n>0:
        yield FE
        n=n-1
        FE,SE=SE,FE+SE
GFIO=genfibo(2,3,10)
for i in GFIO:
    print(i)