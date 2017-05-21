# Statistical Tests Cheatsheet with Python and R

This is a cheatsheet for statistical tests that I need to do and how to do them in Python and R, respectively. 
It is organized by the problems to solve, each with an example of the problem, the Python solution, and the R solution.

A, B, C represent three different versions of a eCommerce website. 
- A test: test on a single case (e.g., Website Version A);
- AB test: test on two contrasting cases (e.g.,Website Version A v.s. B);
- ABC test: test on three contrasting cases (e.g., Website Version A, B, and C). This can be generalized to more than three cases.

Table of Contents
- [Tests of proportions](#tests-of-proportions)
	- [Single proportions](#single-proportions)
		- [A test](#a-test)
			- [Confidence interval](#confidence-interval)
			- [Hypothesis test](#hypothesis-test)
				- [z-test](#z-test)
				- [prop-test](#prop-test)
		- [AB test](#ab-test)
		- [ABC test](#abc-test)
	- [Multiple proportions](#multiple-proportions)
		- [A test](#a-test-1)
		- [AB test](#ab-test-1)
		- [ABC test](#abc-test-1)
- [Tests of means](#tests-of-means)
	- [A test](#a-test-2)
	- [AB test](#ab-test-2)
	- [ABC test](#abc-test-2)

## Tests of proportions
There are problems that concern single proportions and multiple proportions.
- An example of single proportions: the percentage of visitors to your website that clicked "Buy Now" (e.g., a 3% click rate).
- An example of multiple proportions: the percentages of visitors to your website from different countries (e.g., 60% US, 30% UK, 10% DE).

### Single proportions

#### A test 
Data say 526 out of 1000 visitors to your website clicked.

##### Confidence interval
Question: What is the confidence interval of the click rate?

###### Python
```py
>>> clicking_visitors = 526
>>> all_visitors = 1000
>>> confidence_interval_size = 0.95
>>> x = clicking_visitors
>>> n = all_visitors
>>> p_hat = x/n
>>> p_hat
0.526
>>> import numpy as np
>>> standard_error = np.sqrt(p_hat * (1-p_hat) / n)
>>> standard_error
0.015789996833438569
>>> alpha = 1 - confidence_interval_size
>>> alpha
0.050000000000000044
>>> 1 - alpha/2
0.975
>>> import scipy.stats
>>> z_critical = scipy.stats.norm.ppf(1 - alpha/2)
>>> z_critical
1.959963984540054
>>> confidence_interval = p_hat - z_critical*standard_error, p_hat + z_critical*standard_error
>>> confidence_interval
(0.49505217489045894, 0.55694782510954111)
```

Make into a function:
```py
>>> import numpy as np
>>> import scipy.stats
>>> def find_confidence_interval(x, n, confidence_interval_size):
...     p_hat = x/n
...     standard_error = np.sqrt(p_hat * (1-p_hat) / n)
...     alpha = 1 - confidence_interval_size
...     z_critical = scipy.stats.norm.ppf(1 - alpha/2)
...     confidence_interval = p_hat - z_critical*standard_error, p_hat + z_critical*standard_error
...     return confidence_interval
... 
>>> clicking_visitors = 526
>>> all_visitors = 1000
>>> find_confidence_interval(x=clicking_visitors, n=all_visitors, confidence_interval_size=0.95)
(0.49505217489045894, 0.55694782510954111)
```

###### R
```r
> clicking_visitors <- 526
> all_visitors <- 1000
> confidence_interval_size <- 0.95
> x = clicking_visitors
> n = all_visitors
> p_hat = x/n
> p_hat
[1] 0.526
> standard_error = sqrt(p_hat * (1-p_hat) / n)
> alpha = 1 - confidence_interval_size
> alpha
[1] 0.05
> 1 - alpha/2
[1] 0.975
> z_critical = qnorm(1 - alpha/2)
> z_critical
[1] 1.959964
> confidence_interval <- c(p_hat - z_critical*standard_error, p_hat + z_critical*standard_error)
> confidence_interval
[1] 0.4950522 0.5569478
```

Make into a function:
```r
> find_confidence_interval <- function(x, n, confidence_interval_size) {
+     p_hat = x/n
+     standard_error = sqrt(p_hat * (1-p_hat) / n)
+     alpha = 1 - confidence_interval_size
+     z_critical = qnorm(1 - alpha/2)
+     confidence_interval <- c(p_hat - z_critical*standard_error, p_hat + z_critical*standard_error)
+     return(confidence_interval)
+     
+ }
> clicking_visitors <- 526
> all_visitors <- 1000
> find_confidence_interval(x=clicking_visitors, n=all_visitors, confidence_interval_size=0.95)
[1] 0.4950522 0.5569478
```

##### Hypothesis test 
Question: There was a hypothesis of the click rate being 50%. What do the data say about it?

###### z-test
**Python**
```py
>>> clicking_visitors = 526
>>> all_visitors = 1000
>>> x = clicking_visitors
>>> n = all_visitors
>>> p_hypo = 0.5
>>> p_hat = x/n
>>> one_side = False
>>> prop_var = p_hat
>>> standard_error = np.sqrt(prop_var*(1-prop_var)/n)
>>> z = (p_hat-p_hypo)/standard_error
>>> p_value = 1 - scipy.stats.norm.cdf(abs(z))
>>> if one_side == False:
...     p_value *= 2
... 
>>> z, p_value
(1.6466121098225726, 0.099637799747829492)
```
Make into a function:
```py
>>> def single_proportion_ztest(x, n, p_hypo=0.5, prop_var=None, one_side=False):
...     p_hat = x/n
...     if not prop_var:
...         prop_var = p_hat
...     standard_error = np.sqrt(prop_var*(1-prop_var)/n)
...     z = (p_hat-p_hypo)/standard_error
...     p_value = 1 - scipy.stats.norm.cdf(abs(z))
...     if one_side == False:
...         p_value *= 2
...     return z, p_value  
... 
>>> x = clicking_visitors
>>> n = all_visitors
>>> single_proportion_ztest(x, n, p_hypo=p_hypo, prop_var=None, one_side=False)
(1.6466121098225726, 0.099637799747829492)
```
Equivalently, you can use the function from the statsmodels package.
```py
>>> import statsmodels.stats.proportion
>>> statsmodels.stats.proportion.proportions_ztest(clicking_visitors, all_visitors, value=p_hypo)
(1.6466121098225726, 0.099637799747829478)
```
The above uses `p_hat` to . Alternatively we could use `p_hypo`.
```py
>>> p_hypo = 0.5
>>> single_proportion_ztest(x, n, p_hypo=p_hypo, prop_var=p_hypo, one_side=False)
(1.6443843832875589, 0.10009682885123183)
```
Equivalently using the statsmodels package.
```py
>>> import statsmodels.stats.proportion
>>> statsmodels.stats.proportion.proportions_ztest(clicking_visitors, all_visitors, value=p_hypo, prop_var=p_hypo)
(1.6443843832875589, 0.10009682885123182)
```

**R**
```r
```

Make into a function:
```r
```

###### prop-test
In R
```R
> clicking_visitors <- c(526)
> all_visitors <- c(1000)
> prop.test(clicking_visitors, all_visitors)

	1-sample proportions test with continuity
	correction

data:  clicking_visitors out of all_visitors, null probability 0.5
X-squared = 2.601, df = 1, p-value = 0.1068
alternative hypothesis: true p is not equal to 0.5
95 percent confidence interval:
 0.4945121 0.5572857
sample estimates:
    p 
0.526 
```

#### AB test
Given:
- 435 out of 1025 clicked in A; 
- 438 out of 998 clicked in B;

how confidently do you when you say that click rates are about the same?

#####
```Python
>>> import statsmodels.stats.proportion
>>> statsmodels.stats.proportion.proportions_ztest([435, 438], [1025, 998])
(-0.65775309403384319, 0.51069679938649315)
```

##### 
```R
> clicking_visitors <- c(435, 418)
> all_visitors <- c(1025, 998)
> prop.test(clicking_visitors, all_visitors)

	2-sample test for equality of proportions
	with continuity correction

data:  clicking_visitors out of all_visitors
X-squared = 0.043188, df = 1, p-value =
0.8354
alternative hypothesis: two.sided
95 percent confidence interval:
 -0.03847633  0.04958147
sample estimates:
   prop 1    prop 2 
0.4243902 0.4188377 
```



#### ABC test
- 435 out of 1025 clicked in A; 
- 418 out of 998 clicked in B;  
- 412 out of 990 clicked in C;

How confidently do you say that click rates are about the same?

```R
> clicking_visitors <- c(435, 418, 412)
> all_visitors <- c(1025, 998, 990)
> prop.test(clicking_visitors, all_visitors)

	3-sample test for equality of proportions without continuity
	correction

data:  clicking_visitors out of all_visitors
X-squared = 0.14624, df = 2, p-value = 0.9295
alternative hypothesis: two.sided
sample estimates:
   prop 1    prop 2    prop 3 
0.4243902 0.4188377 0.4161616 
```
### Multiple proportions

#### A test
A: 243 from USA; 98 from UK; 65 from DE.

I don't know what question I may have yet.

#### AB test
Given:
- A: 243 from USA; 98 from UK; 65 from DE;
- B: 235 from USA; 97 from UK; 59 from DE;

is the test done properly in terms of testing in similar environments?

#### ABC test
Given:
- A: 243 from USA; 98 from UK; 65 from DE;
- B: 235 from USA; 97 from UK; 59 from DE;
- C: 229 from USA; 90 from UK; 67 from DE;

is the test done properly in terms of testing in similar environments?


## Tests of means

#### A test
Given money spent from 1000 customers, is the averge money spent $50?

#### AB test
Given:
- money spent from 1000 customers in A;
- money spent from 990 customers in B;

is the averge money spent about the same for A and B?

#### ABC test
Given:
- money spent from 1000 customers in A;
- money spent from 990 customers in B;
- money spent from 1012 customers in C;

is the averge money spent about the same for A, B, and C?


Codes:
- [R](https://github.com/yang-zhang/ds-math/blob/master/stat_python_r_r.r)
- [Python](https://github.com/yang-zhang/ds-math/blob/master/stat_python_r.py)

References:
- http://www.springer.com/us/book/9780387790534
- https://www.r-bloggers.com/one-proportion-z-test-in-r/
- http://knowledgetack.com/python/statsmodels/proportions_ztest/
- https://github.com/yang-zhang/ds-math/blob/master/correlating_data_python_r.ipynb
- 

---
[View Source](https://github.com/yang-zhang/yang-zhang.github.io/stat_python_r.md)
[GitHub](https://github.com/yang-zhang)
