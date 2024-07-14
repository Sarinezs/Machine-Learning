import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pima_diabelete.csv')

df = df.drop(['Unnamed: 0'], axis=1)

df['class'] = df['class'].replace('tested_positive', 1)
df['class'] = df['class'].replace('tested_negative', 0)
df = df.fillna(df.mean())

plas_skin_scaler = MinMaxScaler(feature_range=(0,1))
df['plas'] = plas_skin_scaler.fit_transform(df[['plas']])
df['skin'] = plas_skin_scaler.fit_transform(df[['skin']])

insu_scaler = StandardScaler()
df['insu'] = insu_scaler.fit_transform(df[['insu']])

cor =df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(cor, annot = True)
plt.title('Heat Map')
# plt.show()

cor_target = cor['class']
relevant_feature = cor_target.sort_values(ascending=False)[1:4]

relevant_feature.to_csv('new_data.csv')

# print(df)