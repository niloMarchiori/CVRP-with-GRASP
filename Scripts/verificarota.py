import vrplib

instance = vrplib.read_instance(f'Instances/A/A-n32-k5.vrp')
for i in range(instance['dimension']):
    for j in range(i,instance['dimension']):
        instance['edge_weight'][i][j]=int(round(instance['edge_weight'][i][j]))
        instance['edge_weight'][j][i]=int(round(instance['edge_weight'][i][j]))

adj=instance['edge_weight']
demanda=instance['demand']

sum=0

while True:
    try:
        lista=list(map(int,input().split()))
    except:
        break
    capacidade=0
    for i in range(len(lista)-1):
            j=i+1
            a=lista[i]
            b=lista[j]
            sum+=adj[a][b]
            capacidade+=demanda[b]
    print('capacidade: ',capacidade)
print('Custo:',sum)