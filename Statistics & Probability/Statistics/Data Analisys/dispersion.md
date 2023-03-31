## <center> Dispersions. </center> 

### <u>Measures of Spread</u>
A measure of dispersion is how much we can expect a value to differ from the measure of center.

1. Range: its the maximum value - minimum value, not a robust measure.
2. Variance: is an average distance that values in a set lie from the mean. While not the actual average, the variance is usually very close to the average 
   1. Population Variance: is the average squared distance of the population values from the mean:
   $$
       \sigma^2 = \frac{\sum(x_i - \mu)^2}{N}
   $$
   * Here, $ x_i $ is the $ i^{th} $ value in the population, $ \mu $ is the population mean, and $ N $ is the number o values in the population.
   2. Sample Variance: is the adjusted average squared distance of the data values from the sample mean:
   $$
       s^2 = \frac{\sum(x_i - x̄)^2}{n - 1}
   $$
   * Here, $ x_i $ is the $ i^{th} $ value in the sample, x̄ is the sample mean, and $ n $ is the sample size.
3. Standard Deviaiton: is the square root of the variance.
$$
    \sigma = \sqrt{\sigma^2} \\
    s = \sqrt{s^2}
$$
4. Coefficient of Variation: is the ratio of the standard deviation to the mean as a percentage, its used to compare dispersions for two variables. For population is
$$
    CV = \frac{s}{ x̄}\times 100%
$$
* Here, $ s $ is the sample standard deviation and $ x̄ $ is the sample mean.
5. Empirical Rule: when the data follow a bell-shaped distribution, an intersting pattern emerges in the data values:
   * approximately 68% of the data values lie within one standard deviation of the mean.
   * 95% of the data values at two deviations: $ \mu \plusmn 2 \sigma $
   * 99.7% of the data values at three deviations: $ \mu \plusmn 3 \sigma $
6. Chebyshev's Theorem: the proportion of data that lie within K standard deviations of the mean is at least: 
$$ 
    1-\frac{1}{k^2} 
$$ 
----
### <u>Data Estimation</u>:
Empirical Rule x Cherbyshev Theorem: since the empirical rule requires the bell-shaped distribution, the Cherbyshev Theorem is more precise, and allways works. But, the Empirical Rule tends to give better estimates.

### <u>Distributions</u>:
* Normal Distribution: alson known as Gaussian distribution, is a type of continuous probability distribution for a real-valued random variable. The distribution is the bell-shaped graph and the general form of its probability density function is
$$
    f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{\xi-\mu}{\sigma})^2}
$$
* Here, $ \mu $  is the mean or expectation of the distribution (and also its median and mode), the $ \sigma $ is the standard deviation. The variance of the distribution is $ 2 \sigma ^{2}. $ 