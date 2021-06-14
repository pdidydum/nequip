from ase import Atoms, Atom
from ase.visualize import view

import warnings
from copy import deepcopy
from typing import Union, Tuple, Dict, Optional
from collections.abc import Mapping

import numpy as np
import ase.neighborlist
from ase.calculators.singlepoint import SinglePointCalculator, SinglePointDFTCalculator

import torch
from torch_geometric.data import Data
import e3nn.o3

# --- Tutorial --- #
# d = 1.208
# o2 = Atoms([Atom("O", [0, 0, 0]),
#             Atom("C", [0, 0, d])],
#            cell=[(3, 0, 0),
#                  (0, 7.5, 0),
#                  (0, 0, 8)])
# o2.set_pbc((True, True, True))
# view(o2)

# --- PyTorch testing --- #
# a = torch.randn(2, 3)
# a_list = a.tolist()
# print(a_list)
# print(a_list[0])

aspirin_atoms = [6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 6, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1]

pos = np.array([[1.9351, -1.3223, -0.2434],
                [1.1050,  1.1607, -1.2501],
                [2.7351, -0.6791, -1.2130],
                [2.3617,  0.5501, -1.6917],
                [-3.2277,  1.4643,  0.4005],
                [0.7966, -0.7842,  0.2737],
                [0.3291,  0.4374, -0.3489],
                [-1.1688, -1.4345,  1.3998],
                [-1.8708,  1.9584, -1.4831],
                [0.9033, -2.2319,  2.1187],
                [0.0525, -1.4987,  1.3657],
                [-1.9753,  1.5393, -0.3593],
                [-0.9103,  0.9451,  0.2944],
                [0.4981, -2.5795,  2.9364],
                [2.3691, -2.2767,  0.1016],
                [0.7304,  2.1011, -1.6379],
                [3.7474, -1.1822, -1.3683],
                [2.8886,  1.2051, -2.3682],
                [-4.1139,  1.2818, -0.3308],
                [-3.2100,  0.7930,  1.2202],
                [-3.5192,  2.4355,  0.9832]])

positions = torch.tensor(pos).tolist()
batches = torch.tensor([0], dtype=torch.int32).tolist()
atomic_nums = torch.tensor(aspirin_atoms).tolist()
pbc = torch.tensor([[False, False, False]]).numpy()
cell = torch.tensor([[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]).numpy()

unique_batches = list(set(batches)) if batches is not None else [0]

num_atoms = int(len(positions) / len(unique_batches))
batch_atoms = []

for batch in unique_batches:
    atoms = []
    for i in range(num_atoms):
        atom_index = batch * num_atoms + i
        atoms.append(Atom(atomic_nums[atom_index], position=positions[atom_index]))
    mol = Atoms(atoms, cell=cell[batch], pbc=pbc[batch])
    batch_atoms.append(mol)

view(batch_atoms[0])
