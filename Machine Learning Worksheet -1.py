#!/usr/bin/env python
# coding: utf-8

#                           MACHINE LEARNING

# **In Q1 to Q11, only one option is correct, choose the correct option:**

# 1. Which of the following methods do we use to find the best fit line for data in Linear Regression?
# 
# Ans: **A.** Least Square Error

# 2. Which of the following statement is true about outliers in linear regression? 
# 
# Ans: **A.** Linear regression is sensitive to outliers

# 3. A line falls from left to right if a slope is ______?
# 
# Ans: **B.** Negative

# 4. Which of the following will have symmetric relation between dependent variable and independent variable?
# 
# Ans: **B.** Correlation
# 

# 5. Which of the following is the reason for over fitting condition? 
# 
# Ans: **C.** Low bias and high variance

# 6. If output involves label then that model is called as: 
#     
# Ans: **B.** Predictive Model

# 7. Lasso and ridge regression techniques belongs to _________?
# 
# Ans: **D.**  Regularization

# 8. To overcome with imbalance dataset which technique can be used? 
# 
# Ans: **A.** Cross Validation

# 9. The AUC Receiver Operator Characteristic (AUCROC) curve is an evaluation metric for binary 
#  classification problems. It uses _____ to make graph?
#  
#  Ans: **A.** TPR and FPR

# 10. In AUC Receiver Operator Characteristic (AUCROC) curve for the better model area under the 
# curve should be less
# 
# Ans:  **B.** False

# 11.Pick the feature extraction from below:
# 
# Ans: **B.** Apply PCA to project high dimensional data.

# **In Q12, more than one options are correct, choose all the correct options:** 

# 12. Which of the following is true about Normal Equation used to compute the coefficient of the Linear 
# Regression? 
# 
# Ans: **A.** We don't have to choose the learning rate.
#      **B.** It become slow when number of features is very large.
#      **D.** It does not make use of dependent variable.
#      

# 13. Explain the term Regularization?
# 
# Ans: when we use regression models to train some data,there is a good chance that the model will overfit the given training data set. Regularization helps sort this overfitting problem by restricting the degree of freedom of a given equation i.e simply reducing the number of degrees of a polynomial function by reducing their corresponding weights.
# 
# In a linear equation ,we do not want huge weight/coefficientts as a small change in weight can make a large diffrence for the dependent variable(Y).So, regularization contraints the weights of such features to avoid overfitting.
# 
# to regularize the model, a Shrinkage penalty is added to the function.

# 14.Which Particular algorithms are used for regularization?
# 
# Ans:We use  Lasso regularization to overcome the problem that ridge has, Lasso(Least Absolute Shrinkage and Selection Operator) is an alternative that can pick relevant features that will be useful for modelling. Lasso also has the shrinkage parametre but the difference that has with Ridge is that there is no squared term of the estimated coefficient but only an absolute value.To overcome the problem that ridge has, Lasso(Least Absolute Shrinkage and Selection Operator) is an alternative that can pick relevant features that will be useful for modelling. Lasso also has the shrinkage parametre but the difference that has with Ridge is that there is no squared term of the estimated coefficient but only an absolute value. the term after RSS is called the shrinkage penalty or L1 norm.

# 15.Explaim the term error present in linear regreasion equation?
# 
# Ans:An error term is a residual variable produced by a statistical or mathematical model, which is created when the model does not fully represent the actual relationship between the independent variables and the dependent variables. As a result of this incomplete relationship, the error term is the amount at which the equation may differ during empirical analysis.
# 
# The error term is also known as the residual, disturbance, or remainder term, and is variously represented in models by the letters e, ε, or u.
# 
# 
#   
# Y=αX+βρ+ϵ
# where:
# α,β=Constant parameters
# X,ρ=Independent variables
# ϵ=Error term
# 
# 

# In[ ]:




