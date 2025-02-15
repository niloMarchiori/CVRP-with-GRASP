from Scripts import read_config,run_instance
import pandas as pd

parametros=read_config()

dados=pd.DataFrame(columns=['Instance','alpha_min','alpha_mid','alpha_max',])