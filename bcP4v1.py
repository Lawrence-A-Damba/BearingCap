from zcv import zcv
from zgv import zgv
from zqv import zqv
from zch import zch
from zgh import zgh
from zqh import zqh
from zcm import zcm
from zgm import zgm
from zqm import zqm
from math import *

# User Input File name
fileName=input('Enter file name : ')
myFile=open(str(fileName)+'.txt','a',encoding='utf-8')
# Write file name and general equation
myFile.write('\n'+str(fileName)+'.txt'+'\n\nq_u = c * N_c * \u03B6_c + \u00BD B * \u03B3\'_H * N_\u03B3 * \u03B6_\u03B3 + \u03C3\'_D * N_q * \u03B6_q\n')
# Get user input.
Q=float(input('Enter Q approx load (kips) : '))
B=float(input('\nEnter B, foundation length (ft)\nPerpendicular with slope : '))
W=float(input('\nEnter W, width of foundation (ft)\nParallel with slope : '))
D=float(input('\nEnter depth of foundation (ft) : '))
Dgwt=float(input('\nEnter D_gwt, depth below ground surface to groundwater (ft) : '))
phi=float(input('\nEnter \u00F8 : '))
beta=float(input('\nEnter \u03B2 angle (degrees) : '))
delta=float(input('\nEnter \u03B4 angle (degrees) : '))
c=float(input('\nEnter c, soil cohesion (or undrained shear strenght C_u) (ksf): '))
gs=float(input('\nEnter unit weigth of soil beneth foundation (kips/ft^3) : '))
gamma=float(input('\nEnter \u03B3\'_H, effective unit weight beneath foundation base \
within failure zone (kips/ft^3): '))

c_a=c
A_e=B*W
m=float((2+B/W)/(1+B/W))
T=float(Q*sin(radians(delta)))
H=B*tan(radians(45+(radians(phi)/2)))

sigma_D=float(input('\nEnter \u03C3\'_D, effective soil or surcharge pressure at the \
foundation depth D, \u03C3\'_D * D (ksf): '))

list=['zcv','zgv','zqv','zch','zgh','zqh','zcm','zgm','zqm']

Cor1=[zcv,zch,zcm]
Cor2=[zgv,zgh,zgm]
Cor3=[zqv,zqh,zqm]
names=['Vesic','Hansen','Meyerhof']

