#
# Valuation of European volatility options
# in Gruenbichler-Longstaff (1996) model
# square-root diffusion framework
# -- parameter dictionary & web service function
#
from vol_pricing_formula import calculate_option_value

# model parameters

PARAMS={
    'V0' : 'current volatility level',
    'kappa' : 'mean reversion factor',
    'theta' : 'long-run mean of volatility',
    'sigma' : 'volatility of volatility',
    'zeta' : 'factor of the expected volatility risk premium',
    'T' : 'time horizon in years',
    'r' : 'risk-free interest rate',
    'K' : 'strike'
    }

# function for web service

def get_option_value(data):
    ''' A helper function for web service. '''
    errorline = 'Missing parameter %s (%s)\n'
    errormsg = ''
    for para in PARAMS:
        if not data.has_key(para):
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