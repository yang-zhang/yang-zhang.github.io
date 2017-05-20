# Statistical Tests Cheatsheet with Python and R

This is a cheatsheet for statistical tests that I need to do and how to do them in Python and in R. 
It is organized by the problems to solve, each with an example of the problem, the Python solution, and the R solution.

A, B, C represent three different versions of a eCommerce website.

## Tests of proportions
There are problems that concern single proportion and multiple proportions.
- An example of single proportions: the percentage of visitors to your website that clicked "Buy Now" (e.g., a 3% click rate).
- An example of multiple proportions: the percentages of visitors to your website from different countries (e.g., 60% US, 30% UK, 10% DE).

### Single proportions

#### A test 
Given 526 out of 1000 people clicked in A, how confidently do you say that the click rate is 52.6%? 

##### ztest

```Python
>>> import statsmodels.stats.proportion
>>> statsmodels.stats.proportion.proportions_ztest(526, 1000, value=0.5)
(1.6466121098225726, 0.099637799747829478)
```

##### chisquare
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


## Tests of mean

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
- [Python](https://github.com/yang-zhang/ds-math/blob/master/stat_python_r.ipynb)

References:
- http://www.springer.com/us/book/9780387790534
- https://www.r-bloggers.com/one-proportion-z-test-in-r/
- http://knowledgetack.com/python/statsmodels/proportions_ztest/
- https://github.com/yang-zhang/ds-math/blob/master/correlating_data_python_r.ipynb
- 

