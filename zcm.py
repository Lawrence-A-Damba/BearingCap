from math import *
def zcm(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))

    #Calc N_c
    if phi==0:
        N_c=5.14
    else:
        N_c=(N_q-1)*tan(radians(phi))**(-1)
    #zcs has to be 1 if a slope factor is used zcs=0.2*B/W
    #Calc zcs
    zcs=1
    if phi==0:
        zci=(1-beta/90)
    else:
        zci=(1-beta/90)**2
    #Calc zcd same for both cases of phi
    zcd=1+0.2*N_phi**(1/2)*(D/B)

    #Calc total correction
    zc=zcs*zci*zcd
    return N_c,zc,zcs,zci,zcd
