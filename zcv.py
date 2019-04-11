from math import *
def zcv(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))
    c_a=c
    A_e=B*W
    m=(2+(B/W))/(1+(B/W))
    T=Q*sin(radians(delta))
    if phi==0:
        zetaQi=1
    else:
        zetaQi=(1-T/(Q+A_e*c_a*(tan(radians(phi)))**(-1)))**m
    zetaQb=(1-tan(radians(beta)))**2
    zetaQd=(1-0.017*delta*tan(radians(phi)))**2
    #Calc N_c
    if phi==0:
        N_c=5.14
    else:
        N_c=(N_q-1)*tan(radians(phi))**(-1)
    #zcs has to be 1 if a slope factor is used zcs=0.2*B/W
    #Calc zcs
    zcs=1
    #Calc zci
    if phi==0:
        zci=(1-((m*T)/(A_e*c_a*N_c)))
    else:
        zci=(zetaQi-((1-zetaQi)/(N_c*tan(radians(phi)))))
    #Calc zcd (same for both phi conditions)
    zcd=1+0.4*D/B
    #Calc zcb
    if phi==0:
        zcb=1-(beta/147.3)
    else:
        zcb=zetaQb-(1-zetaQb)/(147.3)
    #Calc zcd2
    if phi==0:
        zcd2=1-(delta/147)
    else:
        zcd2=zetaQd-((1-zetaQd)/(147.3))
    #Calc total correction
    zc=zcs*zci*zcd*zcb*zcd2
    return N_c,zc,zcs,zci,zcd,zcb,zcd2
