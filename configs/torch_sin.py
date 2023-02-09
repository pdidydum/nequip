import torch
import numpy as np

x = torch.rand(100)

W = torch.rand(2,10)

b_1 = torch.rand(1,10)
b_2 = torch.rand(1,10)

y = np.sin(x)

y_1 = []

for i in x:
    print(i)
