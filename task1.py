import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.distplot(df['total_bill'], bins=20, kde=True, hue='smoker')
plt.title('Розподіл Сума Рахунку за Категорією Курців')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.legend(title='Курець')
plt.show()
