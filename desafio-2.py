class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades

    def __str__(self):
        return self.nome

def recomendar_modelo(caracteristicas):
    modelos = [
        ModeloIA('Claude 3 Opus', 9, 10, 5, ['Pesquisa', 'Desenvolvimento Acelerado']),
        ModeloIA('Claude 3 Sonnet', 8, 5, 7, ['Codificação', 'Recuperação de informações']),
        ModeloIA('Claude 3 Haiku', 7, 9, 6, ['Velocidade', 'Resumo de dados não estruturados'])
    ]
    modelo_recomendado = None
    capacidades_usuario = [capacidade.lower() for capacidade in caracteristicas['Capacidades']]

    for modelo in modelos:
        capacidades_modelo = [capacidade.lower() for capacidade in modelo.capacidades]
        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado

def obter_caracteristicas():
    caracteristicas = {}
    try:
        caracteristicas['Desempenho'] = int(input())
        caracteristicas['Velocidade'] = int(input())
        caracteristicas['Custo'] = int(input())
        capacidades = input().split(',')
        caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
        return caracteristicas
    except ValueError:
        print("Valores inválidos. Certifique-se de inserir números para desempenho, velocidade e custo.")
        return None

caracteristicas_entrada = None
while not caracteristicas_entrada:
    caracteristicas_entrada = obter_caracteristicas()

melhor_modelo = recomendar_modelo(caracteristicas_entrada)
if melhor_modelo:
    print(f"O {melhor_modelo} é o modelo recomendado.")
else:
    print("Nenhum modelo encontrado.")