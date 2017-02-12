import numpy as np
import matplotlib.pyplot as p

global pi
pi = np.pi

L = [np.log(1 + 10**(-k)) for k in range(7)]

#retourne i tel que 1 <= x*10**(-i) < 10
def red_ln(x):
    i=0
    if(x < 1):
        while x<1:
            x=x*10
            i=i-1
    else:
        while x>=10:
            x=x/10
            i=i+1
    return(i)

def my_ln(x):
    n = red_ln(x)
    xprime = x * 10**(-n)
    y = 0
    p = 1
    for k in range(7):
        while(xprime >= p + p*10**(-k)):
            y = y + L[k]
            p = p + p*10**(-k)
    return((y + xprime/p - 1) + n*np.log(10))

#retourne i tel que 0 <= x - i*ln(10) < ln(10)
def red_exp(x):
    i=0
    if(x>0):
        while(x-i*np.log(10) >= np.log(10)):
            i += 1
    else:
        while(x-i*np.log(10) < 0):
            i -= 1
    return(i)

def my_exp(x):
    n = red_exp(x)
    xprime = x - n*np.log(10)
    y = 1
    for k in range(7):
        while(xprime >= L[k]):
            xprime = xprime - L[k]
            y = y + y*10**(-k)
    return((y + y*xprime) * 10**(n))

A = [np.arctan(10**(-k)) for k in range(5)]
 
def my_arctan(x):
    if(x == 1):
        return pi/4
    if(x < 0):
        return -my_arctan(-x)
    if(x > 1):
        return (pi / 2) - my_arctan(1.0/x)
    
    k = 0
    y = 1
    r = 0
    while(k < 4):
        while((x < y*10**(-k)) and (k < 4)):
            k = k + 1        
        xp = x - y*10**(-k)
        y = y + x*10**(-k)
        x = xp
        r = r + A[k]

    return(r + x/y)

def my_tan(x):
    x = x % pi
    if(x > pi/2):
        return(-my_tan(pi - x))
    if(x > pi/4):
        return(1/my_tan(pi/2 - x))
    
    k = 0
    n = 0
    d = 1
    for k in range(5):
        while(x >= A[k]):
            x = x - A[k]
            np = n + d*10**(-k)
            d = d - n*10**(-k)
            n = np
        k = k + 1
    return((n + x*d)/(d - x*n))

def test_ln():
    nb_point = 1000
    x = [(n/100) for n in range(1, 2*nb_point)]
    c = [abs((my_ln(n) - np.log(n))/np.log(n)) for n in x]

    p.plot(x, c, linewidth=1.0)
    p.xlabel('Abscisse')
    p.ylabel('Ordonnee')
    p.title('ln : erreur relative')
    p.show()

def test_exp():
    nb_point = 1000
    x = [(n/100) for n in range(-nb_point, nb_point)]
    c = [abs((my_exp(n) - np.exp(n))/np.exp(n)) for n in x]

    p.plot(x, c, linewidth=1.0)
    p.xlabel('Abscisse')
    p.ylabel('Ordonnee')
    p.title('exp : erreur relative')
    p.show()

def test_arctan():
    nb_point = 1000
    x = [(n/100) for n in range(-nb_point, nb_point)]
    c = [abs((my_arctan(n) - np.arctan(n))/np.arctan(n)) for n in x]

    p.plot(x, c, linewidth=1.0)
    p.xlabel('Abscisse')
    p.ylabel('Ordonnee')
    p.title('arctan : erreur relative')
    p.show()

def test_tan():
    nb_point = 1000
    x = [(n/100) for n in range(-nb_point, nb_point)]
    c = [abs((my_tan(n) - np.tan(n))/np.tan(n)) for n in x]

    p.plot(x, c, linewidth=1.0)
    p.xlabel('Abscisse')
    p.ylabel('Ordonnee')
    p.title('tan : erreur relative')
    p.show()

#TESTS : affiche les erreurs relatives pour chaque fonction
#test_ln()
#test_exp()
#test_arctan()
#test_tan()
