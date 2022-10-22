#!/usr/bin/env python
# coding: utf-8

#                     **Statistics Worksheet-1**

# **Q1 to Q9 have only one correct answer.Choose the correct option to answer your question.**

# 1. Bernoulli random variable take (only) the value 1 and 0
# 
# Ans: **a.** True

# 2.Which of the following theoram states that the distribution of averages of iid variables, properly normalized,becomes that of a standard normal as the sample size increases?
# 
# Ans: **a.** Central Limit Theoram

# 3.Which of the following is incorrect with respect to use of poisson distribution?
# 
# Ans: **b.** Modeling bounded count data

# 4.Point out the correct statement.
# 
# Ans: **d.** All the above mentioned

# 5.  _____________ random variables are used to model rates.
# 
# Ans: **c.** Poission

# 6. Usually  replacing the standard errors by its estimated value does change thr CLT.
# 
# Ans: **b.** False

# 7.Which of the following testing is concerned with making descision using data
# 
# Ans: **b.** Hypothesis

# 8.Normalized data are centered at________ and have units equal to standard deviation of the original data.
# 
# Ans: **a.** 0

# 9. Which of the following statement is incorrect with respect to outliers?
# 
# Ans: **c.** Outliers cannot conforms to the regression relationship

# **Q10 and Q15 are subjective answer type Question , Anwer them in your own word briefly.**

# 10. What do you understand by the term Normal Distribution?
# 
# Ans: Normal distribution also known as guassian distrbution is the most important probablity distribution in Statistics for independent  random variable,the normal distriution describes how the values of variables are distributed.
# 
# eg: Height Data, Age Data, Sand Collection Data,etc

# 11. How doyou handle missing data? What imputation techniques do you recommend?
# 
# 
# Ans: Data that is not stored or present for some variable in the dataset  are Missing data,Missing data can bias the result of ML models or can reduce the accuracy of models ,There are Two ways to handle the missing data  which are :
# 
#                    1. Deleting the Missing Data.
#                    
#                    2. Imputing the Missing Data.
#                    
#  The KNNImputer by scikit -learn is a widely used method to impute missing values,It is widely being observed as a replacement fot traditional imputation techniques. K- Nearest Neighbors work in a way that it identify the neighboring points  through a measure of distance and the missing values can be estimated using completed value of neighboring observation.  

# 12.What is A/B testing?
# 
# Ans: A/B  testing also known as bucket testing  or split run testing  is a user experienced research methodology, A/B teststing is a way to compare two version of a single variable , typically by testing  a subject response to variant A against variant B , and determining  which of the two variant is more effective.
# A/B test are useful for understanding user engagements and stisfaction of online features like a new feature or products.A/B  testing make user experinces  more sucessful.

# 13.Is mean Imputation of missing data acceptable practice?
# 
# Ans: The process of replacing null values in a data collection with the data’s mean is known as mean imputation.
# 
# Mean imputation is typically considered terrible practice since it ignores feature correlation. Consider the following scenario: we have a table with age and fitness scores, and an eight-year-old has a missing fitness score. If we average the fitness scores of people between the ages of 15 and 80, the eighty-year-old will appear to have a significantly greater fitness level than he actually does.
# 
# Second, mean imputation decreases the variance of our data while increasing bias. As a result of the reduced variance, the model is less accurate and the confidence interval is narrower.

# 14.What is linear regression in statistics?
# 
# Ans: Linear regression is statistical way of measuring the relationship between variabes such as if we take time and cost example : if the time increases so does the cost increases,It is used for future prediction also. The simplest form of the regression equation with one dependent and one independent variable is defined by the formula y = c + b*x, where y = estimated dependent variable score, c = constant, b = regression coefficient, and x = score on the independent variable.Three major uses for regression analysis are (1) determining the strength of predictors, (2) forecasting an effect, and (3) trend forecasting.
# 
# 

# 15. What are the various branches of statistics?
# Ans: The two main branches of statistics are:
# 
# Descriptive Statistics
# Inferential Statistics
# Descriptive Statistics – Through graphs or tables, or numerical calculations, descriptive statistics uses the data to provide descriptions of the population.
# 
# Inferential Statistics – Based on the data sample taken from the population, inferential statistics makes the predictions and inferences.

# In[ ]:




