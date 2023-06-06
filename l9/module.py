"'Modul z funkcjami'"
import datetime
def karta(nr):
    try:
        waga=[]
        k=[int(i) for i in nr]

    except ValueError as ex1:
        print("ValueError")
    for i in range(len(k)):
        if i%2:
            k[i]=2*k[i]
    if not len(k)==16:
        raise ValueError
    for i in range(15):
        if not i%2:
            waga.append(1)
        else:
            waga.append(2)
    waga.reverse()
    control=sum(map(lambda x,y:x*int(y),waga,k))
    if control%10:
        raise ValueError
def spr_year(year):
    s={
        1800:80,
        1900:0,
        2000:20,
        2100:40,
        2200:60
    }
    for i in s:
        if year>=i and year<(i+100):
            return s[i] 

def fun_two(pesel,data,plec):
    "'Zadanie drugie: wpisz pesel,date urodzenia, plec,'"
    dane={'kobieta':0,'mezczyzna':1}
    waga=[1,3,7,9,1,3,7,9,1,3]
    year=data.year
    day=data.day
    month=data.month
    if not int(pesel[:2])==year%100:
        raise ValueError
        return 1
    add=spr_year(year)
    if not int(pesel[2:4])==(month+add):
        raise ValueError
    if not int(pesel[4:6])==day:
        raise ValueError
    if not int(pesel[6:9])%2==dane[plec]:
        raise ValueError
    control=sum(map(lambda x,y:x*int(y),waga,pesel))
    if not int(pesel[-1])==(10-control%10)%10:
        raise ValueError
    if not len(pesel)==11:
        raise ValueError

def average(sposob):
    "'Zadanie 3, oblicza srednia wieku'"
    old=[]
    if sposob:
        with open('daty.in') as pl:
            line=pl.readline()
            while line:
                day=int(line[:2])
                month=int(line[3:5])
                year=int(line[7:11])
                if(day<datetime.date.today and month<datetime.date.month):
                    old.append(datetime.date.year-year)
                else:
                    old.append(datetime.date.year-year-1)
                line=pl.readline()
    else:
        with open('daty.in') as pl:
            s={1:31,2:0,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            line=pl.readline()
            while line:
                try:
                    day=int(line[:2])
                    month=int(line[3:5])
                    year=int(line[7:11])
                except ValueError as ex1:
                    line=pl.readline()
                    continue
                if month==2:
                    if ((not year%4) and year%100) or not year%400:
                        line=pl.readline()
                        continue
                   
                if(day<datetime.date.today().day and month<datetime.date.today().month):
                    old.append(datetime.date.today().year-year)
                else:
                    old.append(datetime.date.today().year-year-1)
                line=pl.readline()

    return sum(old)/len(old)