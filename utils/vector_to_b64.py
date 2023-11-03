import numpy as np
from typing import List
import base64


def embedding_to_str(feature: List[float]) -> str:
    s = np.array(feature, dtype='<f4').tobytes()
    return base64.b64encode(s).decode()


def  str_to_embedding(s: str) -> List[float]:
    s = base64.b64decode(s)
    return np.frombuffer(s, dtype='<f4').tolist()