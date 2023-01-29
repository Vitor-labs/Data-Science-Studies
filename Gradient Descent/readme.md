# <center> Gradient Descent </center>

Gradient Descent is a first-order iterative optimization algorithm used for finding a local minimum of a differentiable function, minimizing the cost function in various machine learning algorithms. It is basically used for updating the parameters of the learning model.

-  The idea is to take repeated steps in the opposite direction of the gradient (or approximate gradient) of the function at the current point, because this is the direction of steepest descent, tweaking parameters iteratively in order to minimize the cost function.
-  When using Gradient Descent, we should ensure that all features have a similar scale, or else it will take much longer to converge.

## **Types of gradient Descent**:

1. **_Batch Gradient Descent_**: This type of processes all the training examples for each iteration, but, if the number of training examples is large, then batch gradient descent is computationally very expensive. 
    - Let hθ(x) be the hypothesis for linear regression. Then, the cost function is given by: Let Σ represents the sum of all training examples from i=1 to m.
  
    - Where xj(i) Represents the jth feature of the ith training example. So if m is very large(e.g. 5 million training samples), then it takes hours or even days to converge to the global minimum.That’s why for large datasets, it is not recommended to use batch gradient descent as it slows down the learning.
  
    - Algorithm for batch gradient descent
   ``` 
    Jtrain(θ) = (1/2m) Σ( hθ(x(i))  - y(i))2
    Repeat {
        θj = θj – (learning rate/m) * Σ( hθ(x(i))  - y(i))xj(i)
        For every j =0 …n 
    }
    ```
  
2. **_Stochastic Gradient Descent_**: This type processes 1 training example per iteration. Hence, the parameters are being updated even after one iteration in which only a single example has been processed. When the number of training examples is large, even then it processes only one example which can be additional overhead for the system as the number of iterations will be quite large.
    - Algorithm for stochastic gradient descent: 1) Randomly shuffle the data set so that the parameters can be trained evenly for each type of data. 2) As mentioned above, it takes into consideration one example per iteration.
    ``` 
    Let (x(i),y(i)) be the training example
    Cost(θ, (x(i),y(i))) = (1/2) Σ( hθ(x(i))  - y(i))2

    Jtrain(θ) = (1/m) Σ Cost(θ, (x(i),y(i)))

    Repeat {
        For i=1 to m{
            θj = θj – (learning rate) * Σ( hθ(x(i))  - y(i))xj(i)
            For every j =0 …n
        } 
    }
    ``` 

3. **_Mini Batch gradient descent_**:  Here b examples where b < m are processed per iteration. So even if the number of training examples is large, it is processed in batches of b training examples in one go. Thus, it works for larger training examples and that too with lesser number of iterations. Where m = number of training examples and n = number of features. 
   - Note that if b = m, then mini batch gradient descent will behave similarly to batch gradient descent.
   - Algorithm for mini batch gradient descent: Say b be the no of examples in one batch, where b < m. Assume b = 10, m = 100;
   - Note: However we can adjust the batch size. It is generally kept as power of 2. The reason behind it is because some hardware such as GPUs achieve better run time with common batch sizes such as power of 2.
    ```
    Repeat {
        For i=1,11, 21,…..,91
            Let Σ be the summation from i to i+9 represented by k. 

            θj = θj – (learning rate/size of (b) ) * Σ( hθ(x(k))  - y(k))xj(k)
                For every j =0 …n
    }
    ```
----
## **Convergence trends in different variants of Gradient Descents**:

In case of Batch Gradient Descent, the algorithm follows a straight path towards the minimum. If the cost function is convex, then it converges to a global minimum and if the cost function is not convex, then it converges to a local minimum. Here the learning rate is typically held constant.

In case of stochastic gradient Descent and mini-batch gradient descent, the algorithm does not converge but keeps on fluctuating around the global minimum. Therefore in order to make it converge, we have to slowly change the learning rate. However the convergence of Stochastic gradient descent is much noisier as in one iteration, it processes only one training example.



