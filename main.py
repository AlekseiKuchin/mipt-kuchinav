from kaggle_environments import make, evaluate

# Список агентов
agents = ["rock_agent.py", "random_agent.py", "copy_opponent.py", "cyclic_agent.py", "counter_agent.py", "frequency_agent.py"]

# Словарь для хранения результатов
results = {}

# Запускаем турнир: каждый агент играет с каждым
for i in range(len(agents)):
    for j in range(i + 1, len(agents)):
        agent1, agent2 = agents[i], agents[j]
        score = evaluate("rps", [agent1, agent2], configuration={"episodeSteps": 100})
        results[(agent1, agent2)] = score

# Печатаем результаты
for match, score in results.items():
    print(f"Match {match[0]} vs {match[1]}: {score}")
