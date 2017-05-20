# Statistical Tests Cheatsheet with Python and R

This is a cheatsheet for statistical tests that I need to do and how to do them in Python and in R. 
It is organized by the problems to solve, each with an example of the problem, the Python solution, and the R solution.

A, B, C represent three different versions of a eCommerce website.

## Tests of proportions
There are problems that concern single proportion and multiple proportions.
- An example of a single proportion: the proportion of visitors to your website that clicked "Buy Now" (e.g., a 3% click rate).
- An example of multiple proportions: the proportions of visitors to your website from different countries (e.g., 60% US, 30% UK, 10% DE).

### Single proportion
#### A test 
Given 526 out of 1000 people clicked in A, how confidently do you say that the click rate is 52.6%? 

#### AB test
Given:
- 435 out of 1025 clicked in A; 
- 438 out of 998 clicked in B;

how confidently do you when you say that click rates are about the same?

#### ABC test
- 435 out of 1025 clicked in A; 
- 418 out of 998 clicked in B;  
- 412 out of 990 clicked in C;

How confidently do you say that click rates are about the same?

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



References:
- to add
- my notebook: todo 
