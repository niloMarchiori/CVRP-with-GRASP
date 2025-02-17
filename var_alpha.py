from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
import matplotlib.pyplot as plt
import numpy as np

def plot_save(costs,alpha,Output_dir,fig_name,title):
    fig, ax = plt.subplots()
    bins = np.arange(780, 2400, 40)
    ax.hist(costs, bins,edgecolor='black', density=False)

    ax.set_title(f'Distribuição para alpha={alpha:.1f} - {title}', fontsize=14, fontname='Times New Roman')
    ax.set_xlabel('Custo da solução', fontsize=12, fontname='Times New Roman')
    ax.set_ylabel('Ocorrência', fontsize=12, fontname='Times New Roman')
    ax.set_xlim(760,2400)
    ax.axvline(x=784, color='red', linestyle='--', linewidth=1, label='BKS*')
   
    ax.legend(fontsize=12, frameon=True)
    ax.tick_params(axis='both', labelsize=10)


    plt.xticks(fontname='Times New Roman')
    plt.yticks(fontname='Times New Roman')
    # plt.show()
    plt.savefig(f"{Output_dir}/{fig_name}_{alpha:.1f}.png", dpi=300)

def main():

    instance='Instances/A/A-n32-k5.vrp'
    Output_dir='Output/var_alpha'
    
    var_alpha=[ 0.1*i for i in range(11)]   
    
    for alpha in var_alpha:
        costs=[]
        for i in range(1000):
            dados=run_instance(instance,alpha,max_iter=10,neibors=[],n_iter=1)
            costs.append(dados['Best_cost'])
        plot_save(costs,alpha,Output_dir,'SLS',"sem busca local")
    print('ok')
    for alpha in var_alpha:
        costs=[]
        for i in range(1000):
            dados=run_instance(instance,alpha,max_iter=10,neibors=[0,1],n_iter=1)
            costs.append(dados['Best_cost'])
        plot_save(costs,alpha,Output_dir,'CLS',"com busca local")


if __name__=='__main__':
    main()