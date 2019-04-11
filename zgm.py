from math import *
def zgm(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))


    #Calc N_g
    if phi==0:
        N_g=0
    else:
        N_g=(N_q-1)*tan(radians(1.4*phi))
    #Calc zgs
    if phi<=0:
        zgs=1
    else:
        zgs=1-0.4*(B/W)
    #Calc zgi
    if phi==0:
        zgi=1
    else:
        if beta<=phi:
            zgi=(1-beta/phi)**2
        else:
            zgi=0
    #Calc zgd is 1 for both phi conditions
    if phi==0:
        zgd=1
    else:
        zgd=1+0.1*N_phi**(1/2)*(D/B)
    #Calc total correction
    zg=zgs*zgi*zgd
    return N_g,zg,zgs,zgi,zgd
