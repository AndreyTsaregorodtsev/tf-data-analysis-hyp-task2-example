import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp


chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if(cramervonmises_2samp(x,y).pvalue < 0.01):
      return False
    else:
      return True
