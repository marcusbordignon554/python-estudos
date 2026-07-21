import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv"
df = pd.read_csv(url)

df_maiores = df.sort_values(by="area", ascending=False).head(300)

plt.figure(figsize=(10, 7))

bairros_cores = [
    "Ipanema", "Copacabana", "Leblon", "Gávea",
    "Botafogo", "Tijuca", "Grajaú"
]

cores = {
    "Ipanema": "red",
    "Copacabana": "green",
    "Leblon": "blue",
    "Gávea": "magenta",
    "Botafogo": "cyan",
    "Tijuca": "orange",
    "Grajaú": "yellow"
}

for bairro in bairros_cores:
    sub_df = df_maiores[df_maiores['bairro'] == bairro]
    plt.scatter(
        sub_df['area'],
        sub_df['condominio'],
        s=sub_df['preco'] / 2e5,  
        c=cores[bairro],
        alpha=0.5,
        label=bairro
    )

plt.xlabel("area")
plt.ylabel("condominio")
plt.title("Área X valor do condomínio de apartamentos no Rio de Janeiro")
plt.legend(title="", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()
