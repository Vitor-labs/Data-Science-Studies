# importing libraries
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler, Binarizer, StandardScaler, LabelEncoder

# data set link
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
# data parameters
names = ['Alcohol','Malic acid','Ash Alcalinity of ash',
        'Magnesium','Total phenols','Flavanoids',
        'Nonflavanoid phenols','Proanthocyanins','Color intensity',
        'Hue','OD280/OD315 of diluted wines','Proline']

# preparating of dataframe using the data at given link and defined columns list
dataframe = pandas.read_csv(URL, names = names)
array = dataframe.values

# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]

# initialising the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
# learning the statistical parameters for each of the data and transforming
rescaledX = scaler.fit_transform(X)

# summarize transformed data
binarizer = Binarizer(threshold = 0.0).fit(X)
binaryX = binarizer.transform(X)

# Computes the mean and std to be used for later scaling.
standard = StandardScaler().fit(X)
standardedX = standard.transform(X)

numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
print(binaryX[0:5,:])
print(standardedX[0:5,:])
