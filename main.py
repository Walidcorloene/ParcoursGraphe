import pandas as pd
import csv

dfGraphe= pd.read_csv('probleme_graphe.csv',delimiter=',')

dfg= dfGraphe.copy()

dfg=dfg.sort_values(by='type_aretes',ascending=False)

depart=dfg[dfg['noeud_amont']== 'sommet_91']['noeud_aval'].values[0]
print(depart)

listExplo=[]
for i in range(10):
  lis=[]
  depart=dfg[dfg["type_aretes"]=='depart']['noeud_amont'].values[i]
  lis.append(depart)
  while(dfg[dfg["noeud_amont"]==depart]["type_aretes"].values[0]!= 'arrivee'):
    depart=dfg[dfg['noeud_amont']== depart]['noeud_aval'].values[0]
    lis.append(depart)
  lis.append(depart)
  listExplo.append(lis)
  print(f"aventurier {i}",listExplo[i])


