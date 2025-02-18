import re

def parse_parameters(file_path='config.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    parameters = {'alpha':0,'max_iter':1,'neibors':[],
                  'Instance_dir':[],'draw':False,'n_iter':5,'Output_dir':''}
    
    for line in lines:
        line = line.strip()
        
        if not line or line.startswith('#') or '-' in line:
            continue
        line=line.split(':')
        if line[0]=='alpha':
            parameters['alpha']=float(line[1])

        elif line[0]=='max_iter':
            parameters['max_iter']=int(line[1])
        
        
        elif line[0]=='neibors':
            parameters['neibors']=(list(map(int,line[1].split())))

        elif line[0]=='Instance_dir':
            for dir in line[1].split():
                parameters['Instance_dir'].append(dir)
        elif line[0]=='Output_dir':
            parameters['Output_dir']=line[1]
        elif line[0]=='draw':
            if line[1]==' False':
                parameters['draw']=False
            if line[1]==' True':
                parameters['draw']=True

        elif line[0]=='n_iter':
            parameters['n_iter']=int(line[1])
        
            
    return parameters