from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("penguins").head(20)
# print(var)
sns.scatterplot(x=var.bill_length_mm, y=var.bill_depth_mm,hue =var.sex)
plt.show()
