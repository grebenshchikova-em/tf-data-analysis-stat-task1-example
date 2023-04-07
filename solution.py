import pandas as pd
import numpy as np


chat_id = 586404828 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  t = 68
  n = len(x)
  mu = 0
  sigma = 1

  x_error = np.random.normal(mu, sigma, n)
  a = 2 * x_error/ t**2

  return a.mean()
