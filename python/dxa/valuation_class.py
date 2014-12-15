#
# DX Library Valuation
# valuation_class.py
#

class valuation_class(object):
    ''' Basic class for single-factor valuation.
    
    Attributes
    ==========
    name : string
    	name of the object
    underlying :
    	instance of simulation class
    mar_env : instance of market_environment
        market environment data for valuation
    payoff_func : string
        derivatives payoff in Python syntax
        Example: 'np.maximum(maturity_value - 100, 0)' 
        where maturity_value is the NumPy vector with
        respective values of the underlying
        Example: 'np.maximum(instrument_values - 100, 0)' 
        where instrument_values is the NumPy matrix with
        values of the underlying over the whole time/path grid
        
    Methods
    =======
    update:
    	updates selected valuation parameters
    delta :
        returns the Delta of the derivative
    vega :
        returns the Vega of the derivative
    '''

    def __init__(self, name, underlying, mar_env, payoff_func=''):
        try:
            self.name = name
            self.pricing_date = mar_env.pricing_date
            try:
                self.strike = mar_env.get_constant('strike')
                  # strike is optional
            except:
                pass
            self.maturity = mar_env.get_constant('maturity')
            self.currency = mar_env.get_constant('currency')
            # simulation parameters and discount curve from simulation object
            self.frequency = underlying.frequency
            self.paths = underlying.paths
            self.discount_curve = underlying.discount_curve
            self.payoff_func = payoff_func
            self.underlying = underlying
            # provide pricing_date and maturity to underlying
            self.underlying.special_dates.extend([self.pricing_date,
                                                  self.maturity])
        except:
            print "Error parsing market environment."

    def update(self, initial_value=None, volatility=None,
               strike=None, maturity=None):
        if initial_value is not None:
            self.underlying.update(initial_value=initial_value)
        if volatility is not None:
            self.underlying.update(volatility=volatility)
        if strike is not None:
            self.strike = strike
        if maturity is not None:
            self.maturity = maturity
            # add new maturity date if not in time_grid
            if not maturity in self.underlying.time_grid:
                self.underlying.special_dates.append(maturity)
                self.underlying.instrument_values = None

    def delta(self, interval=None, accuracy=4):
        if interval is None:
            interval = self.underlying.initial_value / 50.
        # forward-difference approximation
        # calculate left value for numerical Delta
        value_left = self.present_value(fixed_seed=True)
        # numerical underlying value for right value
        initial_del = self.underlying.initial_value + interval
        self.underlying.update(initial_value=initial_del)
        # calculate right value for numerical delta
        value_right = self.present_value(fixed_seed=True)
        # reset the initial_value of the simulation object
        self.underlying.update(initial_value=initial_del - interval)
        delta = (value_right - value_left) / interval
        # correct for potential numerical errors
        if delta < -1.0:
            return -1.0
        elif delta > 1.0:
            return 1.0
        else:
            return round(delta, accuracy)

    def vega(self, interval=0.01, accuracy=4):
        if interval < self.underlying.volatility / 50.:
            interval = self.underlying.volatility / 50.
        # forward-difference approximation
        # calculate the left value for numerical Vega
        value_left = self.present_value(fixed_seed=True)
        # numerical volatility value for right value
        vola_del = self.underlying.volatility + interval
        # update the simulation object
        self.underlying.update(volatility=vola_del)
        # calculate the right value for numerical Vega
        value_right = self.present_value(fixed_seed=True)
        # reset volatility value of simulation object
        self.underlying.update(volatility=vola_del - interval)
        vega = (value_right - value_left) / interval
        return round(vega, accuracy)