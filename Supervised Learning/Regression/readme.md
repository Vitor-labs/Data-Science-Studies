# <center> **Regression** :
Regression is chosen when the output variable is a real or continuous value,  it's used to model and understand the relationship between a dependent variable and one or more independent variables.

The main types of regression techniques:

1. **Simple Regression:** Most basic regression, used to model a linear relationship between a single dependent variable and one or more independent variables.
2. **Polynomial Regression:** Extension of simple regression, used to model a non-linear relationship between the dependent variable and independent variables.
3. **Decision Tree Regression:** This is a non-parametric method used to model a decision tree to predict a continuous outcome.
4. **Random Forest Regression:** This is an ensemble method that combines multiple decision trees to improve the predictive performance of the model.
5. **Support Vector Regression (SVR):** This is a linear model for regression tasks, it can also handle non-linear relationships by mapping the data into a higher dimensional space.
6. **Ridge Regression:** This is a regularized linear regression model, it tries to reduce the model complexity by adding a penalty term to the cost function
8. **Lasso Regression:** This is another regularized linear regression model, it works by adding a penalty term to the cost function, but it tends to zero out some features’ coefficients, which makes it useful for feature selection.
9. **Neural Network Regression:** This is a non-linear model that uses a neural network to model the relationship between the independent and dependent variables.

----
### **[Simple Linear Regression](https://en.wikipedia.org/wiki/Simple_linear_regression)** :    
Here we have an quantitative variable as response, the formula:
$$ Y=\beta_{0}+\beta_{1}X $$
- Where &beta;<sub>1</sub> is a parameter witch can be positive or negative, that corrects the slope.
- to find the parameters we need to minimize a certain error function
- for linear regression we minimize the sun of square errors

**Error Function**: e<sub>i</sub> = y<sub>i</sub> - ŷ<sub>i</sub>  
- Where y<sub>i</sub> is the real number and ŷ<sub>i</sub> is the prediction, 

Finding coefficients
- for &beta;<sub>1</sub>: 
  $$
  \beta_{1}=\frac{\sum_{i=1}^{n} (x_{1}-{\bar{x}}) (y_{1}-{\bar{y}})} {\sum_{i=1}^{n} (x_{1}-{\bar{x}})^{2} }
  $$
- for &beta;<sub>0</sub>:
   $$ \beta_{0}=\bar{y}-\beta_{1}\bar{x} $$
- Where $\bar{x}$ is the mean of the independent variables and $\bar{y}$ is the mean of the target

1. Relevance of coefficients
    - p-value: quantify statistical significance, this value tells if an null hypothesis can be rejected or not.

2. Accuracy of the linear model
    - for this, usually is used the **Residual Standard Error**, where, the smaller the value, better it is.
    $$ RSE =\sqrt{\frac{1}{n-2}RSS} $$
    - where RSS is the **Residual Sum of Squares** also known as the sum of squared estimate of errors, is the sum of the squares of residuals (deviations predicted from actual empirical values of data):
    $$ \sum_{i=1}^{n}(y_{i}-\hat{y}_{i})^{2} $$
    - we also use the Coefficient of determination $R^{2}$, that measures how well data points fit a line or curve and the proportion of variability explained by a feature X. Where:
    $$ R^{2}=\frac{TSS-RSS}{TSS}=1-\frac{RSS}{RSS}
    $$
    - Where TSS is the **Total Sum of Squares**. Is a quantity that appears as part of a standard way of presenting results of such analyses. For a set of observations, $y_{i}, i ≤ n$, it is defined as the sum over all squared differences between the observations and their overall mean $\bar{y}$. For TSS:
    $$ \sum{}(y_{i}-\hat{y}_{i})^2 $$

----
### **Other types of Regressions** :

**Multiple Linear Regression**: very similar to the previous one, we simple extend the model to fit more features, with his oun parameter for p predictions. $Y=\beta_{0}+\beta_{1}X_{1}+\beta_{2}X_{2}+...+\beta_{p}X_{p}$
- To Assess a model of Multiple Linear Regression we use the F statistic, where p is the total of predictions and n is the total of data points.
  $$ F=\frac{\frac{TSS-RSS}{p}}{\frac{RSS}{(n-p-1)}} $$
- if F is much greater (<<) than 1, then there is a strong relationship, for a small dataset, with a couple of houndreds of data points, F has to be way larger than 1. 

**Polynomial regression**: fits a nonlinear relationship between the value of x and the corresponding conditional mean of y, denoted $ E(y |x). $ The goal is to model the expected value of a dependent variable y in regards to the independent variable x, modelled as an nth degree polynomial in x. 
- used for curvilinear data
$$ l = {\displaystyle y=\beta _{0}+\beta _{1}x+\beta _{2}x^{2}+\beta _{3}x^{3}+\cdots +\beta _{n}x^{n}+\varepsilon .\,} $$
- conditional mean of a random variable is its expected value – the value it would take “on average” over an arbitrarily large number of occurrences – given that a certain set of "conditions" is known to occur.

**Stepwise regression**: used for fitting regression models with predictive models. It is carried out automatically. With each step, the variable is added or subtracted from the set of explanatory variables. The approaches for stepwise regression are forward selection, backward elimination, and bidirectional elimination. The formula for stepwise regression is $b_{j.std} = b_{j}(s_{x} * s_{y}^{-1})$.

**Ridge regression**: used for analyzing multiple regression data. When multicollinearity occurs, least squares estimates are unbiased. A degree of bias is added to the regression estimates, and as a result, ridge regression reduces the standard errors. The formula for ridge regression is $\beta = (X^{T}X + \lambda * I)^{-1}X^{T}y$

**Lasso regression**: method that performs both variable selection and regularization. Lasso regression uses soft thresholding. Lasso regression selects only a subset of the provided covariates for use in the final model. Lasso regression is 
$$ N^{-1}\sum^{N}_{i=1}f(x_{i}, y_{I}, \alpha, \beta) $$

**ElasticNet regression**: is a regularized regression method that linearly combines the penalties of the lasso and ridge methods. ElasticNet regression is used for support vector machines, metric learning, and portfolio optimization. The penalty function is given by:
$$||\beta||_{1} = \sum^{p}_{j=1}|\beta_{j}| $$

----


