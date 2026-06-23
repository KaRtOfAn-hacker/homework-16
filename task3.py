import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('penguins')

for col in df.select_dtypes(include=['object', 'category']).columns:
    df[col] = df[col].astype('category').cat.codes

corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()
