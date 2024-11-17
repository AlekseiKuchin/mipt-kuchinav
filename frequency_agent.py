import random

def frequency_agent(observation, configuration):
    if observation.step == 0:
        return random.randrange(0, configuration.signs)  # Первый ход случайный

    # Считает, какой ход соперник использовал чаще всего
    actions = observation['lastOpponentActions'] if hasattr(observation, 'lastOpponentActions') else []
    if actions:
        most_common = max(set(actions), key=actions.count)  # Находит самый частый ход
        return (most_common + 1) % configuration.signs  # Контрит его
    return random.randrange(0, configuration.signs)
