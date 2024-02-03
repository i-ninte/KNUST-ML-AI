 scipy.stats as stats
observations = [650, 570, 420, 480, 510, 380, 490]
expectations = [5import00, 500, 500, 500, 500, 500, 500]
result = stats.chisquare(f_obs=observations, f_exp=expectations)
result


# to  calculate x2 static and p values for hypothesis testing
import numpy as np
import scipy.stats as stats
observations = np.array([[850, 450],[1300, 900]])
result = stats.contingency.chi2_contingency(observations)
result
