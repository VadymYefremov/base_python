""" Use SOLID principles"""
import numpy as np, pandas as pd
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import scipy.stats as statsimport
import statsmodels.api as sm


class DoNothing:
    """ I don't now what is it"""
    def precission(self, y_d, yhat):
        """ Creates list """
        res = []
        for i in range(yhat):
            res.append((y_d[i] - yhat[i]) ** 2)
        return res


DoN = DoNothing


class LikelihoodFunction:
    """ Define likelihood function
     """
    def mle_regression(self, params):
        """ 'str params' inputs are guesses at our parameters/
     'yhat' predictions  next, we flip the Bayesian question,
     compute PDF of observed values normally distributed around,
     with a standard deviation of sd.
     'negLL - return negative LL """
        intercept, beta, s_d = params[0], params[1], params[2]
        yhat = intercept + beta * GetData.x()
        neg_ll = -np.sum(scipy.stats.norm.logpdf(GetData.y(), loc=yhat, scale=s_d))
        return (neg_ll)


lf = LikelihoodFunction()


class GetData:
    """ Class get data, contains methods for getting data, namely:
    'N','x','noise','y','df'
    """
    @staticmethod
    def N():
        """ N data"""
        return 20

    @staticmethod
    def x():
        """ counts x"""
        return np.linspace(0, 20, GetData.N())

    @staticmethod
    def noise():
        """ counts noise"""
        return np.random.normal(loc=0.0, scale=2.0, size=GetData.N())

    @staticmethod
    def y():
        """ counts y"""
        return 3 * GetData.x() + 1 + GetData.noise()

    @staticmethod
    def df():
        """ counts df"""
        return pd.DataFrame({'y': GetData.y(), 'x': GetData.x(), 'constant': 0})


df = GetData.df()
print(df)


class Plotting:
    """for plotting results data"""
    @staticmethod
    def plt():
        """ Plotting data """
        return plt.scatter(df.x, df.y), plt.show()


pl = Plotting.plt()


class CalculationOfResults:
    """ Class calculation of results  """

    def X(self):
        """ fit model and summarize """
        return df[['constant', 'x']]

    @staticmethod
    def guess():
        """ counts guess """
        return np.array([5, 5, 2])

    def results(self):
        """ counts result"""
        return minimize(lf.mle_regression, CalculationOfResults.guess(),
                        method='Nelder-Mead', options={'disp': True})


cl = CalculationOfResults()
# 1-й метод - МНК (статистическая оценка) - минимизировали сумму
print(sm.OLS(GetData.y(), cl.X()).fit().summary())

results = cl.results()
print(results['x'])
