from math import *
def zgh(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))
    c_a=c
    A_e=B*W
    m=(2+(B/W))/(1+(B/W))
    T=Q*tan(radians(phi))+A_e*c_a
    #Calc N_g
    if phi==0:
        N_g=0
    else:
        N_g=1.5*(N_q-1)*tan(radians(phi))
    #Calc zgs
    if phi==0:
        zgs=1
    else:
        zgs=1-0.4*(B/W)
    #Calc zgi
    if phi==0:
        zgi=1
        #cotangent of 0 is an error
        #zgi=(1-((0.7*T)/(Q+A_e*c_a*tan(radians(phi))**(-1))))**5
    else:
        zgi=(1-(((0.7-delta/450)*T)/(Q+A_e*c_a*tan(radians(phi))**(-1))))**5
    #Calc zgd is 1 for both phi conditions
    zgd=1
    #Calc zgb is the same for both phi conditions
    zgb=(1-0.5*tan(radians(beta)))**5
    #Calc zbd2
    zgd2=(e**(-0.047*delta*tan(radians(phi))))
    #Calc total correction
    zg=zgs*zgi*zgd*zgb*zgd2
    return N_g,zg,zgs,zgi,zgd,zgb,zgd2
