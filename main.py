def sayilar(sayi):
    if (sayi==0):
        return  " "
    elif (sayi==1):
        return "bir"
    elif (sayi==2):
        return "iki"
    elif (sayi==3):
        return "üç"
    elif (sayi==4):
        return "dört"
    elif (sayi==5):
        return "beş"
    elif (sayi==6):
        return "alti"
    elif (sayi==7):
        return "yedi"
    elif (sayi==8):
        return "sekiz"
    elif (sayi==9):
        return "dokuz"
    else:
        return ''

def on(sayi):
    if (sayi == 0):
        return " "
    elif (sayi == 1):
        return "on"
    elif (sayi == 2):
        return "yirmi"
    elif (sayi == 3):
        return "otuz"
    elif (sayi == 4):
        return "kirk"
    elif (sayi == 5):
        return "elli"
    elif (sayi == 6):
        return "altmis"
    elif (sayi == 7):
        return "yetmis"
    elif (sayi == 8):
        return "seksen"
    elif (sayi == 9):
        return "doksan"
    else:
        return ''




sayi=float(input("sayı giriniz"))

tam_kisim=round(sayi)-1

a= sayi % 10
b= ((sayi-a) /10) %10
c=sayi %100
d=((sayi-c)/100) %10
e= sayi %1000
f= ((sayi-e)/1000) %10
g=sayi %10000
h=((sayi-g)/10000) %10
i=sayi%100000
j=((sayi-i)/100000) %10


ondalikli_kisim= (sayi-tam_kisim)*100

k=ondalikli_kisim %10
l=((ondalikli_kisim-d) /10) %10


if (j==0):
    jj = ''
elif (j == 1):
    jj = 'yüz'
else:
    jj = sayilar(j) + 'yüz'

hh = on(h)

if (f == 0 and (j != 0 or h != 0)) :
    ff = 'bin'
elif (f == 0 and j == 0 and h == 0 ):
    ff = ''
else:
    ff = sayilar(f) + 'bin'

if (d==0):
    dd = ''
elif (d == 1):
    dd = 'yüz'
else:
    dd = sayilar(d) + 'yüz'

bb = on(b)

if(a==0 and (j!=0 or h!=0 or f!=0 or d!=0 or b!=0)):
    aa=''
elif(a==0 and j==0 and h==0 and f==0 and d==0 and b==0):
    aa='sıfır'
else:
    aa=sayilar(a)

ll= on(l)
if(k==0 and l!=0):
    kk=''
elif(k==0 and l==0):
    kk='sıfır'
else:
    kk=sayilar(l)



print(jj+hh+ff+dd+bb+aa+"lira" + ll+kk+"kuruş")

