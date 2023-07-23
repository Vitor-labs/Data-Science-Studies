# <CENTER> **TIME-SERIES: PREPROCESSING** </CENTER>

1. **Dealing with missing Data**.
   
   This case is more complex than other analysis, by the fact that values between consecutive periods, usualy affect each other.

   in this cases you can just adjust the frequency, like reducing the periods or increasing then.

   you could try to aggregate the data, by some averange of the individual values.

   by increasing the frequecy, this creates new time periods, with no values assigned to then, in this cases you have to approximate missing values.

2. **Maintenance of Cronological Order**
   
   Time-Series Data requires a maintece of this order to be analysed, but from a machine learning perspective, this is a inconvenience, because we can't just shuffle the data freely.

   in this case we can pick a cut off point for training and testing.

3. **Strandard Distributions**
   
   Time Series graphs do not follow any of familiar strandard distributions from statistics and probability. This is because this type of data do not satisfies the Gauss-Markov assumptions.

   Instead, we assume that past pattern in the values will repeat in the future.
