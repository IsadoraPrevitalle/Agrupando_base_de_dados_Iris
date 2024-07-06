import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

atributos = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'class']
df = pd.read_csv('iris.csv', names=atributos)

#print(df.describe())
#print(df.head())

#Criando visualização
sns.set(rc ={'figure.figsize':(10,5)})
sns.scatterplot(data = df, x='petal.length', y='petal.width')
plt.show()

# Criando a matriz x

x = df[['sepal.length','sepal.width','petal.length','petal.width']]
print(x)

z = linkage(x, method='ward')
plt.figure(figsize=(12, 5))
dendrogram(z)
plt.title('Dendograma')
plt.xlabel('Amostras')
plt.ylabel('Distância')
plt.axhline(y=10, color='r', linestyle='--')
plt.show()

#executar o agrupamento hierarquico
agg__clustering = AgglomerativeClustering(n_clusters=3) #n_clusters Se eu não passar ele tenta por default
rotulos = agg__clustering.fit_predict(x)
df['cluster'] = rotulos

print(df)