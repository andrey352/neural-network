import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

print(data.head(10))


sns.barplot(x='Дата', y='Значение', data=data)
plt.show()


sns.histplot(data=data, x='Дата', hue='Значение', kde=True)
plt.show()

