## <center> **Measures** </center> 

### <u>Mean</u>: 
The sample mean is the arithmetic mean of a set of sample data, given by:
$$
    x̄ = \frac{x_1 + x_2 + ... + x_n}{n} = \frac{\sum\limits_{i=1}^n{x_i}}{n}
$$
- where $ x_i $ is the $ i^{th} $ data value and $ n $ is the sample size.

The population mean is the arithmetic mean of all values in the population, given by:
$$
    \mu = \frac{x_1 + x_2 + ... + x_n}{N} = \frac{\sum\limits_{i=1}^n{x_i}}{N}
$$
- where $ x_i $ is the $ i^{th} $ data value and $ N $ is the population size.

The weighted mean is the mean of a data set in which each data value in the set does not hold the same relative importance, given by:
$$
    x̄ = \frac{\sum(x_i \cdot w_i)}{\sum w_i} 
$$
- where $ x_i $ is the $ i^{th} $ data value and $ w_i $ is the weight of the $ i^{th} $ data value.


### <u>Median</u>: 
the median is the middle value in the data set, maibe this value isn't a data-set value.


### <u>Mode</u>: 
the most observed value in the data set, it cam be unimodal, tha means only one value occurs most often. Bimodal, Exactly two values occur equally often. And multimodal, more than two values occur equally often.
* a data set could have no mode.
---

## <center> Which measure use </center>

- for nominal data, the mode is the best.
- for ordinal data, either the mode or the mean.
- for numeric data, the median is the best.
- for symmetric numeric data, the mean can be used.

### <u>Skewness and the Hildebrand rule</u>:
to know if the data is symmetric enough to use the mean he Hildebrand rule is frequently used, defined as:
$$
    H = \frac{x̄ - \~{x}}{s}
$$
* Where $ x̄ $ is the sample mean, $ \~{x} $  is the sample median, and $ s $ is the sample standar deviation.
* if $ |H| < 0.2 $, the the data are sufficiently symmetric.

## <center> Measures for Relative Position </center> 
### <u>Percentiles</u>: 
To calculate a value's relative position, we can divide the data into equals parts and state in which part the value lies, dividing into 100 parts is called percentiles.

* to find the data value for the $ P^{th} $ percentile
$$
   I = n \cdot \frac{P}{100}
$$
* where $ I $ is the location of the $ P^{th} $ percentile in the ordered array of data values, $ n $ is the number of data values in the sample, and $ P $ stands for the  $ P^{th} $ percentile

$ P^{th} $ Percentile of a Data Value: the $ P^{th} $ of a particular value in a data set is given by:
$$
    P = \frac{I}{n} \cdot 100
$$
* $ P $ is the percentile rounded to the nearest whole number, $ I $ is the number of values in the data set $ \le $ to the given value, and $ n $ is the number of values in the sample.

### <u>Quartiles</u>: 
Are used in a numerical description, aptly called the five-number summary because it contains five numbers.
* The minimum value
* $ Q_1 $ = First Quartile (or the median): 25% of the data are $ \le $ to this value.
* $ Q_2 $ = Second Quartile: 50% of the data are $ \le $ to this value.
* $ Q_3 $ = Third Quartile: 75% of the data are $ \le $ to this value.
* the maximum value.  
 
To represent this graphically, we can use the box plot graph, also know as box-and-whisker plot.

### <u>Standard Scores</u>:
To compare two data values from different populations by comparing their respective percentiles. this score, also know as z-score tells how many standard deviations the value is away from the mean. 
* for population: 
    $$
        z = \frac{x-\mu}{\sigma}
    $$
  * where, $ x $ is the value of interest, $ \mu $ is the mean, and $ \sigma $ is the standard deviation.

* for sample:
    $$
        z = \frac{x - x̄}{s}
    $$
  * where, $ x $ is the value of interest, x̄ is the mean, and $ s $ is the standard deviation.