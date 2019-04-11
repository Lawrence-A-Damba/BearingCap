from math import *
def zch(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))
    c_a=c
    A_e=B*W
    #m=(2+(B/W))/(1+(B/W))
    T=Q*tan(radians(phi))+A_e*c_a
    if D/B<=1:
        k=D/B
    else:
        k=atan(radians(D/B))
    if phi==0:
        zetaQi=1
    else:
        zetaQi=(1-((0.5*T)/(Q+A_e*c_a*(tan(radians(phi))))))**(5)
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
    if phi==0:
        zci=(1-(1-(T/(A_e*c_a))**0.5))/2
    else:
        zci=(zetaQi-((1-zetaQi)/(N_q-1)))
    #Calc zcd
    if k==0:
        zcd=1
    else:
        if phi==0:
            zcd=0.4*k
        else:
            zcd=1+0.4*k
    #Calc zcb
    if phi==0:
        zcb=1-(beta/147.3)
    else:
        zcb=zetaQb-((1-zetaQb)/(147.3))
    #Calc zcd2
    if phi==0:
        zcd2=1-(delta/147)
    else:
        zcd2=zetaQd-((1-zetaQd)/(147.3))
    #Calc total correction
    zc=zcs*zci*zcd*zcb*zcd2
    return N_c,zc,zcs,zci,zcd,zcb,zcd2
