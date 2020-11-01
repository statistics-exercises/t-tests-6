import numpy as np
import scipy.stats

def testStatistic( data, mu ) : 
  # Your code to compute the testStatistic that is described
  # in the text on the right should be calculated here
  
  
def pvalue( data, mu ) :
  T = testStatistic(data, mu )
  # You should add code here that uses the T value that is returned from 
  # testStatistic to determine the p-value for the hypothesis test.
  

# The code from here should not need to be modified
data = np.array([ 0.59, 3.07, 3.14, 2.11, -0.25, 2.83, 3.59, 1.74, 3.06])
print("The null hypothesis is that the data is a set of samples from a distribution")
print("with an expectation of 2")
print("The alternative hypothsis is that the data is a set of samples from a distribution")
print("with an expectation that is greater than 2")
print("The p-value for this hypothesis test is", pvalue(data, 2) )
