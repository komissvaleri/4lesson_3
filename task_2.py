

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


warnings.filterwarnings('ignore')

df = pd.read_csv('zp.csv')

qu_1 = df['zplt'].quantile(0.25)
qu_3 = df['zplt'].quantile(0.75)
raz = qu_3 - qu_1
print(qu_1, qu_3, raz)
boxplot_range = (qu_1 - 1.5 * raz, qu_3 + 1.5 * raz)
print(boxplot_range)

outliers = df.loc[(df['zplt'] < boxplot_range[0]) | (df['zplt'] > boxplot_range[1])]
print(outliers.shape[0])
df[['zplt']].boxplot()
plt.show()