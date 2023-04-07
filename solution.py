import pandas as pd
import numpy as np


chat_id = 586404828 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  g = []
  g = []
  for i in range(len(x)):
    g.append(2 * x[i] / 4624.)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#    return x.mean() # Ваш ответ
    return np.mean(g)
