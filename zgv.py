from math import *
def zgv(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))
    c_a=c
    A_e=B*W
    m=(2+(B/W))/(1+(B/W))
    T=Q*tan(radians(phi))+A_e*c_a
    #Calc N_g
    if phi==0:
        if beta==0:
            N_g=0
        else:
            N_g=-2*sin(beta)
    else:
        N_g=2*(N_q)*tan(phi)
    #Calc zgs
    if phi==0:
        zgs=1
    else:
        zgs=1-0.4*(B/W)
    #Calc zgi
    if phi==0:
        zgi=1
    else:
        zgi=(1-(T/(Q+A_e*c_a*(tan(radians(phi))**(-1)))))**(m+1)
    #Calc zgd is 1 for both phi conditions
    zgd=1
    #Calc zgb is the same for both phi conditions
    zgb=pow(1-(tan(radians(beta))),2)
    #Calc zbd2 is the same for both phi conditions
    zgd2=pow(1-0.017*delta*(tan(radians(phi))),2)
    #Calc total correction
    zg=zgs*zgi*zgd*zgb*zgd2
    return N_g,zg,zgs,zgi,zgd,zgb,zgd2
