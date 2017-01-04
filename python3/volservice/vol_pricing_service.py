#
# Valuation of European volatility options
# in Gruenbichler-Longstaff (1996) model
# square-root diffusion framework
# -- parameter dictionary & web service function
#
from vol_pricing_formula import calculate_option_value

# model parameters

# http://127.0.0.1:4000/?V0=0.2&kappa=2.0&theta=0.21&sigma=0.02&zeta=0.0&T=1.0&r=0.05&K=0.19

PARAMS = {
    'V0': 'current volatility level',
    'kappa': 'mean reversion factor',
    'theta': 'long-run mean of volatility',
    'sigma': 'volatility of volatility',
    'zeta': 'factor of the expected volatility risk premium',
    'T': 'time horizon in years',
    'r': 'risk-free interest rate',
    'K': 'strike'
}

# function for web service


def get_option_value(data):
    ''' A helper function for web service. '''
    errorline = 'Missing parameter %s (%s)\n'
    errormsg = ''
    for para in PARAMS:
        if para not in data.keys():
            # check if all parameters are provided
            errormsg += errorline % (para, PARAMS[para])
    if errormsg != '':
        return errormsg
    else:
        result = calculate_option_value(
            float(data['V0']),
            float(data['kappa']),
            float(data['theta']),
            float(data['sigma']),
            float(data['zeta']),
            float(data['T']),
            float(data['r']),
            float(data['K'])
        )
        return str(result)
