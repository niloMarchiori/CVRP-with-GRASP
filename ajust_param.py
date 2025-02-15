from Scripts.read_config import parse_parameters
from Scripts.read_dir import read_dir
from Scripts.run_instance import run_instance
import pandas as pd

parametros=parse_parameters()
dir=parametros['teste_dir']




for instance in read_dir(dir):
    dados={'alpha':[],'max_iter':[],'neibors':[],'custo':[]}
    for alpha in parametros['alpha']:
        for max_iter in parametros['max_iter']:
            for neibor in parametros['neibors']:
                 instance_path=dir+'/'+instance
                 sol=run_instance(instance_path,alpha,max_iter,neibor)
                 dados['alpha'].append(alpha)
                 dados['max_iter'].append(max_iter)
                 dados['neibors'].append(neibor)
                 dados['custo'].append(sol['Custo'])
    df = pd.DataFrame(dados)
    print(df.to_string(index=False))
    df.to_csv("Output/Ajuste_de_parametros/"+instance[:-3]+"json", index=False)

                 





