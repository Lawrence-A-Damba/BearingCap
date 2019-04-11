from math import *
def zqm(Q,B,W,D,c,beta,delta,phi):
    N_phi=(tan(radians(45+phi/2)))**2
    N_q=N_phi*(e)**(pi*tan(radians(phi)))


    #Calc N_g
    if phi==0:
        N_g=0
    else:
        N_g=(N_phi)*e**(pi*tan(radians(phi)))
    #Calc zqs
    if phi<=0:
        zqs=1
    else:
        zqs=1+0.1*N_phi*(B/W)
    #Calc zqi
    if phi==0:
        zqi=(1-beta/90)
    else:
        zqi=(1-beta/90)**2
    #Calc zqd is 1 for both phi conditions
    if phi==0:
        zqd=1
    else:
        zqd=1+0.1*N_phi**(1/2)*(D/B)
    #Calc total correction
    zq=zqs*zqi*zqd
    return N_g,zq,zqs,zqi,zqd
