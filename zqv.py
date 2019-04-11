from math import *
def zqv(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))
    c_a=c
    A_e=B*W
    m=(2+(B/W))/(1+(B/W))
    T=Q*tan(radians(phi))+A_e*c_a
    if D/B<=1:
        k=D/B
    else:
        k=atan(radians(D/B))
    #Calc N_q
    if phi==0:
        N_q=1
    else:
        N_q=N_phi*(e)**(pi*tan(radians(phi)))
    #Calc zqs
    if phi==0:
        zqs=1
    else:
        zqs=1+B/W
    #Calc zqi
    if phi==0:
        zqi=1
    else:
        zqi=(1-((T)/(Q+A_e*c_a*((tan(radians(phi))**(-1))))))**m
    #Calc zqd
    if phi==0:
        zqd=1
    else:
        zqd=(1+(2*tan(radians(phi))*(1-sin(radians(phi))**2))*k)
    #Calc zqb same for both cases of phi
    zqb=pow(1-tan(radians(beta)),2)
    #Calc zqd2 same for both cases of phi
    zqd2=pow((1-0.017*delta*tan(radians(phi))),2)
    #Calc total correction
    zq=zqs*zqi*zqd*zqb*zqd2
    return N_q,zq,zqs,zqi,zqd,zqb,zqd2
