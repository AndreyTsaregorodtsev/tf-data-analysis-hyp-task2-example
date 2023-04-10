import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if(anderson_ksamp([x,y]).pvalue < 0.01):
      return False
    else:
      return True
