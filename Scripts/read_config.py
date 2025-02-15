import re

def parse_parameters(file_path='config.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    parameters = {'alpha':[0,0,0],'max_iter':[0,0,0],'neibors':[],'teste_dir':''}
    
    for line in lines:
        line = line.strip()
        
        if not line or line.startswith('#') or '-' in line:
            continue
        line=line.split()
        if line[0]=='alpha_min':
            parameters['alpha'][0]=float(line[1])
        elif line[0]=='alpha_max':
            parameters['alpha'][1]=float(line[1])
        elif line[0]=='alpha_var':
            parameters['alpha'][2]=float(line[1])

        elif line[0]=='max_iter_min':
            parameters['max_iter'][0]=int(line[1])
        elif line[0]=='max_iter_mid':
            parameters['max_iter'][1]=int(line[1])
        elif line[0]=='max_iter_max':
            parameters['max_iter'][2]=int(line[1])
        
        
        elif line[0]=='Use':
            parameters['neibors'].append(list(map(int,line[1:])))
        elif line[0]=='teste_dir':
            parameters['teste_dir']=line[1]
            
    return parameters