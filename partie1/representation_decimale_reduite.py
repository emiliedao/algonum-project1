import numpy as np

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


if __name__ == "__main__":
    main()
    
