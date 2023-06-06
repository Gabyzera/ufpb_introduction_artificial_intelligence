# ⭐ Algoritmo A*
Esta pasta apresenta o sétimo exercício, contendo a apresentação do questionário, testes do código e comentários sobre as informações geradas. 

## ❔ O que é o Algoritmo A*?
É um algoritmo de busca utilizado para encontrar o caminho mais curto em um grafo. Ele combina os benefícios da busca em largura (BFS) e da busca em profundidade (DFS), aproveitando uma função heurística para orientar a busca em direção à solução mais promissora.

O algoritmo A* utiliza uma estrutura de dados chamada fila de prioridade  para armazenar os nós a serem explorados. Cada nó na fila de prioridade tem um valor de prioridade associado, que é calculado pela soma do custo do caminho percorrido até o nó (custo) e uma estimativa do custo restante até o objetivo (heurística). O algoritmo seleciona o nó com a menor prioridade (menor valor de f = g + h) para expandir e explorar.

## 📄 Fila de prioridade
Min-Heap