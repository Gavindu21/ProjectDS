
# iris_analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

print("Dataset Info:")
print(iris.head())
print(iris.describe())


sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.title("Sepal Length vs Sepal Width by Species")
plt.savefig("iris_plot.png")  
plt.show()