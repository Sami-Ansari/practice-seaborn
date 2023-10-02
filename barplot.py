from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
# show the mean value
var = sns.load_dataset('penguins').head(15)
# print(var)

# order parameter is used to set the parameter of the graph
# order_1 = ["Dream","Biscoe","Torgersen"]
# sns.barplot(x=var.island,y = var.bill_length_mm,
#             hue = var.sex ,order= order_1,
#             hue_order=["Female","Male"],ci=1,
#             orient="v")
# island vs bill_len hue is used for comparison of male and female
# ci for middle black line ci means confidence interval
# orient h for horizontal only apply on numeric value and v for vertical

order_1 = ["Dream","Biscoe","Torgersen"]
sns.barplot(x=var.bill_length_mm,y = var.bill_length_mm,
            hue = var.sex ,
            hue_order=["Female","Male"],ci=1,
            orient="h",palette='icefire',saturation=10)
plt.show()


