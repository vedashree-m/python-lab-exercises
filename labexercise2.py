# -*- coding: utf-8 -*-
"""labexercise2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aNdoxNDzobgd5j-CqaBOXZg1C8OCdg7z
"""

#you have two datasets representing the test scores of students before and after AI-based tutoring. Perform a paired T-test to determine if the Ai-based tutoring significantly improved students scores
from scipy.stats import ttest_rel

# Example datasets
before_scores = [75, 80, 72, 90, 85]
after_scores = [82, 85, 78, 92, 88]

# Perform paired T-test
t_statistic, p_value = ttest_rel(after_scores, before_scores)


print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


alpha = 0.05
if p_value < alpha:
    print("The AI-based tutoring significantly improved students' scores.")
else:
    print("There is no significant improvement in students' scores due to AI-based tutoring.")

#you want to check if there's an association between the choice of programming language(Python, Java, C++) ad students job placement status(placed , not placed). perform a chi-square test for independence.
from scipy.stats import chi2_contingency

# Rows represent programming languages
# Columns represent job placement status (Placed, Not Placed)
contingency_table = [
    [50, 30],  # Python: [Placed, Not Placed]
    [40, 35],  # Java: [Placed, Not Placed]
    [20, 25]   # C++: [Placed, Not Placed]
]

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)


print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
for row in expected:
    print(row)


alpha = 0.05
if p < alpha:
    print("There is a significant association between programming language choice and job placement status.")
else:
    print("There is no significant association between programming language choice and job placement status.")

#you want to compare the effectiveness of three different AI models(A,B,C) on predicting house prices. The prediction errors for each model are given. perform a one-way ANOVA test to check if there is a significant difference between the models.

from scipy.stats import f_oneway

# Example data
model_a_errors = [10, 12, 11, 13, 14]
model_b_errors = [8, 9, 7, 10, 6]
model_c_errors = [15, 14, 16, 14, 17]

# Perform one-way ANOVA test
f_statistic, p_value = f_oneway(model_a_errors, model_b_errors, model_c_errors)


print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("There is a significant difference in prediction errors between the AI models.")
else:
    print("There is no significant difference in prediction errors between the AI models.")

#you want to determine there is a correlation between students practice hours and their scores in a machine learning exam. Calculate the person correlation coefficient to measure the linear relationship between the two variables.
from scipy.stats import pearsonr

# Example data
practice_hours = [2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 70, 75, 80]

# Calculate Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(practice_hours, exam_scores)


print(f"Pearson correlation coefficient: {correlation_coefficient}")
print(f"P-value: {p_value}")


alpha = 0.05
if p_value < alpha:
    print("There is a significant linear relationship between practice hours and exam scores.")
else:
    print("There is no significant linear relationship between practice hours and exam scores.")

#in a company ,60% of employees are proficient in python . out of a sample of 100 employees , 70 are found to be proficient in python. perform a Z-test to check if the proportion of python-proficient employees is significantly different from the comapny's standard(60%)
from statsmodels.stats.proportion import proportions_ztest

# Sample data
sample_size = 100
sample_proficient = 70
company_proportion = 0.6

# Perform Z-test
stat, p_value = proportions_ztest(count=sample_proficient, nobs=sample_size, value=company_proportion)


print(f"Z-statistic: {stat}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("The proportion of Python-proficient employees is significantly different from the company's standard.")
else:
    print("The proportion of Python-proficient employees is not significantly different from the company's standard.")