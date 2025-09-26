class Company:
    cname="dnul"
    clocation="banglore"
    ecount=0
    def __init__(self,en,es,ej,eid):
        self.ename=en
        self.esalary=es
        self.ejob=ej
        self.eid=eid
        Company.ecount+=1
    def __del__(self):
        Company.ecount=Company.ecount-1
x=Company("arnab",30000,"datasort","ord012")
y=Company("Dn",40000,"Genai","ord21")
del y
print(Company.ecount)