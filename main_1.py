import math
class Punkt:
    def __init__(self):
        self.x=0
        self.y=0
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self,w):
        self._x=w
    @y.setter
    def y(self,w):
        self._y=w
#zaadanie 1
a=Punkt()
a.x=1
a.y=0
b=Punkt()
b.x=2
b.y=0
#zadanie 2
def zakres(x1,x2,y1,y2):
    def dec(pf):
        def fw(p1,p2):
            if(p1.x<x1 or p1.y<y1 or p1.y>x2 or p1.y>y2):
                raise ValueError
            if(p2.x<x1 or p2.y<y1 or p2.y>x2 or p2.y>y2):
                raise ValueError
            return pf(p1,p2)
        return fw
    return dec
#zadanie4
class Modulo:
    s={}
    def __init__(self,pf):
        Modulo.s[pf.__name__]=0
        self._pf=pf
    def __call__(self,*p):
        Modulo.s[self._pf.__name__]+=1
        return self._pf(*p)
    @staticmethod
    def numer():
        return Modulo.s

@zakres(0,10,0,10)
@Modulo
def dodawanie(a,b):
    tmp=Punkt()
    tmp.x=a.x+b.x
    tmp.y=a.y+b.y
    return tmp

@zakres(0,10,0,10)
def odejmowanie(a,b):
    tmp=Punkt()
    tmp.x=a.x-b.x
    tmp.y=a.y-b.y
    return tmp

try:
    wynik=dodawanie(a,b)
except ValueError as ex1:
    print("Punkty znajduja sie poza zakresem")
else:
    print(wynik.x,wynik.y)

try:
    wynik=odejmowanie(a,b)
except ValueError as ex1:
    print("Punkty znajduja sie poza zakresem")
else:
    print(wynik.x,wynik.y)


#zadanie 3
@Modulo
def odcinek(p1,p2):
    return math.sqrt(((p1.x-p2.x)**2+(p1.y-p2.y)**2))
class Figure:
    odcinki=0
    @staticmethod
    def obwod(*p):
        #i fo i in 
        #odcinek(p[i],p[i+1])
        Figure.odcinki=[odcinek(p[i],p[i+1]) for i in range(len(p)-1)]
        Figure.odcinki.append(odcinek(p[0],p[-1]))
        return sum(Figure.odcinki)
    @staticmethod
    def pole(*p):
        obw=Figure.obwod(*p)/2
        if len(p)==4:
            a=1
            for i in Figure.odcinki:
                a=a*(obw-i)
            return math.sqrt((a))
        else:
            a=obw
            for i in Figure.odcinki:
                a=a*(obw-i)
            return math.sqrt((a))

c=Punkt()
c.x=2
c.y=1
wynik.x=1
wynik.y=1
print(Figure.pole(a,b,c,wynik))
print(Modulo.numer())
#sprawdzic czy da sie wpisac w okrag?

