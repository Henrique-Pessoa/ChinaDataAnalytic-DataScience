import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./SuicideChina.csv",)
data.isnull().sum()

fig1 = plt.subplot(331)
fig2 = plt.subplot(332)
fig3 = plt.subplot(333)

age_groups = []

for x in data.Age:
    if x < 18:
        age_groups.append('child')
    elif 18 <= x < 35:
        age_groups.append('young')
    elif 35 <= x < 60:
        age_groups.append('Adult')
    else:
        age_groups.append('old')

data['Age_group'] = age_groups

plt.suptitle("Suiciding China")
sns.countplot(data=data,x='Year', hue='Sex',ax=fig1,palette="Pastel1")
sns.countplot(data = data, x="Age_group", hue="Sex",ax=fig2,palette="Pastel1")
sns.countplot(data = data, x="Age_group", hue="method",ax=fig3,palette="Pastel1")

plt.show()
