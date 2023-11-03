# -*- encoding: utf-8 -*-
import re, random
from pathlib import Path
from typing import List
import pickle
import json
from pprint import pprint
import unicodedata

import os, sys, shutil
BASE_DIR =  os.path.abspath('.')
sys.path.append(BASE_DIR)

# Turn a Unicode string to plain ASCII, thanks to
# https://stackoverflow.com/a/518232/2809427
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

# Lowercase, trim, and remove non-letter characters
# 句子标准化，所谓标准化，指的是：大写转小写，标点分离
def normalize_string_basic(s):
    s = unicodeToAscii(s.lower().strip())
    # the re.sub(r"([().!?])", r" \1", s) the () in the first variable is relative to the second variable \1 
    s = re.sub(r"([().!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s

# Lowercase, trim, and remove non-letter characters
# 句子标准化：大写转小写，拼写标准化，标点分离，拼写纠错
def normalize_string(s:str):
    s = unicodeToAscii(s.lower().strip())

    s = re.sub(r"what's", "what is", s)
    s = re.sub(r"who's", "who is", s)
    s = re.sub(r"where's", "where is", s)
    s = re.sub(r"when's", "when is", s)
    s = re.sub(r"how's", "how is", s)
    s = re.sub(r"it's", "it is", s)
    s = re.sub(r"he's", "he is", s)
    s = re.sub(r"she's", "she is", s)
    s = re.sub(r"that's", "that is", s)
    s = re.sub(r"there's", "there is", s)
    s = re.sub(r"\'s", " ", s)  # 除了上面的特殊情况外，“\'s”只能表示所有格，应替换成“ ”
    s = re.sub(r"\'ve", " have ", s)
    s = re.sub(r"can't", "can not ", s)
    s = re.sub(r"n't", " not ", s)
    s = re.sub(r"i'm", "i am", s)
    s = re.sub(r" m ", " am ", s)
    s = re.sub(r"\'re", " are ", s)
    s = re.sub(r"\'d", " would ", s)
    s = re.sub(r"\'ll", " will ", s)
    s = re.sub(r" e g ", " eg ", s)
    s = re.sub(r" b g ", " bg ", s)
    s = re.sub(r" 9 11 ", "911", s)
    s = re.sub(r"e-mail", "email", s)
    s = re.sub(r"quikly", "quickly", s)
    s = re.sub(r" usa ", " america ", s)
    s = re.sub(r" u s ", " america ", s)
    s = re.sub(r" uk ", " england ", s)
    s = re.sub(r"imrovement", "improvement", s)
    s = re.sub(r"intially", "initially", s)
    s = re.sub(r" dms ", "direct messages ", s)  
    s = re.sub(r"demonitization", "demonetization", s) 
    s = re.sub(r"actived", "active", s)
    s = re.sub(r"kms", " kilometers ", s)
    s = re.sub(r" cs ", " computer science ", s)
    s = re.sub(r" ds ", " data science ", s)
    s = re.sub(r" ee ", " electronic engineering ", s)
    s = re.sub(r" upvotes ", " up votes ", s)
    s = re.sub(r" iphone ", " phone ", s)
    s = re.sub(r"calender", "calendar", s)
    s = re.sub(r"ios", "operating system", s)
    s = re.sub(r"programing", "programming", s)
    s = re.sub(r"bestfriend", "best friend", s)
    s = re.sub(r"III", "3", s) 
    s = re.sub(r"II", "3", s) 
    s = re.sub(r"the us", "america", s)
    s = re.sub(r"(\d+)(k)", r"\g<1>000", s)

    s = re.sub(r"([.,!?%/]+)", r" \1 ", s)
    s = re.sub(r"[^a-zA-Z0-9.,!?%/]+", " ", s)
    s = re.sub(r"\s{2,}", " ", s)
    
    """ Fix misspelled words
Here we are not actually building any complex function to correct the misspelled words but just checking that each 
character should occur not more than 2 times in every word. It’s a very basic misspelling check. """
    s = ''.join(''.join(s)[:2] for _, s in itertools.groupby(s))
    return s


if __name__ == '__main__':
    
    s = 'a()dfc(acd?e.!'
    print(normalizeString(s))
    print()
