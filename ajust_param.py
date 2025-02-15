from Scripts.read_config import parse_parameters
from Scripts.read_dir import read_dir
from Scripts.run_instance import run_instance
import pandas as pd

parametros=parse_parameters()
dir=parametros['teste_dir']

dados=[[],[],[]]

for instance in read_dir(dir):
    for i in range(3):
        sol=run_instance(dir+'/'+isinstance,parametros['alpha'][i],max_iter=100000)
        





colunas = pd.MultiIndex.from_tuples([
    ("alpha", "min"),
    ("alpha", "alpha_var"),
    ("alpha", "alpha_max"),
    ("max_iter", "max_iter_min"),
    ("max_iter", "max_iter_mid"),
    ("max_iter", "max_iter_max"),
    ("neibors", "valor")])