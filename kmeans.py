import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

atributos = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'class']
df =pd.read_csv('iris.csv', names=atributos)

# print(df.describe())
# print(df.head())

#Criando visualização
sns.set(rc ={'figure.figsize':(10,5)})
#sns.scatterplot(data = df, x='petal.length', y='petal.width', hue='class') #--> hue: cria e separa por meio de legenda
# sns.scatterplot(data = df, x='petal.length', y='petal.width')
# plt.show()

#Constroi uma matriz contendo todos os atributos com execeção da class
X = df[df.columns.difference(['class'])].values
print(X)

#N_cluster é o valor de k grupos 
kmeans = KMeans(n_clusters=3)

#Treino do algoritmo
kmeans.fit(X)

print('Centroide')
#valor dos centroides
print(kmeans.cluster_centers_)

print('Rótulos')
#Rótulos atribuidos a cada amostra
print(kmeans.labels_)

df['cluster'] = kmeans.labels_
print(df)

sns.scatterplot(data=df, x='sepal.length', y='sepal.width', hue='cluster')
plt.scatter(kmeans.cluster_centers_[:,2], kmeans.cluster_centers_[:,3], s=100, c = 'black')
plt.show()

sns.scatterplot(data=df, x='petal.length', y='petal.width', hue='cluster')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c = 'black')
plt.show()

#Se não sabemos qual a quantidade de grupo queremos
distancia = {}
#Testo o kmeans com diferentes valores de k
for k in range(1,15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distancia[k] = kmeans.inertia_

sns.pointplot(x=list(distancia.keys()), y = list(distancia.values()))    
plt.show()