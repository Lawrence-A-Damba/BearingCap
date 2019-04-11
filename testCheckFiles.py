import math
from zcv import *
from zgv import *
from zqv import *
from zch import *
from zgh import *
from zqh import *
from zcm import *
from zgm import *
from zqm import *

zCv=zcv(0.1,10,6,0,0.6,14,14,0)
print('\nVesic Phi=0\n')
print('N_c= '+str(zCv[0])+'\nzc= '+str(zCv[1])+'\nzcs= '+str(zCv[2])+'\nzci= '+str(zCv[3])+'\nzcd= '+str(zCv[4])+'\nzcb= '+str(zCv[5])+'\nzcd2= '+str(zCv[6])+'\n')
zGv=zgv(0.1,10,6,0,0.6,14,14,0)
print('N_g= '+str(zGv[0])+'\nzg= '+str(zGv[1])+'\nzgs= '+str(zGv[2])+'\nzgi= '+str(zGv[3])+'\nzgd= '+str(zGv[4])+'\nzgb= '+str(zGv[5])+'\nzgd2= '+str(zGv[6])+'\n')
zQv=zqv(0.1,10,6,0,0.6,14,14,0)
print('N_q= '+str(zQv[0])+'\nzq= '+str(zQv[1])+'\nzqs= '+str(zQv[2])+'\nzqi= '+str(zQv[3])+'\nzqd= '+str(zQv[4])+'\nzqb= '+str(zQv[5])+'\nzqd2= '+str(zQv[6])+'\n')


zCh=zch(0.1,10,6,0,0.6,14,14,0)
print('\nHansen Phi=0\n')
print('N_c= '+str(zCh[0])+'\nzc= '+str(zCh[1])+'\nzcs= '+str(zCh[2])+'\nzci= '+str(zCh[3])+'\nzcd= '+str(zCh[4])+'\nzcb= '+str(zCh[5])+'\nzcd2= '+str(zCh[6])+'\n')
zGh=zgh(0.1,10,6,0,0.6,14,14,0)
print('N_g= '+str(zGh[0])+'\nzg= '+str(zGh[1])+'\nzgs= '+str(zGh[2])+'\nzgi= '+str(zGh[3])+'\nzgd= '+str(zGh[4])+'\nzgb= '+str(zGh[5])+'\nzgd2= '+str(zGh[6])+'\n')
zQh=zqh(0.1,10,6,0,0.6,14,14,0)
print('N_q= '+str(zQh[0])+'\nzq= '+str(zQh[1])+'\nzqs= '+str(zQh[2])+'\nzqi= '+str(zQh[3])+'\nzqd= '+str(zQh[4])+'\nzqb= '+str(zQh[5])+'\nzqd2= '+str(zQh[6])+'\n')


zCm=zcm(0.1,10,6,0,0.6,14,14,0)
print('\nMeyerhof Phi=0\n')
print('N_c= '+str(zCm[0])+'\nzc= '+str(zCm[1])+'\nzcs= '+str(zCm[2])+'\nzci= '+str(zCm[3])+'\nzcd= '+str(zCm[4])+'\n')
zGm=zgm(0.1,10,6,0,0.6,14,14,0)
print('N_g= '+str(zGm[0])+'\nzg= '+str(zGm[1])+'\nzgs= '+str(zGm[2])+'\nzgi= '+str(zGm[3])+'\nzgd= '+str(zGm[4])+'\n')
zQm=zqm(0.1,10,6,0,0.6,14,14,0)
print('N_q= '+str(zQm[0])+'\nzq= '+str(zQm[1])+'\nzqs= '+str(zQm[2])+'\nzqi= '+str(zQm[3])+'\nzqd= '+str(zQm[4])+'\n')


zCv=zcv(0.1,10,6,0,0.6,14,14,30)
print('\nVesic Phi=30\n')
print('N_c= '+str(zCv[0])+'\nzc= '+str(zCv[1])+'\nzcs= '+str(zCv[2])+'\nzci= '+str(zCv[3])+'\nzcd= '+str(zCv[4])+'\nzcb= '+str(zCv[5])+'\nzcd2= '+str(zCv[6])+'\n')
zGv=zgv(0.1,10,6,0,0.6,14,14,30)
print('N_g= '+str(zGv[0])+'\nzg= '+str(zGv[1])+'\nzgs= '+str(zGv[2])+'\nzgi= '+str(zGv[3])+'\nzgd= '+str(zGv[4])+'\nzgb= '+str(zGv[5])+'\nzgd2= '+str(zGv[6])+'\n')
zQv=zqv(0.1,10,6,0,0.6,14,14,30)
print('N_q= '+str(zQv[0])+'\nzq= '+str(zQv[1])+'\nzqs= '+str(zQv[2])+'\nzqi= '+str(zQv[3])+'\nzqd= '+str(zQv[4])+'\nzqb= '+str(zQv[5])+'\nzqd2= '+str(zQv[6])+'\n')

zCh=zch(0.1,10,6,0,0.6,14,14,30)
print('\nHansen Phi=30\n')
print('N_c= '+str(zCh[0])+'\nzc= '+str(zCh[1])+'\nzcs= '+str(zCh[2])+'\nzci= '+str(zCh[3])+'\nzcd= '+str(zCh[4])+'\nzcb= '+str(zCh[5])+'\nzcd2= '+str(zCh[6])+'\n')
zGh=zgh(0.1,10,6,0,0.6,14,14,30)
print('N_g= '+str(zGh[0])+'\nzg= '+str(zGh[1])+'\nzgs= '+str(zGh[2])+'\nzgi= '+str(zGh[3])+'\nzgd= '+str(zGh[4])+'\nzgb= '+str(zGh[5])+'\nzgd2= '+str(zGh[6])+'\n')
zQh=zqh(0.1,10,6,0,0.6,14,14,30)
print('N_q= '+str(zQh[0])+'\nzq= '+str(zQh[1])+'\nzqs= '+str(zQh[2])+'\nzqi= '+str(zQh[3])+'\nzqd= '+str(zQh[4])+'\nzqb= '+str(zQh[5])+'\nzqd2= '+str(zQh[6])+'\n')

zCm=zcm(0.1,10,6,0,0.6,14,14,30)
print('\nMeyerhof Phi=30\n')
print('N_c= '+str(zCm[0])+'\nzc= '+str(zCm[1])+'\nzcs= '+str(zCm[2])+'\nzci= '+str(zCm[3])+'\nzcd= '+str(zCm[4])+'\n')
zGm=zgm(0.1,10,6,0,0.6,14,14,30)
print('N_g= '+str(zGm[0])+'\nzg= '+str(zGm[1])+'\nzgs= '+str(zGm[2])+'\nzgi= '+str(zGm[3])+'\nzgd= '+str(zGm[4])+'\n')
zQm=zqm(0.1,10,6,0,0.6,14,14,30)
print('N_q= '+str(zQm[0])+'\nzq= '+str(zQm[1])+'\nzqs= '+str(zQm[2])+'\nzqi= '+str(zQm[3])+'\nzqd= '+str(zQm[4])+'\n')

