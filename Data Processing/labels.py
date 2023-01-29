import pandas as pd
from sklearn.preprocessing import LabelEncoder

names = ['sepal length','sepal width','petal length','petal width','species']

# Import dataset
df = pd.read_csv('./Datasets/iris.data', names=names)
print(df['species'].unique())

# label_encoder object knows how to understand word labels.
label_encoder = LabelEncoder()

# Encode labels in column 'species'.
df['species']= label_encoder.fit_transform(df['species'])

print(df['species'].unique())

one_hot_encoded_data = pd.get_dummies(df, columns = ['species'])
print(one_hot_encoded_data)
