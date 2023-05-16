---
title: Sieve of Eratosthenes
autor: Ryan Jensen
number-depth: 1
order: 110
format:
  html:
    code-fold: true
    default-image-extension: svg
  pdf:
    default-image-extension: pdf
---


#### Problem
A natural number greater than one is prime if it cannot be written as the product
of two smaller natural numbers. In this problem, you will find the first few
prime numbers using the Sieve of Eratosthenes. Find out how many prime numbers
are less than 120.

Write out then numbers 1-120 in order in the grid below. Cross out two. Circle 
two, this is the first prime. Now cross out (or color out) all multiples of two 
except two itself. The next number not crossed out is three. Circle it since it
is the next prime. Now cross out all multiples of three except three itself. 
Repeat this process: find the then next number which is not crossed out; this 
is the next prime; circle it and then cross out all multiples of it except 
itself. Keep going until you can't cross out any more. Count the primes (circled
numbers).

::: {.cell execution_count=1}

::: {.cell-output .cell-output-stdout}
```
Render PDF requires pylatex installation.
```
:::
:::


![Sieve of Eratosthenes](image/sieve){width=50%}

