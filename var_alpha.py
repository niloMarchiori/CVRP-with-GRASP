from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
import pandas as pd

def main():

    instance='Instances/A/A-n32-k5.vrp'
    Output_dir='Output/var_alpha'
    rows=[]
        
    df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost',
                             'Avrg_cost','Best_temp',
                             'Avrg_temp','Best_gap','Avrg_gap'])
    
    dados=run_instance(f'{dir}/{instance}',alpha=0.1,max_iter=10000,neibors=[])
    rows.append(dados)
    print(instance, 'OK')
    df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
    # print(df)
    df.to_csv(f"{Output_dir}/{dir}/out.csv", index=False)

if __name__=='__main__':
    main()