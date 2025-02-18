from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
import pandas as pd
from ajust_param import ajuste_param

def gera_tabelas():
    stop=False
    instance_dir=['Instances/A','Instances/B','Instances/F']
    Output_dir='Output'
    for dir in instance_dir:
        instances_path=read_dir(dir)
        rows=[]
        
        df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap'])
        
        for instance in instances_path:
            try:
                dados=run_instance(f'{dir}/{instance}',alpha=0.24,max_iter=15000,neibors=[0,1])
                rows.append(dados)
                print(instance, 'OK')
            except:
                stop=True
                break
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"{Output_dir}/{dir}/out.csv", index=False)

        if stop:
            break
if __name__=='__main__':
    ajuste_param()
    gera_tabelas()