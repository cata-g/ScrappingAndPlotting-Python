import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

frames = []

excel_sheets = pd.read_excel('research.xlsx',sheet_name=None)
for key in excel_sheets.keys():
    frames.append(excel_sheets[key])
df = pd.concat(frames)

test_df = pd.DataFrame(df)[['Category', 'Applicants']]
cat_apps = test_df.groupby(['Category']).sum()

plt.figure(figsize=(12,8), dpi=200)
sns.barplot(data=cat_apps, y=cat_apps.index, x='Applicants', palette='Set2')
plt.show()
