import pandas as pd
from sklearn import preprocessing
from matplotlib.image import imread
import numpy as np

df = pd.read_csv("C:\\Users\\Riley\\Desktop\\MachineLearning\\dog-breed-identification\\labels.csv")

print(list(df))
# print(df.describe())
# print(df.iloc[100])

breeds = df["breed"].unique()
le = preprocessing.LabelEncoder()
le.fit(df["breed"])

df["breed"] = le.transform(df["breed"])
X = np.zeros((10222,20000))
y = np.zeros((10222))
for idx,row in df.iterrows():
    img = imread("C:\\Users\\Riley\\Desktop\\MachineLearning\\dog-breed-identification\\train\\train\\000bec180eb18c7604dcecc8fe0dba07.jpg")
    img = img.flatten()
    X[idx, :] = img[:20000]
    y[idx] = row["breed"]
    print(idx)
    
print(df.head())
print(img.shape)

