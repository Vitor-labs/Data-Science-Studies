# Final Transformations Steps

## Encoding Categorical Features

Involves transforming categorical data into integer format, enabling its utilization in various models. Categorical data typically exists in the form of strings or object data types. Here how to Encode Categorical Features

1. Ordinal Encoding

When converting ordinal data to numeric form, it’s crucial to preserve the inherent order. In this process, each category is assigned a numerical value ranging from 0 to the total number of categories. 

2. Nominal Encoding

Nominal data lacks any inherent order. Encoding categories in an ordinal manner can mislead machine learning algorithms into assigning unwarranted importance when, in fact, the data is nominal and lacks such inherent order. For nominal data, a better approach involves transforming each category into a distinct column and assigning binary values (0 or 1) based on the presence of the respective category. Consequently, this transformation increases the number of features, with each category represented as a separate column

## Data Splitting

In the realm of data science and machine learning, data splitting is a crucial step. It involves partitioning the given dataset into two or more subsets and facilitating model training, validation, and testing. This process is fundamental, especially when building models reliant on the dataset. Typically, we divide the main dataset into two or three parts to achieve this [18].
How does Data Splitting work?

When engaged in supervised machine learning tasks, it’s advisable to partition the data into three distinct sets: the training set, the testing set, and the validation set. But what exactly does this entail?

- Training Set: This subset of the main dataset is utilized to educate the model, enabling it to grasp patterns and relationships within the data for accurate predictions. When selecting training data from the entire dataset, it’s essential to prioritize high data representativeness, ensuring an adequate representation for each class. Additionally, the quality of the extracted data should encompass impartiality, as biased data could compromise the accuracy of the model [18].

- Validation Set: This set is used to understand the performance of the model in comparison to different models and hyperparameter choices. During the process of constructing a machine learning model, our approach typically involves training multiple models by adjusting parameters or employing various algorithms. For instance, while developing a decision tree model for our dataset, we engaged in hyperparameter tuning, revealing multiple well-performing models under varying conditions. Consequently, the task at hand is to select the optimal model by considering different parameters. A critical observation is that employing the same data for both training and model tuning can result in overfitting, rendering the model incapable of generalization. This is where the validation set plays a crucial role, serving as independent and unbiased data. It facilitates a fair comparison of model performance, aiding in the selection of the best model algorithm or parameters. Once this data aids in identifying the most promising model and parameter combinations, we proceed to put the model into production, estimating its performance. However, it’s advisable not to employ the test data for evaluating the model before finalizing the optimal choice.

- Test set: As mentioned earlier, following the steps of training, validation, and model selection, the next phase involves putting the selected model into production after evaluating its performance on a specific subset of data known as the test set. Exercise caution during this phase, as premature execution can result in overfitting, yielding an unreliable model performance. The test set should be employed as the ultimate evaluation stage, once validation set usage is concluded, and the final model is chosen