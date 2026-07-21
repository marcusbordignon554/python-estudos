import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv"
df = pd.read_csv(url)

df = df.drop(columns=['pm2'])  
df = df.astype({
    'condominio': np.float64,
    'quartos': np.int64,
    'suites': np.int64,
    'vagas': np.int64,
    'area': np.float64,
    'preco': np.float64
})  

df['preco_m2'] = df['preco'] / df['area']  
df['condominio'] = df['condominio'].round(2)
df['preco'] = df['preco'].round(2)
df['preco_m2'] = df['preco_m2'].round(2)  

df = df[(df['quartos'] > 2) & (df['suites'] > 1) & (df['vagas'] >= 2) & (df['area'] > 200)]  # e)

df = df.loc[df.groupby("bairro")["preco"].idxmin()]  

df.to_csv("saida_exercicio5.csv", index=False)  
