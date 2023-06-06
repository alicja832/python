import abc
#1 albo zagniezdzomo-zwracamy self albo zwracamy nowy obiekt
#init nie tworzy obiektu tylko new,najpierw new a pozniej init-automatem
class Iterator:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.it=min
    def __iter__(self):
        return self
    def __next__(self):
        #elementy przez ktore bedziemy dzielic,sprawdzac
        self.it+=1
        if self.it<self.max:
            k=[i for i in range(1,self.it)]
            if self.it%2!=0 and not self.it<=1:
                for i in k:
                    if not self.it%i==0:
                        return self.it
        else:
            raise StopIteration
#zadanie pierwsze spr
test=Iterator(1,10)
for i in test:
    if(i):
        print(i)
class Iteratorv2:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.it=min
    def __iter__(self):
        return Iteratorv2(self.min,self.max)
    def __next__(self):
        #elementy przez ktore bedziemy dzielic,sprawdzac
        self.it+=1
        if self.it<self.max:
            k=[i for i in range(1,self.it)]
            if self.it%2!=0 and not self.it<=1:
                for i in k:
                    if not self.it%i==0:
                        return self.it
        else:
            raise StopIteration
#zadanie pierwsze spr
test=Iteratorv2(1,10)
for i in test:
    if(i):
        print(i)

#zadanie2
class Iteratorlosowy:
    def __init__(self,m,a,min,max,n):
        self.min=min
        self.max=max
        self.m=m
        self.a=a
        self.it=0
        self.x=1
        self.n=n
        self.scalar=self.m/max
    def __iter__(self):
        return self
    def __next__(self):
        #elementy przez ktore bedziemy dzielic,sprawdzac
        self.it+=1
        s=0
        if self.it<self.n:
            self.x=(self.x*self.a)%self.m
            return self.x/self.scalar
        else:
            raise StopIteration
a=Iteratorlosowy(2**31-1,7**5,0,1,10**5)
b=Iteratorlosowy(2**31-1,7**5,0,1,10**5)
liczba=0
for i in a:
    for j in b:
        for n in range(1,11):
            if i<0.1*n and j<0.1*n:
                liczba+=1
print(liczba/(10**10)*100)#wynik w procentach


#zadanie 3
class Calka(abc.ABC):
    def __init__(self,f,min,max,n):
        self.min=min
        self.max=max
        self.n=n
        self.f=f
        "'Metoda iteracyjna'"
    @abc.abstractmethod
    def metoda(self):
        "'Metoda iteracyjna'"
class Simpson(Calka):
    def metoda(self):
        h=(self.max-self.min)/(2*n)
        f0=[self.f(self.min)]
        f1=[]
        f2=[]
        f4=[self.f(self.max)]
        i=0
        while i<2*n:
            if(i%2==0):
                f2.append(self.f(self.min+i*h))
            else:
                f1.append(self.f(self.min+i*h))
            i+=1
        s=h/3*(sum(f0)+4*sum(f1)+2*sum(f2)+sum(f4))
        "'Metoda iteracyjna'"
        return s
b=Simpson(lambda x:x,0,10,10000)
wynik=b.metoda()
print(wynik)

class MonteCarlo(Calka):
    def metoda(self):
        gener=Iteratorlosowy(2**31-1,7**5,self.min,self.max,self.n)
        k=[i for i in gener]
        t=0
        print(k)
        

b=MonteCarlo(lambda x:x,0,10,10)
b.metoda()