def singletuonclass(func):
    l=[]
    def inner():
        if l==[]:
            mco=func()
            l.append(mco)
        return l[0]
    return inner
@singletuonclass
class movie:
    def __init__(self):
        self.avt=200
    def bookticket(self,nt):
        if nt<self.avt:
            self.avt-=nt
            print("ticket booking successful")
        else:
            print("ticket booking unsuccessful")
            print(F"only {self.avt}  tickets available")
arnab=movie()
arnab.bookticket(100)
ankita=movie()
ankita.bookticket(50)
arab=movie()
arab.bookticket(100)