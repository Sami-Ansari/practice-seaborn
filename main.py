import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

# var = [1,2,3,4,5,6,7]
# var_1 = [2,3,4,1,5,6,7]

# df = pd.DataFrame({"var":var,"var_1":var_1})

# # plt.plot(var,var_1)
# plt.show()

# sns.lineplot(x='var',y = 'var_1',data = df)
# plt.show()

# load data from data sheet

y_1  = sns.load_dataset("penguins").head(20)
# print(y_1)
# sns.lineplot(x='bill_length_mm',y = 'flipper_length_mm',data = y_1)
# plt.show()
sns.lineplot(x='bill_length_mm',y = 'flipper_length_mm',data = y_1,
              hue="sex",style="sex",palette="Accent"
              ,markers=["o",">"],dashes=False) # palette for color 
    
plt.grid()
plt.title("Python")

plt.show()


