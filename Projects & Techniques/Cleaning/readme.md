### Table of Contents
- [**Data Cleaning**](#data-cleaning)
- [Seeding Data Techniques](#seeding-data-techniques)

## **Data Cleaning**
*“Better data beats fancier algorithms”*. Steps involved in Data Cleaning: 

1. Removal of unwanted observations 
   This includes deleting duplicate redundant or irrelevant values from your dataset.  Redundant observations alter the efficiency by a great extent as the data repeats and  may add towards the correct side or towards the incorrect side, thereby producing unfaithful results.

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

## Seeding Data Techniques

1. Analyse the distribution of data. To visualize the distribution plot, using seaborn:
```python
sns.distplot(dataset['variable-to-visualize'])
```
