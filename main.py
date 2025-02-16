import os
import sys
from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
from Scripts.gera_grafico import gera_grafico_An32k5
import pandas as pd

def main():
    stop=False
    for X in ['A','B','F']:
        instances_path=read_dir(f'Instances/{X}')
        rows=[]
        ##MUDAR DA MAIN CERTA===========
        df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap','n_iter'])
        ##==============================
        for instance in instances_path:
            try:
                dados=run_instance(f'Instances/{X}/{instance}',alpha=0.1,max_iter=10000,neibors=[0,1])
                rows.append(dados)
                print(instance, 'OK')
            except:
                stop=True
                break
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"Output/Instance_{X}/out_{X}.csv", index=False)

        if stop:
            break
if __name__=='__main__':
    # gera_grafico_An32k5()
    main()