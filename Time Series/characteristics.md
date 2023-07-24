# <CENTER> **Types & characteristics of Time Series** </CENTER>

### Some particular types of time series:

1. White Noise: unpredictable data, follows no pattern, without repetition.
   - The series is white noise if the variables are independent and identically distributed with zero mean. Therefore, all variables have the same variance (σ²) and each value has a zero correlation with the other values ​​in the series.

2. Random Walk: is different from a list of random numbers because the next value in the sequence is a modification of the previous value in the sequence.

   - the values tend to persist over time and the differences between periods are simply white noise. Where: $P_{t}=P_{t-1}+\epsilon_{t}$ 
  
   And the the residuals are assumed to be white noises: $\epsilon_{t} \sim WN(\mu, \sigma²)$
----

### Some characteristics of time series:

1. Stationarity: implies that taking consecutive samples of data with the same sizes, should give the save covariance, regardless of the starting point.
   - for Covariance Stationarity, we should have: a constante mean $( \mu )$ and variance $( \sigma² )$, and for that a constant covariance between periods with identical distances $(Cov(x_n, x_{n+k}) = Cov(x_m, x_{m+k}))$

   - Dickey-Fuller Test: verify if a AR models has or not a unitary root.

   - time series with trends, or with seasonality, are not stationary 
   
2. Seazonality: made by 3 effects, trend (pattern througout the data), seasonal (cyclical effects) and residual (error on prediction). The most simple type of this decomposition is the naive that make a linear relationship between those 3 parts. 
That can be splited in two forms
   - Additive: that assumes that the observated data is the sum of the 3 effects, pretty rare for actual time series to have constant crest and trough values.
   - Multiplicative: assumes that the observated data is the multiplication of the 3 effects

Seasonality can be removed from the series. This process is called Seasonal Adjustment, or Deseasonalizing. 

1. Auto Correlation: Correlation p(x,y) measures the similarity in the change of values of two series, in this case we only have a single variable. Auto correlation measures the correlation between a sequence and itself.
   
   - The Auto Correlation Function measures the correlation between diferent lags. It may capture secondary effects.

   - The Partial Auto Correlation Function measures only the direct relationship between the series and it's lag. It cancels out all additional channels a previous period value affects the present one.

