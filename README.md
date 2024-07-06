# Algoritmos_de_agrupamento
Esse projeto aborda o uso de três diferentes algoritmos não supervisionados para realizar agrupamento na base de dados Iris. Foram utilizados os algoritmos k-means, DBSCAN e hierárquico.

#### K-Means
O algoritmo **k-means** é um método de agrupamento que particiona os dados em \(k\) clusters, onde \(k\) é um número pré-definido. Ele funciona atribuindo cada ponto de dados ao cluster mais próximo com base na distância média aos centróides dos clusters. Os centróides são iterativamente recalculados até que as atribuições de cluster não mudem mais significativamente, nesse caso, como o numero de cluster já era de conhecimento, o mesmo não precisou ser recalculado.

#### DBSCAN
O **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** é um algoritmo de agrupamento baseado em densidade que identifica clusters em regiões densas de pontos de dados, separando os ruídos (pontos de dados que não pertencem a nenhum cluster). Ele é especialmente útil para detectar clusters de forma arbitrária e em cenários onde possam ter diferentes densidades.

#### Agrupamento Hierárquico
O **agrupamento hierárquico** constrói uma árvore de clusters (dendrograma), onde cada nível da árvore representa uma divisão dos dados em clusters menores. Existem duas abordagens principais: aglomerativa (bottom-up) e divisiva (top-down). No método aglomerativo, cada ponto de dados começa como um cluster separado e os clusters são mesclados iterativamente até que todos os pontos estejam em um único cluster.

### Desempenho dos Algoritmos
- **K-Means:** Funciona bem quando os clusters são esféricos e de tamanho similar. Nesse caso, o algoritmo identifica corretamente os clusters correspondentes às três espécies, mas é sensível a outliers e à escolha inicial dos centróides.
- **DBSCAN:** É eficaz para detectar clusters de formas arbitrárias e é robusto a outliers. Para essa base de dados, o DBSCAN identificou os clusters naturais das espécies, mas a escolha dos parâmetros (como \(epsilon\) e o número mínimo de pontos) é crucial para um bom desempenho.
- **Agrupamento Hierárquico:** Fornece uma visualização detalhada da estrutura dos dados através do dendrograma, permitindo uma análise profunda dos níveis de agrupamento. No entanto, pode ser computacionalmente intensivo para grandes conjuntos de dados. Na base de dados Iris, este método mostra como as diferentes espécies se subdividem e se relacionam.

### Relevância
Esse projeto testa a eficácia de diferentes modelos de agrupamento em bases de dados conhecidas, sendo fundamentais para:

1. **Comparação de Algoritmos:** Permitem comparar a eficácia de diferentes métodos em termos de precisão, robustez e eficiência.
2. **Aprimoramento de Modelos:** Ajudam a identificar as limitações e pontos fortes de cada algoritmo, orientando melhorias futuras.
3. **Educação e Aprendizado:** São recursos valiosos para o ensino de técnicas de aprendizado de máquina, proporcionando exemplos práticos para estudantes e pesquisadores.
4. **Aplicações Práticas:** Facilitam a escolha do algoritmo mais adequado para problemas específicos em aplicações do mundo real, desde a biologia até a análise de mercado.

O uso de k-means, DBSCAN e algoritmos hierárquicos na base de dados Iris exemplifica como diferentes abordagens de agrupamento podem ser aplicadas e comparadas para entender melhor a estrutura dos dados. Esses estudos são cruciais para o desenvolvimento contínuo de técnicas de aprendizado de máquina e para a aplicação eficiente dessas técnicas em diversas áreas.

Esses algoritmos, com suas diferentes metodologias e características, proporcionam uma visão abrangente de como o agrupamento não supervisionado pode ser utilizado para explorar e entender conjuntos de dados complexos.
