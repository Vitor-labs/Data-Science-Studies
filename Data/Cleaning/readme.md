
### **Data Cleaning** :
*“Better data beats fancier algorithms”*. Steps involved in Data Cleaning: 

1. Removal of unwanted observations 
   This includes deleting duplicate/ redundant or irrelevant values from your dataset. 
   - Redundant observations alter the efficiency by a great extent as the data repeats and  may add towards the correct side or towards the incorrect side, thereby producing unfaithful results.

2. Fixing Structural errors 
    The errors that arise during measurement, transfer of data, or other similar situations are called structural errors. Structural errors include typos in the name of features, the same attribute with a different name, mislabeled classes, i.e. separate classes that should really be the same, or inconsistent capitalization. 

3. Managing Unwanted outliers 
    Outliers can cause problems with certain types of models. For example, linear regression models are less robust to outliers than decision tree models. Generally, we should not remove outliers until we have a legitimate reason to remove them. Sometimes, removing them improves performance, sometimes not. So, one must have a good reason to remove the outlier, such as suspicious measurements that are unlikely to be part of real data.

4. Handling missing data 
    Missing data is a deceptively tricky issue in machine learning. We cannot just ignore or remove the missing observation. They must be handled carefully as they can be an indication of something important. The two most common ways to deal with missing data are: 

    - Dropping observations with missing values. The fact that the value was missing may be informative in itself. Plus, in the real world, you often need to make predictions on new data even if some of the features are missing!
    
    - Imputing the missing values from past observations. Again, “missingness” is almost always informative in itself, and you should tell your algorithm if a value was missing. Even if you build a model to impute your values, you’re not adding any real information. You’re just reinforcing the patterns already provided by other features.

Some data cleansing tools 
1. Openrefine
2. Trifacta Wrangler
3. TIBCO Clarity
4. Cloudingo
5. IBM Infosphere Quality Stage
----

### **Feature Scaling** : 
technique to standardize the independent features present in the data in a fixed range. It is performed during the data pre-processing, to handle highly varying magnitudes or values or units, this way, no feature can dominate others. 

-  If feature scaling is not done, then a machine learning algorithm tends to weigh greater values, higher and consider smaller values as the lower values, regardless of the unit of the values.

- Standardization replaces the values with their Z scores. 
$$ z=\frac{x-\mu}{\sigma} $$

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

- Euclidean Distance: It is the square root of the sum of squares of differences between the coordinates of data point and centroid of each class. Where x is Data Point value, y is Centroid value and k is num of feature values.
$$
d(x, y)=\sqrt[r]{\sum_{k=1}^{n}\left(x_{k}-y_{k}\right)^{r}}
$$
- Manhattan Distance: It is calculated as the sum of absolute differences between the coordinates (feature values) of data point and centroid of each class. 
$$
d(x, y)=\sum_{k=1}^{n}\left|x_{k}-y_{k}\right|  
$$ 
----

### **Label Encoding** :
refers to converting the labels into a numeric form so as to convert them into the machine-readable form

**Limitation of label Encoding:**

- Label encoding may lead to the generation of priority issues in the training of data sets. A label with a high value may be considered to have high priority than a label having a lower value.

One approach to solve this problem can be label encoding where we will assign a numerical value to these labels

One Hot Encoding:
- In this technique, the categorical parameters will prepare separate columns for all labels. So, wherever there is an X, the value will be 1 in X column and 0 in Y column, and vice-versa.
----

### **Imbalanced Data Distribution** :
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

### **Dummy Variables** : 

In statistics, especially in regression models, we can’t use categorical data directly, it needs to numerical attributes.  
One hot encoding is used in regression models following label encoding, if there are n number of categories in categorical attribute, n new attributes will be created. These attributes are called Dummy Variables. Hence, dummy variables are “proxy” variables for categorical data in regression models. 

**Dummy Variable Trap:**  

The Dummy variable trap is a scenario where there are attributes that are highly correlated (Multicollinear) and one variable predicts the value of others. When we use one-hot encoding for handling the categorical data, then one dummy variable (attribute) can be predicted with the help of other dummy variables.  
Hence, one dummy variable is highly correlated with other dummy variables. Using all dummy variables for regression models leads to a dummy variable trap. So, the regression models should be designed to exclude one dummy variable. 

**For Example:**   
Let’s consider the case of gender having two values male (0 or 1) and female (1 or 0). Including both the dummy variable can cause redundancy because if a person is not male in such case that person is a female, hence, we don’t need to use both the variables in regression models. This will protect us from the dummy variable trap.
