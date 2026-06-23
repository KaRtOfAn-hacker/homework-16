import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.distplot(df['total_bill'], bins=20, kde=True, color='brown', alpha=0.7, linewidth=3)
plt.title('Розподіл Сума Рахунку з Налаштуваннями Графіка')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.show()
