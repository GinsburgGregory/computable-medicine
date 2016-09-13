import os 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.join('.','sample-dataframe.csv'))

ax = sns.barplot(data=df, x='disease', y='probability', hue='type')
ax.set_ylabel("Probability")
ax.set_xlabel("Disease")
ax.set_yscale('log')
plt.legend(title="")
plt.savefig(os.path.join('.','sample-bar-graph.png'))
