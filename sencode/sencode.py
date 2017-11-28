import numpy as np
import pandas as pd

import os
package_dir, _ = os.path.split(__file__)
data_file = os.path.join(package_dir, 'blosum62.txt')

blosum62 = pd.read_table(data_file, delim_whitespace=True)
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
