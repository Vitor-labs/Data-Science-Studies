# Data Transformation

Data transformation involves technically converting data from one format, standard, or structure to another, without changing the dataset’s content. This is typically done to prepare the data for consumption by an application or user, or to enhance data quality.

### Table of Contents
- [Data Transformation](#data-transformation)
    - [Table of Contents](#table-of-contents)
  - [Data aggregation](#data-aggregation)
  - [Feature Engineering](#feature-engineering)
    - [Scaling](#scaling)
    - [Normalization](#normalization)
    - [Standardization](#standardization)

## Data aggregation
method used to present data in a summarized form. Given the likelihood of data originating from diverse sources, combining all incoming data into a cohesive description is the essence of data aggregation. 

  - pandas.groupby(): Grouping involves breaking down a dataset into smaller subsets depending on specific variables. This function is highly versatile and allows for the grouping of data based on one or more columns. 
  ```python
  new_df = df.groupby(['site', 'name'])[['total_sales', 'score']].sum().query('site == "amazon" & score > 0')
  ```
  - pandas.pivot_table(): Multidimensional form of GroupBy aggregation. When using a pivot table, input data in a column-wise format is organized into a two-dimensional table, offering a multidimensional summary of the information. 
  ```python
  agg_selected_region_platform = pd.pivot_table(data=reference_df, index='platform', values = ['na_sales', 'eu_sales', 'jp_sales'], aggfunc = 'sum').sort_values(by='jp_sales')
  ```

## Feature Engineering

A pivotal stage in the creation of accurate and efficient machine learning models. A significant facet of feature engineering involves scaling, normalization, and standardization, encompassing the alteration of data to enhance its suitability for modeling. Employing these methods can enhance model accuracy, mitigate the influence of outliers, and ensure uniformity in data scale.

### Scaling

Crucial step in data preprocessing, aiming to standardize the values of features or variables within a dataset to a uniform scale. The primary objective is to ensure that all features have a fair influence on the model, avoiding the dominance of features with higher values. 
The necessity for feature scaling arises when working with datasets that encompass features having diverse ranges, units of measurement, or orders of magnitude. In such scenarios, discrepancies in feature values can introduce bias in model performance or hinder the learning process. Scaling promotes meaningful feature comparisons, enhances model convergence, and prevents specific features from dominating others solely based on their magnitude.
Certain machine learning algorithms exhibit sensitivity to feature scaling, whereas others remain mostly unaffected by it, here two exemples:

1. Gradient Descent Based Algorithms: algorithms that use gradient descent as an optimization technique (like linear regression, logistic regression, etc) require data to be scaled.

2. Distance-Based Algorithms: K-nearest neighbors (KNN), K-means clustering, and support vector machines (SVM), are highly influenced by the range of features. This is because these algorithms rely on calculating distances between data points to ascertain their similarity.

### Normalization

Approach to standardize feature values within a dataset to a consistent scale. This is carried out to streamline data analysis and modeling, mitigating the influence of disparate scales on machine learning model accuracy 

### Standardization

Some form of scaling, involves centering values around the mean and adjusting the standard deviation to one unit. This process involves eliminating the mean and adjusting the scale to unit variance, ultimately resulting in a mean of 0 and a standard deviation of 1. This aligns the data with a standard normal distribution.