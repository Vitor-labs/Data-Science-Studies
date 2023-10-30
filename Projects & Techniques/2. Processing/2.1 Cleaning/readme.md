### Table of Contents
- [**Data Cleaning**](#data-cleaning)
- [Dropping Duplicated Values](#dropping-duplicated-values)
- [Seeding Data Techniques](#seeding-data-techniques)

## **Data Cleaning**
*“Better data beats fancier algorithms”*. Steps involved in Data Cleaning: 

1. Removal of unwanted observations 
   This includes deleting duplicate redundant or irrelevant values from your dataset. Redundant observations alter the efficiency by a great extent as the data repeats and may add towards the correct side or towards the incorrect side, thereby producing unfaithful results.

   - to find duplicated values with pandas, use
    ```python
   # Find duplicates
   duplicates = df[df.duplicated()]
   # Remove duplicates
   df = df.drop_duplicates()
   ```
   - in SQL
    ```sql
    -- Find duplicates
    SELECT * FROM table_name
    WHERE column1 = column2;

    -- Remove duplicates
    DELETE FROM table_name
    WHERE column1 = column2;
    ```

2. Fixing Structural errors 
    The errors that arise during measurement, transfer of data, or other similar situations, include typos in the name of features, the same attribute with a different name, mislabeled classes, i.e. separate classes that should really be the same, or inconsistent capitalization. 

3. Managing Unwanted outliers 
    Outliers can cause problems with certain types of models. Linear regression models are less robust to outliers than decision tree models. Generally, we should not remove outliers until we have a legitimate reason to remove them.

4. Handling missing data 
   Missing data cannot just be ignored or removed. They must be handled carefully as they can be an indication of something important. The two most common ways to deal with missing data are:
    
    - Trick to find missing values, this will sum the presences of null cells in
      ```python
      dataset.isnull().sum()
      ```

    - Dropping observations with missing values. The fact that the value was missing may be informative in itself. 
    
    - Imputing the missing values from past observations. Again, “missingness” is almost always informative in itself, and you should tell your algorithm if a value was missing.
----

## Dropping Unwanted Values

When cleaning and preprocessing data, it's important to remove unwanted observations, which can include deleting duplicate, redundant, or irrelevant values.

1. Removing Duplicates:
   - Duplicate Row Removal: Identify and remove rows that are exact duplicates of one another, retaining only one instance of each unique row.
   - Duplicate Column Removal: Identify and remove columns that contain duplicate or identical information.

2. Filtering Irrelevant Rows:
   - Row Filtering: Filter out rows that don't meet specific criteria or conditions relevant to your analysis. This is often done using conditional statements or filters.

3. Feature Selection:
   - Remove Redundant Features: Identify and remove columns that are highly correlated with other columns, as they may not provide additional information.
   - Irrelevant Feature Removal: Remove columns that do not contribute to the task at hand or have little predictive power.

4. Time-Series Data Truncation:
    In time-series data, you can truncate or filter data to a specific time frame, removing observations outside of that range.

## Outliers

Handling outliers is an important step in data preprocessing to ensure that extreme or erroneous data points do not unduly influence the results of your analysis or modeling. Here are some common techniques to handle outliers:

1. Visual Inspection:
   - Visualize the data using box plots, scatter plots, or histograms to identify outliers. This can help you understand the distribution and identify potential extreme values.

2. Z-Score or Standard Score:
   - Calculate the Z-score for each data point, which measures how many standard deviations the data point is from the mean. Typically, values with a Z-score greater than a certain threshold (e.g., ±3) are considered outliers and can be removed or transformed.

3. IQR (Interquartile Range) Method:
   - Use the IQR to identify outliers. Calculate the IQR (the range between the 75th and 25th percentiles), and consider values outside a certain multiple of the IQR (e.g., 1.5 times the IQR) as outliers.

4. Winsorization:
   - Winsorization involves capping extreme values by setting them to a specified percentile (e.g., 1st and 99th percentiles). This approach mitigates the impact of outliers without removing them entirely.

5. Trimming:
   - Remove a certain percentage of the data points with the highest and lowest values. This technique trims the dataset to remove outliers.

6. Log Transformation:
   - Apply a logarithmic transformation to the data, which can help normalize the distribution and reduce the impact of extreme values.

7. Robust Statistics:
   - Use robust statistical methods that are less sensitive to outliers. For example, the median and median absolute deviation (MAD) are robust alternatives to the mean and standard deviation.

8. Binning or Discretization:
   - Group data into bins or discrete categories, which can help to reduce the impact of extreme values.

9. Imputation:
   - Replace outliers with more reasonable values, which can be done using imputation techniques like mean, median, or regression-based imputation.

10. **Clustering and Segmentation:**
    - Segment the data into clusters and analyze each cluster separately, potentially reducing the impact of outliers in the overall analysis.

11. **Ensemble Methods:**
    - Use ensemble techniques like Random Forest, which are less sensitive to individual data points, to model the data.

12. **Anomaly Detection Algorithms:**
    - Employ dedicated anomaly detection algorithms, such as Isolation Forest, One-Class SVM, or Local Outlier Factor, to explicitly identify and handle outliers.

The choice of technique depends on the nature of the data and the specific goals of your analysis or modeling. It's important to carefully consider the impact of outlier handling on your results and to document the steps taken during preprocessing.


## Seeding Data Techniques

Handling missing data is an important aspect of data preprocessing in machine learning and data analysis. There are various techniques for seeding data to handle missing data

1. Analyse the distribution of data. To visualize the distribution plot, using seaborn:
```python
sns.distplot(dataset['variable-to-visualize'])

There are various techniques and methods to do some inputation 

1. Mean/Median/Mode Imputation:
   - Mean imputation: Replace missing values with the mean of the observed values in the same feature.
   - Median imputation: Replace missing values with the median of the observed values in the same feature.
   - Mode imputation: Replace missing categorical data with the mode (most frequent value) of the observed data in the same feature.

2. Forward Fill and Backward Fill:
   - Forward fill: Fill missing values with the previous known value in the sequence.
   - Backward fill: Fill missing values with the next known value in the sequence.

3. Multiple Imputation:
   - Generate multiple imputed datasets with different imputed values for the missing data. This helps account for uncertainty in imputation and is particularly useful for statistical analysis.

4. Model Imputation:
   - Use linear regression, K-Nearest Neighbors or a Random Forest to predict the missing values based on the relationship between the target variable and other features. Fit a linear model using non-missing data and predict the missing values. Random forests are robust and can handle both numerical and categorical data.
   - Train a neural network to predict missing values based on the available data. Deep learning models can capture complex relationships in the data.

5. Interpolation:
   - Use interpolation methods such as linear or polynomial interpolation to estimate missing values based on the trend in the available data points.

6. Missing Indicator:
   - Create a binary indicator variable that flags whether a data point is missing in a particular feature. This preserves the information about missingness, which can be useful in some cases.

7. Principal Component Analysis (PCA):
   - Use PCA to impute missing data by projecting the data into a lower-dimensional subspace and then reconstructing it. This can be particularly useful for high-dimensional data.

8. Hot Deck Imputation:
    - Assign missing values with values from randomly selected, similar records in the dataset, also known as "donor imputation."

9. Weighted Imputation:
    - Assign weights to observations based on their similarity to the observation with missing data. Use these weights to compute imputed values.

10. Expectation-Maximization (EM) Algorithm:
    - An iterative statistical algorithm that estimates missing values and underlying model parameters simultaneously.

The choice of imputation technique depends on the nature of the data, the amount of missing data, and the specific problem you are trying to solve. It's important to consider the potential impact of imputation on the analysis and modeling process, as well as the assumptions that different techniques make about the missing data mechanism.
```