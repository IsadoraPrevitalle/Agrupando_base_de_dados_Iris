import pandas as pd
import seaborn as sns
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

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

#min_sample - quantidade de registros dentro do circulo para ser consigerado um grupo (por default é 5)
DBScan = DBSCAN(eps=0.5, min_samples=5)

DBScan.fit(x)

#Obtendo os rótulos dos grupos
rotulos = DBScan.labels_

print(rotulos)

df['cluster'] = rotulos
print(df)

sns.scatterplot(data=df, x='petal.length', y='petal.width', hue='cluster')
plt.show()