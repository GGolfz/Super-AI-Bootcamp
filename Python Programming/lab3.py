#  22p21c0568-วิศรุต
#  read data & visualization
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
y = df[df['diabetes']==1]
n = df[df['diabetes']==0]
plt.xlabel('isDiabetes')
plt.ylabel('count')
ax = ['yes','no']
ay = [len(y),len(n)]
plt.bar(ax,ay)
plt.show()