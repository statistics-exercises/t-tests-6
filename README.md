# One-tailed t-tests

You hopefully did not find the previous exercise too difficult.  For the most part, the code that you will have written will have been identical to the code that you were writing last week.  The only small difference is that this week the t-distribution is used in place of the normal distribution as we only have a small number of data points.

To consolidate what we have just done lets now do a one-tailed test rather than a two-tailed test.  In particular, I would like you to __test whether the 9 points in the NumPy array called `data` are samples from a normal distribution with an expectation of two or if there is sufficient evidence to suppose that the expectation of the distribution is less than two.__ 

To get you started in completing the exercise I have written two functions for you which you must complete:

1. `testStatistic` - Two variables are passed to this function.  `data` is a NumPy array that contains N data points, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis.  This function should return the test statistic, which is calculated in the usual way.
2. `pvalue` - Two variables are passed to this function.  `data` is a NumPy array that contains N data points, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis.  The function calls `testStatistic` to the test statistic.  You should modify it so that the function returns the __p-value__ based on the value of the __statistic__.
