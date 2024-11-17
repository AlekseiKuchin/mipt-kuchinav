import random

def counter_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % configuration.signs  # Контрит последний ход
    else:
        return random.randrange(0, configuration.signs)  # Первый ход случайный
