# 🪢 Algoritmo de Busca da url A e B

Este código implementa um algoritmo de pesquisa em largura para encontrar o caminho mais curto entre dois sites em um determinado grafo de sites conectados. 
Um problema é criado com o grafo, o nó inicial e uma função para verificar se o nó atual é o site alvo.

## 🧱 Atributos de classes
### 🧶 Nó
- Estado
  - Estado atual (site) do nó.
- Custo
  - O custo acumulado para chegar a este nó.
- Pai
  - O nó pai do nó atual.
- Ação
  - A ação tomada para alcançar este nó.
  
### ❔Problema
- Espaco_estados
  - O grafo de sites e suas conexões.
- Inicial
  -  O nó inicial na árvore de pesquisa.
- Objetivo
  - Uma função lambda para verificar se o nó atual é o site de destino.

### 🔍 Algoritmo de pesquisa em largura e profundidade
- Problema
  - Uma instância da classe `Problema`.
- Fronteira
  - Uma lista de nós a serem explorados.
- Visitados
  - Uma lista de nós visitados.
- Solução
  - O caminho da solução encontrada pelo algoritmo.
- Situação
  - O status atual da pesquisa.

## ⚙️ Métodos de execução
- `Executar()`
  - Executa o algoritmo de busca em largura e imprime o resultado.
- `Passo_busca()`
  - Executa uma única etapa do algoritmo de busca.