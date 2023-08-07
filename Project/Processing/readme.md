### Table of Contents
- [**Data Processing** :](#data-processing-)
- [This is the final step in which the obtained output and the data model data and all the useful information are saved for future use.](#this-is-the-final-step-in-which-the-obtained-output-and-the-data-model-data-and-all-the-useful-information-are-saved-for-future-use)
- [**Feature Scaling**](#feature-scaling)
- [$$](#)
- [**Label Encoding**](#label-encoding)
- [**Imbalanced Data Distribution**](#imbalanced-data-distribution)
- [**Dummy Variables**](#dummy-variables)
- [**Data Distribution** :](#data-distribution-)
- [**Data Preprocessing** :](#data-preprocessing-)

## **Data Processing** :
Data Processing is the task of converting data from a given form to a much more usable and desired form i.e. making it more meaningful and informative. The output of this complete process can be in any desired form like graphs, videos, charts, tables, images, and many more, depending on the task we are performing and the requirements of the machine. Can be divided in the following steps:

1. Collection.
The most crucial step when starting with ML is to have data of good quality and accuracy, high-quality and accurate data will make the learning process of the model easier and better and at the time of testing, the model would yield state-of-the-art results. 

2. Preparation.
The collected data can be in a raw form which can’t be directly fed to the machine. So, this is a process of collecting datasets from different sources, analyzing these datasets and then constructing a new dataset for further processing and exploration. 

3. Input. 
Now the prepared data can be in the form that may not be machine-readable, so to convert this data to the readable form, some conversion algorithms are needed.

4. Processing. 
This is the stage where algorithms and ML techniques are required to perform the instructions provided over a large volume of data with accuracy and optimal computation.

5. Output.
In this stage, results are procured by the machine in a meaningful manner which can be inferred easily by the user. Output can be in the form of reports, graphs, videos, etc

6. Storage. 
This is the final step in which the obtained output and the data model data and all the useful information are saved for future use.
----

## **Feature Scaling**
technique to standardize the independent features present in the data in a fixed range. It is performed during the data pre-processing, to handle highly varying magnitudes or values or units, this way, no feature can dominate others. 

  * If feature scaling is not done, then a machine learning algorithm tends to weigh greater values, higher and consider smaller values as the lower values, regardless of the unit of the values.

  * Standardization replaces the values with their Z scores. 
  $$
  z=\frac{x-\mu}{\sigma} 
  $$

Techniques to perform Feature Scaling:
  - Min-Max Normalization: This technique re-scales a feature or observation value with distribution value between 0 and 1.
  $$
  X_{\text {new }}=\frac{X_{i}-\min (X)}{\max (x)-\min (X)}
  $$
  - Standardization: It is a very effective technique which re-scales a feature value so that it has distribution with 0 mean value and variance equals to 1.
  $$
  X_{\text {new }}=\frac{X_{i}-X_{\text {mean }}}{\text { Standard Deviation }}
  $$

Once the model is trained, an N-dimensional (where N is the no. of features present in the dataset) graph with data points from the given dataset, can be created. 

Prediction of the class of new data points: 

The model calculates the distance of this data point from the centroid of each class group. Finally, this data point will belong to that class, which will have a minimum centroid distance from it. 
The distance can be calculated between centroid and data point using these methods- 

  * Euclidean Distance: It is the square root of the sum of squares of differences between the coordinates of data point and centroid of each class. Where x is Data Point value, y is Centroid value and k is num of feature values.
  $$
  d(x, y)=\sqrt[r]{\sum_{k=1}^{n}\left(x_{k}-y_{k}\right)^{r}}
  $$
  * Manhattan Distance: It is calculated as the sum of absolute differences between the coordinates (feature values) of data point and centroid of each class. 
  $$
  d(x, y)=\sum_{k=1}^{n}\left|x_{k}-y_{k}\right|  
  $$
----

## **Label Encoding**
refers to converting the labels into a numeric form so as to convert them into the machine-readable form

**Limitation of label Encoding:**

- Label encoding may lead to the generation of priority issues in the training of data sets. A label with a high value may be considered to have high priority than a label having a lower value.

One approach to solve this problem can be label encoding where we will assign a numerical value to these labels

One Hot Encoding:
- In this technique, the categorical parameters will prepare separate columns for all labels. So, wherever there is an X, the value will be 1 in X column and 0 in Y column, and vice-versa.
----

## **Imbalanced Data Distribution**
Generally happens when observations in one of the class are much higher or lower than the other classes. Standard ML techniques such as Decision Tree and Logistic Regression have a bias towards the majority class, and they tend to ignore the minority class. 
- In this case, our model becomes more prone to the case when minority class has negligible or very lesser recall.

SMOTE (Synthetic Minority Oversampling Technique) – Oversampling:  
Aims to balance class distribution by randomly increasing minority class examples by replicating them. SMOTE synthesises new minority instances between existing minority instances. It generates the virtual training records by linear interpolation for the minority class. 

These synthetic training records are generated by randomly selecting one or more of the k-nearest neighbors for each example in the minority class. After the oversampling process, the data is reconstructed and several classification models can be applied for the processed data.

1. **Setting the minority class set A**, for each $ x \in A $, the k-nearest neighbors of x are obtained by calculating the Euclidean distance between x and all other sample in set A.
   
2. **The sampling rate N is set according to the imbalanced proportion.** For each $x \in A$, N examples (x1, x2, …, xn) are randomly selected from its k-nearest neighbors, and they construct the set $ A_1 $.
 
4. For each example $x_k \in A_1$ (k=1, 2, …, N), the following formula is used to generate a new example: $x' = x + rand(0, 1) * \mid x - x_k \mid$ in which rand(0, 1) represents the random number between 0 and 1.

NearMiss Algorithm – Undersampling:
Is an under-sampling technique. It aims to balance class distribution by randomly eliminating majority class examples. When instances of two different classes are very close to each other, we remove the instances of the majority class to increase the spaces between the two classes. 

To prevent problem of information loss in most under-sampling techniques, near-neighbor methods are widely used. The basic intuition about the working of near-neighbor methods is as follows:

1. The method first finds the distances between all instances of the majority class and the instances of the minority class. Here, majority class is to be under-sampled.
2. Then, n instances of the majority class that have the smallest distances to those in the minority class are selected.
3. If there are k instances in the minority class, the nearest method will result in k*n instances of the majority class.
----

## **Dummy Variables**

In statistics, especially in regression models, we can’t use categorical data directly, it needs to numerical attributes.  
One hot encoding is used in regression models following label encoding, if there are n number of categories in categorical attribute, n new attributes will be created. These attributes are called Dummy Variables. Hence, dummy variables are “proxy” variables for categorical data in regression models. 

**Dummy Variable Trap:**  

The Dummy variable trap is a scenario where there are attributes that are highly correlated (Multicollinear) and one variable predicts the value of others. When we use one-hot encoding for handling the categorical data, then one dummy variable (attribute) can be predicted with the help of other dummy variables.  
Hence, one dummy variable is highly correlated with other dummy variables. Using all dummy variables for regression models leads to a dummy variable trap. So, the regression models should be designed to exclude one dummy variable. 

**For Example:**   
Let’s consider the case of gender having two values male (0 or 1) and female (1 or 0). Including both the dummy variable can cause redundancy because if a person is not male in such case that person is a female, hence, we don’t need to use both the variables in regression models. This will protect us from the dummy variable trap.


## **Data Distribution** :

Normal distribution:  
In probability theory, normal or Gaussian distribution is a continuous probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. 

- Normal distributions used in statistics and are often used to represent real-valued random variables.  
  
- has two parameters: &mu; the mean, wich is the central tendency of the distribution, and &sigma; the standard deviation that is a measure of variability. It defines the width of the normal distribution.
  
- The standard deviation determines how far away from the mean the values tend to fall. It represents the typical distance between the observations and the average.
----

## **Data Preprocessing** :

For achieving better results from the applied model in Machine Learning projects the format of the data has to be in a proper manner. 

Another aspect is that the data set should be formatted in such a way that more than one Machine Learning and Deep Learning algorithm are executed in one data set, and best out of them is chosen.

1. Rescale Data  
   When our data is comprised of attributes with varying scales, many machine learning algorithms can benefit from rescaling the attributes to all have the same scale.

   This is useful for optimization algorithms used in the core of machine learning algorithms like gradient descent.

   It is also useful for algorithms that weight inputs like regression and neural networks and algorithms that use distance measures like K-Nearest Neighbors.

2. Binarize Data  
   We can transform our data using a binary threshold. All values above the threshold are marked 1 and all equal to or below are marked as 0.
   
   It can be useful when you have probabilities that you want to make crisp values. It is also useful when feature engineering and you want to add new features that indicate something meaningful.

3. Standardize Data  
   Standardization is a useful technique to transform attributes with a Gaussian distribution and differing means and standard deviations to a standard Gaussian distribution with a mean of 0 and a standard deviation of 1.
