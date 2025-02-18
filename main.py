from Scripts.run_instance import run_instance
from Scripts.read_config import parse_parameters
from Scripts.read_dir import read_dir
import pandas as pd
import os

def main():
    param = {'alpha':0,'max_iter':1,'neibors':[],
                  'Instance_dir':[],'draw':False,'n_iter':5,'Output_dir':''}
    param=parse_parameters()
    alpha=param['alpha']
    max_iter=param['max_iter']
    neibors=param['neibors']
    instance_dir=param['Instance_dir']
    draw=param['draw']
    n_iter=param['n_iter']
    Output_dir=param['Output_dir']

    stop=False

    

    for dir in instance_dir:
        instances_path=read_dir(dir)
        rows=[]
        
        df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap'])
        
        for instance in instances_path:
            try:
                dados=run_instance(f'{dir}/{instance}',alpha,max_iter,neibors,n_iter,draw)
                rows.append(dados)
                print(instance, 'OK')
            except:
                stop=True
                break
        final_dir=f"{Output_dir}/{dir}"
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        df.to_csv(f"{final_dir}/out.csv", index=False)

        if stop:
            break
if __name__=='__main__':
    main()