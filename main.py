from kaggle_environments import evaluate

# Список файлов с кодами агентов
agents = [
    "rock_agent.py",    # Агент, выбирающий только камень
    "random_agent.py",  # Случайный агент
    "copy_opponent.py", # Агент, копирующий противника
    "cyclic_agent.py",  # Цикличный агент
    "counter_agent.py", # Агент, контрящий ходы
]

# Турнир: каждый агент против каждого
results = {}

for i in range(len(agents)):
    for j in range(i + 1, len(agents)):
        agent1, agent2 = agents[i], agents[j]

        # Оценка матча между двумя агентами
        match_result = evaluate("rps", [agent1, agent2], configuration={"episodeSteps": 100})
        results[(agent1, agent2)] = match_result

# Вывод результатов
for (agent1, agent2), score in results.items():
    print(f"Match {agent1} vs {agent2}: {score}")
