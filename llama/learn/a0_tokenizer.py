from pathlib import Path
import pandas as pd
import numpy as np
from pandas import DataFrame
import os, sys, shutil, logging, json
import re, random, math
from icecream import ic
ic.configureOutput(includeContext=True, argToStringFunction=lambda _: str(_))
ic.lineWrapWidth = 120
sys.path.append(os.path.abspath('.'))
from collections import defaultdict
from utils.log_util import logger
from utils.file_util import FileUtil
from tqdm import tqdm
from llama.tokenizer import Tokenizer
from sentencepiece import SentencePieceProcessor

SEED = 0
random.seed(SEED)
np.random.seed(SEED)

model_path = '/mnt/nas1/models/llama/pretrained_weights/tokenizer.model'
sp_model = SentencePieceProcessor(model_file=model_path)
s = 'This is 过 tes, no!'
r = sp_model.encode(s, out_type=str)
print(r)
r = sp_model.encode(s, out_type=int)
print(r)