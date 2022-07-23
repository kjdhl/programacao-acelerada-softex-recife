import pandas as pd
import numpy as np

df = pd.read_csv('notas_alunos.csv')


soma_notas = df[' nota_1'] +df['nota_2'] 
df['media'] = soma_notas/2 


df['situacao'] = np.where((df['media']>= 7) & (df['faltas']<=5), 'APROVADO','REPROVADO')
df.to_csv('alunos_situacao.csv')


    