import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest


chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if(ztest(x,y)[1] < 0.01):
      return True
    else:
      return False
