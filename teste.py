
solucao=[[0,1,2,3,4,5,0],
         [0,6,7,8,0],
         [0,9,10,11,12,13,14,0]]
posiveis={1:0}
iteracao=0
for i in range(1,15):
    for j in range(i+1,15):
        posiveis[(i,j)]=0
        iteracao+=1
print(iteracao)

    
iteracao=0
for rota_i in range(len(solucao)-1):
    for no_i in solucao[rota_i]:
        if no_i==0: continue
        for rota_j in range(rota_i+1,len(solucao)):
            for no_j in solucao[rota_j]:
                if no_j==0: continue
                posiveis[(no_i,no_j)]+=1
                iteracao+=1
print(iteracao)

for key in posiveis:
    print(key, posiveis[key])