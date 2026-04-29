
# Meses (1 a 12) relacionados aos níveis de água em metros
niveis_agua = {
    "Janeiro": 30, "Fevereiro": 40, "Março": 35, "Abril": 28,
    "Maio": 25, "Junho": 22, "Julho": 20, "Agosto": 18,
    "Setembro": 20, "Outubro": 22, "Novembro": 25, "Dezembro": 28
}

def gerenciar_recurso(dados):
    # Identificando pontos notáveis (máximos e mínimos) [4, 5]
    mes_max = max(dados, key=dados.get)
    mes_min = min(dados, key=dados.get)
    
    print(f"Relatório de Gestão de Recursos:")
    print(f"- Pico de nível (Máximo): {mes_max} com {dados[mes_max]}m")
    print(f"- Nível mais baixo (Mínimo): {mes_min} com {dados[mes_min]}m")
    
    # Aplicação de Intervalos para Intervenção [6, 7]
    # Se o nível estiver no intervalo [8], emitir alerta crítico
    limite_critico = 20
    
    print("\nAnálise de Intervenção:")
    for mes, nivel in dados.items():
        if nivel <= limite_critico:
            print(f"⚠️ ALERTA: Intervenção necessária em {mes}. Nível {nivel}m está no intervalo crítico.")
            

# Execução do algoritmo
gerenciar_recurso(niveis_agua)