import re, random
from pathlib import Path
from typing import List
import pickle
import json
from pprint import pprint
from icecream import ic
import os, sys, shutil
import torch
from torch import nn, einsum
import torch.nn.functional as F
import numpy as np
sys.path.append(os.path.abspath('.'))
from einops import rearrange, repeat, reduce
from einops.layers.torch import Rearrange
import cv2
import copy
ims = cv2.imread('data/1ant.jpg', flags=1)
ims_ = copy.deepcopy(ims)
ims1 = cv2.imread('data/2bee.jpg', flags=1)
ic(type(ims.shape[:2]))
h, w = ims.shape[:2]
ic(ims.shape)
ic(ims1.shape)
ims1 = cv2.resize(ims1, (w, h))
ic(ims1.shape)
ims1_ = copy.deepcopy(ims1)
imgs = np.stack((ims, ims_, ims1, ims1_), 0)
ic(ims.shape, ims.dtype)
ic(imgs.shape)

imgs2 = repeat(ims, 'h w c -> b h w c', b=2)
ic(imgs2.shape)

out_path = 'utils/einops_out_imgs/'
Path(out_path).mkdir(exist_ok=True)



# # exchange portrait, that's h and w
# ims_exchange_h_w = rearrange(ims, 'h w c -> w h c')
# cv2.imwrite(out_path + 'ims_exchange_h_w.jpg', ims_exchange_h_w)

# ims_merge_h = rearrange(imgs, 'b h w c -> (b h) w c')
# cv2.imwrite(out_path + 'ims_merge_h.jpg', ims_merge_h)
a = torch.tensor([[11, 12], 
                [21, 22]])
b = torch.tensor([[2, 1], 
                [3, 4]])
ic(torch.einsum('ii', b))
ic(torch.einsum('ii->', b))
ic(torch.einsum('ij', b))
ic(torch.einsum('ij->', b))

# diagonal
ic(torch.einsum('ii->i', b))

ic(a.mul(b))
ic(a.mm(b))
ic(torch.einsum('ik,kj->ij', a, b))
ic(torch.einsum('ik,kj->j', a, b))

a = np.arange(60.).reshape(3,4,5)
b = np.arange(24.).reshape(4,3,2)
o = np.einsum('ijk,jil->kl', a, b)
ic(o)
ic(np.sum(a[:,:,0]*b[:,:,0].T))
ic(np.sum(b[:,:,0]*a[:,:,0].T))

a=torch.arange(6).reshape(2,3)
ic(a)

a = torch.tensor([[11, 12, 2], 
                [21, 22, 2]])
b = torch.tensor([[1, 1, 3]])
ic(torch.einsum('id,jd->ij', a, b))

if __name__ == '__main__':
    
    print(f'{__file__} ends')
