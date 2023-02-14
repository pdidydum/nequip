import numpy as np
data = np.load('aspirin_ccsd-test.npz')
N = 3
Np=2
z=np.array([1 for i in range(Np)])
E = np.random.rand(N,1)
F = np.random.rand(N,Np,3)
R = np.random.rand(N,Np,3)
type=data['type']
theory=data['theory']
name=data['name']
np.savez(open('test.npz','wb'),E=E,R=R,F=F,type=type,name=name,theory=theory,z=z)