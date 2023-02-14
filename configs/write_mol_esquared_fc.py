import numpy as np
data = np.load('aspirin_ccsd-test.npz')
N = 6
Np=2
z=np.array([1 for i in range(Np)])
R = np.random.rand(N,Np,3)
R[N-1] = [[   1, 0, 0],
      [  -1, 0, 0]]
R[N-2] = [[ 1.001, 0, 0],
      [  -1, 0, 0]]
R[N-3] =  [[   1, 0, 0],
      [-0.999, 0, 0]]     
F = 2*R
E=np.empty((N,1))

FC = np.ones_like(F)

FC = FC +1

for i in range(N):
      E[i][0]=sum(R[i][0]**2)+sum(R[i][1]**2)
type=data['type']
theory=data['theory']
name=data['name']
np.savez(open('test_esq2_fc.npz','wb'),E=E,R=R,F=F,FC=FC,type=type,name=name,theory=theory,z=z)