# -*- encoding: utf-8 -*-
import re, random
from pathlib import Path
from typing import List
import pickle
import json
import torch
import numpy as np
from pprint import pprint
from icecream import ic
import os, sys, shutil
sys.path.append(os.path.abspath('.'))


def save_args(model_out_path, args):
    """
    saves args config into the model save path
    """
    os.makedirs(args.output_dir, exist_ok=True)
    file = os.path.join(model_out_path, 'args.txt')
    with open(file, 'w', encoding='utf-8') as f:
        for k, v in vars(args).items():
            f.write(f'{k}: {v}\n')

def pair(t):
    """ usage        
    image_height, image_width = pair(image_size)
    patch_height, patch_width = pair(patch_size)
    """
    return t if isinstance(t, tuple) else (t, t)            

def set_seed(seed_num):
    random.seed(seed_num)
    np.random.seed(seed_num)
    try:
        torch.manual_seed(seed_num)
        torch.cuda.manual_seed_all(seed_num)
        # Some cudnn methods can be random even after fixing the seed unless you tell it to be deterministic
        torch.backends.cudnn.deterministic = True        
    except Exception as _:
        pass