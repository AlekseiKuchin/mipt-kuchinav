def cyclic_agent(observation, configuration):
    return observation.step % configuration.signs  # Циклический выбор: камень -> бумага -> ножницы
