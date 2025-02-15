import os
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