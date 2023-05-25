def acao(destino, custo):
  return {'destino': destino, 'custo': custo}

#definicao dos estados da Romenia com as cidades e as cidades conectadas a cada uma
estados_romenia = [
  {'estado': 'Arad',
    'acoes': [acao('Zerind', 75), acao('Sibiu', 140), acao('Timisoara', 118)]},
  {'estado': 'Zerind',
    'acoes': [acao('Arad', 75), acao('Oradea', 71)]},
  {'estado': 'Sibiu',
    'acoes': [acao('Arad', 140), acao('Oradea', 151), acao('Fagaras', 99), acao('Rimnicu Vilcea', 80)]},
  {'estado': 'Timisoara',
    'acoes': [acao('Arad', 118), acao('Lugoj', 111)]},
  {'estado': 'Oradea',
    'acoes': [acao('Zerind', 71), acao('Sibiu', 151)]},
  {'estado': 'Fagaras',
    'acoes': [acao('Sibiu', 99), acao('Bucharest', 211)]},
  {'estado': 'Rimnicu Vilcea',
    'acoes': [acao('Sibiu', 80), acao('Craiova', 146), acao('Pitesti', 97)]},
  {'estado': 'Lugoj',
    'acoes': [acao('Timisoara', 111), acao('Mehadia', 70)]},
  {'estado':'Bucharest',
    'acoes': [acao('Fagaras', 211), acao('Pitesti', 101), acao('Giurgiu', 90), acao('Urziceni', 85)]},
  {'estado': 'Craiova',
    'acoes': [acao('Drobeta', 120), acao('Rimnicu Vilcea', 146), acao('Pitesti', 138)]},
  {'estado': 'Pitesti',
    'acoes': [acao('Craiova', 138), acao('Rimnicu Vilcea', 97), acao('Bucharest', 101)]},
  {'estado': 'Mehadia',
    'acoes': [acao('Lugoj', 70), acao('Drobeta', 75)]},
  {'estado': 'Giurgiu', 
    'acoes': [acao('Bucharest', 90)]},
  {'estado': 'Urziceni',
    'acoes': [acao('Bucharest', 85), acao('Vaslui', 142), acao('Hirsova', 98)]},
  {'estado': 'Vaslui',
    'acoes': [acao('Urziceni', 142), acao('Iasi', 92)]},
  {'estado': 'Iasi',
    'acoes': [acao('Vaslui', 92), acao('Neamt', 87)]}, 
  {'evento': 'Neamt',
    'acoes': [acao('Iasi', 87)]},
  {'evento': 'Hirsova',
    'acoes': [acao('Urziceni', 98), acao('Eforic', 86)]},
  {'evento': 'Drobeta',
    'acoes': [acao('Mehadia', 75), acao('Craiova', 120)]},
  {'evento': 'Eforic',
    'acoes': [acao('Hirsova', 86)]}]

class No:
  def __init__(self, estado, custo, pai, acao):
    self.estado =  estado
    self.custo = custo
    self.pai = pai
    self.acao = acao
  
  def __str__(self):
    return f'({self.estado}, {self.custo})'
  
  def __repr__(self):
    return self.__str__()
  
  def filhos(self, problema):
    espaco_acoes = next(e for e in problema.espaco_estados if e['estado'] == self.estado)
    
    resultado = []
    for acao in espaco_acoes['acoes']:
      filho = No(acao['destino'], self.custo + acao['custo'],
                 self, acao['destino'])
      resultado.append(filho)
      
      return resultado
  
  def constroi_solucao(self):
    no_atual = self 
    solucao = [no_atual]
    while no_atual.pai != None:
      no_atual = no_atual.pai
      solucao.insert(0, no_atual)
      
    return solucao
    
class Problema:
  def __init__(self, espaco_estados, inicial, objetivo):
    self.espaco_estados = espaco_estados
    self.inicial = inicial
    self.objetivo = objetivo
    
busca_iniciando = 0
busca_falha = 1
busca_sucesso = 2
busca_em_curso = 3

class BuscaLargura:
  def __init__(self, problema):
    self.problema = problema
    self.fronteira = [problema.inicial]
    self.visitados = [problema.inicial.estado]
    self.solucao = []
    self.situacao = busca_iniciando
    
  def executar(self):
        while self.situacao != busca_falha and self.situacao != busca_sucesso:
            self.passo_busca()

        if self.situacao == busca_falha:
            print("Busca falhou!")
            
        elif self.situacao == busca_sucesso:
            print("Busca teve sucesso!")
            print(f"Solucao: {self.solucao}")
            
  def passo_busca(self):
    if (self.situacao == busca_falha):
      print("Busca falhou!")
      return
    
    if (self.situacao == busca_sucesso):
      print("Busca chegou ao objetivo com sucesso!")
      return
    
    try: 
      # utilizacao do pop para fila FIFO
      no = self.fronteira.pop(0)
    except IndexError:
      self.situacao = busca_falha 
      return
    
    # faz teste do objetivo 
    if self.problema.objetivo(no):
      self.situacao = busca_sucesso
      self.solucao = no.constroi_solucao()
      return 
      
    # obtem os filhos do no 
    for filho in no.filhos(self.problema):
      if (filho not in self.fronteira) and (filho.estado not in self.visitados):
        self.fronteira.append(filho)
        self.visitados.append(filho.estado)
  
class BuscaProfundidade:
  def __init__(self, problema):
    self.problema = problema
    self.fronteira = [problema.inicial]
    self.visitados = [problema.inicial.estado]
    self.solucao = []
    self.situacao = busca_iniciando
    
  def executar(self):
        while self.situacao != busca_falha and self.situacao != busca_sucesso:
            self.passo_busca()

        if self.situacao == busca_falha:
            print("Busca falhou!")
            
        elif self.situacao == busca_sucesso:
            print("Busca teve sucesso!")
            print(f"Solucao: {self.solucao}")
            
  def passo_busca(self):
    if (self.situacao == busca_falha):
      print("Busca falhou!")
      return
    
    if (self.situacao == busca_sucesso):
      print("Busca chegou ao objetivo com sucesso!")
      return
    
    try: 
    #utilizacao do push para fila LIFO
      no = self.fronteira.push(0)
    except IndexError:
      self.situacao = busca_falha 
      return
    
    # faz teste do objetivo 
    if self.problema.objetivo(no):
      self.situacao = busca_sucesso
      self.solucao = no.constroi_solucao()
      return 
      
    # obtem os filhos do no 
    for filho in no.filhos(self.problema):
      if (filho not in self.fronteira) and (filho.estado not in self.visitados):
        self.fronteira.append(filho)
        self.visitados.append(filho.estado)

no_arad = No('Arad', 0, None, None)
problema_romenia = Problema(estados_romenia, 
                            no_arad,
                            lambda no: no.estado == 'Bucharest')

while BuscaLargura != busca_falha and BuscaLargura != busca_sucesso:
  BuscaLargura.self.passo_busca()
  print(BuscaLargura.fronteira)

while BuscaProfundidade != busca_falha and BuscaProfundidade != busca_sucesso:
  BuscaProfundidade.self.passo_busca()
  print(BuscaProfundidade.fronteira)