for i in range(0,3):
    myFile.write('\n\n\n'+str(names[i])+'\n')
    z_c=Cor1[i](Q,B,W,D,c,beta,delta,phi)
    z_g=Cor2[i](Q,B,W,D,c,beta,delta,phi)
    z_q=Cor3[i](Q,B,W,D,c,beta,delta,phi)
    # Write Q thur T
    myFile.write('\nQ = '+str('%.2f'%Q)+'\t\u00F8 = '+str('%.2f'%phi)+'\nB = '+str('%.2f'%B)+'\t\u03B2 = '+str('%.2f'%beta)+'\nW = '+str('%.2f'%W)+'\t\u03B4 = '+str('%.2f'%delta)+\
    '\nD = '+str('%.2f'%D)+'\tH = '+str('%.2f'%(H))+'\nm = '+str('%.2f'%(m))+'\tT = '+str('%.2f'%T)+'\n')
    # Write c thur zeta_q
    myFile.write('\nc = '+str('%.2f'%c)+'\t1/2B = '+str('%.2f'%(B/2))+'\t\u03C3\'_D = '+str('%.2f'%sigma_D)+'\n\t\t\u03B3\'_H = '+ str('%.2f'%(gamma))+\
    '\nN_c = '+str('%.2f'%z_c[0])+'\tN_\u03B3 = '+str('%.2f'%(z_g[0]))+'\tN_q = '+str('%.2f'%z_q[0])+'\n\u03B6_c = '+str('%.2f'%(z_c[1]))+\
    '\t\u03B6_\u03B3 = '+str('%.2f'%(z_g[1]))+'\t\u03B6_q ='+str('%.2f'%(z_q[1]))+'\n\n')
    # Write totals
    myFile.write('Total = '+str('%.2f'%(c*z_c[0]*z_c[1]))+'\tTotal = '+str('%.2f'%(0.5*B*gamma*z_g[0]*z_g[1]))+'\tTotal = '+\
    str('%.2f'%(sigma_D*z_q[0]*z_q[1]))+'\n\n')
    # Write q_u equation
    myFile.write('q_u = (c * N_c * \u03B6_c) + (\u00BD B * \u03B3\'_H * N_\u03B3 * \u03B6_\u03B3) + (\u03C3\'_D * N_q * \u03B6_q)\n')
    q_u=c*z_c[0]*z_c[1]+0.5*B*gamma*z_g[0]*z_g[1]+sigma_D*z_q[0]*z_q[1]
    myFile.write(str('%.2f'%(q_u))+' = ('+str('%.2f'%c)+' * '+str('%.2f'%z_c[0])+' * '+str('%.2f'%(z_c[1]))+') + ('+str('%.2f'%0.5)+' * '+str('%.2f'%B)+' * '+str('%.2f'%(gamma))+' * '+str('%.2f'%(z_g[0]))+\
    ' * '+str('%.2f'%(z_g[1]))+') + ('+str('%.2f'%sigma_D)+' * '+str('%.2f'%(z_q[0]))+' * '+str('%.2f'%(z_q[1]))+')\n')
    myFile.write(str('%.2f'%(q_u))+' = ('+str('%.2f'%(c * z_c[0] * z_c[1]))+') + ('+str('%.2f'%(0.5 * B * gamma * z_g[0]
    * z_g[1]))+') + ('+str('%.2f'%(sigma_D * z_q[0] *z_q[1]))+')\n\n')
    if names[i]=='Meyerhof':
        myFile.write('zc = '+str('%.2f'%(z_c[1]))+'\tzg = '+str('%.2f'%(z_g[1]))+'\tzq = '+str('%.2f'%(z_q[1]))+\
        '\n\nzcs = '+str('%.2f'%(z_c[2]))+'\tzgs = '+str('%.2f'%(z_g[2]))+'\tzqs = '+str('%.2f'%(z_q[2]))+\
        '\nzci = '+str('%.2f'%z_c[3])+'\tzgi = '+str('%.2f'%z_g[3])+'\tzqi = '+str('%.2f'%z_q[3])+\
        '\nzcd = '+str('%.2f'%(z_c[4]))+'\tzgd = '+str('%.2f'%z_g[4])+'\tzqd = '+str('%.2f'%z_q[4])+\
        '\n\n')
    else:
        myFile.write('zc = '+str('%.2f'%(z_c[1]))+'\tzg = '+str('%.2f'%(z_g[1]))+'\tzq = '+str('%.2f'%(z_q[1]))+\
        '\n\nzcs = '+str('%.2f'%(z_c[2]))+'\tzgs = '+str('%.2f'%(z_g[2]))+'\tzqs = '+str('%.2f'%(z_q[2]))+\
        '\nzci = '+str('%.2f'%z_c[3])+'\tzgi = '+str('%.2f'%z_g[3])+'\tzqi = '+str('%.2f'%z_q[3])+\
        '\nzcd = '+str('%.2f'%(z_c[4]))+'\tzgd = '+str('%.2f'%z_g[4])+'\tzqd = '+str('%.2f'%z_q[4])+\
        '\nzcb = '+str('%.2f'%(z_c[5]))+'\tzgb = '+str('%.2f'%(z_g[5]))+'\tzqb = '+str('%.2f'%(z_q[5]))+\
        '\nzcd2 = '+str('%.2f'%(z_c[6]))+'\tzgd2 = '+str('%.2f'%(z_g[6]))+'\tzqd2 = '+str('%.2f'%(z_q[6]))+'\n\n')
    q_a=q_u/3
    myFile.write(str('q_a = q_u / 3\n'))
    myFile.write(str('%.2f'%(q_a))+' = '+str('%.2f'%(q_u))+ '/ 3\n')
    myFile.write('\nT = '+str('%.2f'%T)+'\t Tsliding = '+str('%.2f'%float(Q*tan(radians(phi))+A_e*c_a)))
myFile.close()
