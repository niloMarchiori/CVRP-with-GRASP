import os
import sys
from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
import pandas as pd

def main():
    for X in ['A','B','F']:
        instances_path=read_dir(f'Instances/{X}')
        rows=[]
        df=pd.DataFrame(columns=['Instance_name', 'Custo','Tempo','Best_temp','n_iter','Erro'])
        for instance in instances_path:
            dados=run_instance(f'Instances/{X}/{instance}',max_iter=100)
            rows.append(dados)
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"Output/Instance_{X}/out_{X}.csv", index=False)
if __name__=='__main__':
    main()


# ['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap','n_iter']