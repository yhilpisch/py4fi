#
# Valuation of European volatility call options
# in Gruenbichler-Longstaff (1996) model
# square-root diffusion framework
# -- semianalytical formula
#
from scipy.stats import ncx2
import numpy as np

# Semianalytical option pricing formula of GL96


def calculate_option_value(V0, kappa, theta, sigma, zeta, T, r, K):
    ''' Calculation of European call option price in GL96 model.

    Parameters
    ==========
    V0 : float
        current volatility level
    kappa : float
        mean reversion factor
    theta : float
        long-run mean of volatility
    sigma : float
        volatility of volatility
    zeta :
        volatility risk premium
    T : float
        time-to-maturity
    r : float
        risk-free short rate
    K : float
        strike price of the option

    Returns
    =======
    value : float
        net present value of volatility call option
    '''
    D = np.exp(-r * T)  # discount factor
    
    # variables
    alpha = kappa * theta
    beta = kappa + zeta
    gamma = 4 * beta / (sigma ** 2 * (1 - np.exp(-beta * T)))
    nu = 4 * alpha / sigma ** 2
    lamb = gamma * np.exp(-beta * T) * V0
    cx1 = 1 - ncx2.cdf(gamma * K, nu + 4, lamb)
    cx2 = 1 - ncx2.cdf(gamma * K, nu + 2, lamb)
    cx3 = 1 - ncx2.cdf(gamma * K, nu, lamb)
    
    # formula for European call price
    value = (D * np.exp(-beta * T) * V0 * cx1
      + D * (alpha / beta) * (1 - np.exp(-beta * T))
      * cx2 - D * K * cx3)
    return value

