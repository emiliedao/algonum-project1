import numpy as np
import matplotlib.pyplot as mp


MAX_ITE = 1000


def rp(x, p):
    """ Calcule la representation decimale reduite d'un nombre
    Param : x : float, p : int
    Return : la representation decimale reduite de x avec p decimales
             (nb de chiffres significatifs)
    """
    # Cas particulier
    if (x == 0):
        return 0

    # Necessaire dans le cas de flottants negatifs (pour appliquer le log)
    y = abs(x)

    val = int(np.log10(y))

    # y >= 1
    if (val >= 0):
        val = val + 1 # val = nombre de chiffres significatifs avant la virgule
        
    # else 0 < y < 1
    # -val = nombre de 0 non representatifs apres la virgule
    
    return round(x, p - val)


def addition_rp(x, y, p):
    return rp(rp(x, p) + rp(y, p), p)


def multiplication_rp(x, y, p):
    return rp(rp(x, p) * rp(y, p), p)


def delta_add(x, y, p):
    reel = x + y
    machine = addition_rp(x, y ,p)

    return abs(reel - machine) / abs(machine)


def delta_mul(x, y, p):
    reel = x * y
    machine = multiplication_rp(x, y ,p)

    return abs(reel - machine) / abs(machine)


def afficher_delta(x, p):
    abs_array = np.arange(0, 5, 0.01)
    ord_delta_add = [delta_add(x, y, p) for y in abs_array]
    ord_delta_mul = [delta_mul(x, y, p) for y in abs_array]
    
    mp.plot(abs_array, ord_delta_add, linewidth=1.0)
    mp.plot(abs_array, ord_delta_mul, linewidth=1.0, color='r')

    mp.xlabel("y")
    mp.ylabel("delta")
    mp.legend(["delta_add", "delta_mul"])
    mp.title("Erreurs relatives de l'addition et la multiplication pour x = " + str(x))
    mp.show()


def log_2_v1(p):
    res = 0
    
    for i in range(1, MAX_ITE):
        tmp = (-1)**(i + 1) / float(i)
        res = addition_rp(res, tmp, p)

    return res


def log_2_v2(p):
    res = 0
    
    for i in range(MAX_ITE, 0, -1):
        tmp = (-1)**(i + 1) / float(i)
        res = addition_rp(res, tmp, p)

    return res       
        

def main():
    x = 3.141592658
    y = 10507.1823
    z = 0.0001857563
    
    print "Test de la fonction rp sur la batterie de test fournie\n"
    print "________________________________________________________"
    print ("Nombre reel\tSur 4 decimales\tSur 6 decimales").expandtabs(20)
    print (str(x) + "\t" + str(rp(x, 4)) + "\t" + str(rp(x,6))).expandtabs(20)
    print (str(y) + "\t" + str(rp(y, 4)) + "\t" + str(rp(y,6))).expandtabs(20)
    print (str(z) + "\t" + str(rp(z, 4)) + "\t" + str(rp(z,6))).expandtabs(20)
    print (str(-x) + "\t" + str(rp(-x, 4)) + "\t" + str(rp(-x,6))).expandtabs(20)

    # afficher_delta(10**(-4)/2, 5)
    # vals pertinentes : 10**(-4), 0.0001857563
    # 10**(-4)/2
    # Precision machine limitee : 10**(-p + 1) / 2


if __name__ == "__main__":
    main()


# Comprehension de liste
    
