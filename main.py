import os
import sys
from Scripts.run_instance import *
import pandas as pd

def read_dir(instance_directory):
    directory_path=instance_directory
    files_names=[]
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path) and item[-1]!='l':
                files_names.append(item)
    else:
        print(f'O diretório {directory_path} não existe ou não é um diretório.')

    files_names=sorted(files_names)
    return files_names

def main():
    for X in ['A','B','F']:
        instances_path=read_dir(f'Instances/{X}')
        rows=[]
        df=pd.DataFrame(columns=['Instance_name', 'Custo','Tempo','Best_temp','n_iter','Erro'])
        for instance in instances_path:
            dados=run_instance(f'Instances/{X}/{instance}',max_iter=1000)
            rows.append(dados)
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"Output/Instance_{X}/out_{X}.csv", index=False)
if __name__=='__main__':
    main()