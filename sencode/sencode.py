import numpy as np
import pandas as pd

blosum62 = pd.read_table('blosum62.txt', delim_whitespace=True)
def encode_blosum62(sequence):
    return np.array([blosum62[c] for c in sequence])

alphabet = list('ARNDCQEGHILKMFPSTWYVBZX*')
alpha_to_idx = {c: i for i, c in enumerate(alphabet)}
def encode_onehot(sequence):
    return np.array([onehot(alpha_to_idx[c]) for c in sequence])

def onehot(i):
    onehot = np.zeros(len(alphabet))
    onehot[i] = 1
    return onehot
