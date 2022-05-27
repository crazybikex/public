# PYTHON_RANDOM

# In[1]

# randomモジュールをインポート
import random

# 乱数シードを固定
random.seed(0)

# 0～9の乱数を生成
val = random.randrange(10)

print(val)
