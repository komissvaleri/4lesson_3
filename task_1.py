

import warnings
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')

df = pd.read_csv('zp.csv')

mean_zp = df['zplt'].sum() / df['zplt'].count()
print(mean_zp)
mean = df['zplt'].mean()
print(mean)

msd_zp = (df['zplt'] - df['zplt'].mean()) ** 2
print(msd_zp)

zp_std = np.sqrt(((df['zplt'] - df['zplt'].mean()) ** 2).sum() / df['zplt'].count())
print(zp_std)
std = df['zplt'].std(ddof=0)
print(std)

zp_variance = ((df['zplt'] - df['zplt'].mean()) ** 2).sum() / df['zplt'].count()
print(zp_variance)
zp_var = df['zplt'].var(ddof=0)
print(zp_var)


zp_variance2 = ((df['zplt'] - df['zplt'].mean())**2).sum() / (df['zplt'].count() - 1)
print(zp_variance2)
zp_var_2 = df['zplt'].var(ddof=1)
print(zp_var_2)

