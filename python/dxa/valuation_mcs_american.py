#
# DX Library Valuation
# valuation_mcs_american.py
#
import numpy as np

from valuation_class import valuation_class

class valuation_mcs_american(valuation_class):
    ''' Class to value American options with arbitrary payoff
    by single-factor Monte Carlo simulation.
        
    Methods
    =======
    generate_payoff :
        returns payoffs given the paths and the payoff function
    present_value : 
        returns present value (LSM Monte Carlo estimator)
        according to Longstaff-Schwartz (2001)
    '''

    def generate_payoff(self, fixed_seed=False):
        '''
        Parameters
        ==========
        fixed_seed :
            use same/fixed seed for valuation
        '''
        try:
            strike = self.strike
        except:
            pass
        paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed)
        time_grid = self.underlying.time_grid
        try:
            time_index_start = int(np.where(time_grid == self.pricing_date)[0])
            time_index_end = int(np.where(time_grid == self.maturity)[0])
        except:
            print "Maturity date not in time grid of underlying."
        instrument_values = paths[time_index_start:time_index_end + 1]
        try:
            payoff = eval(self.payoff_func)
            return instrument_values, payoff, time_index_start, time_index_end
        except:
            print "Error evaluating payoff function."

    def present_value(self, accuracy=6, fixed_seed=False, bf=5, full=False):
        '''
        Parameters
        ==========
        accuracy : int
            number of decimals in returned result
        fixed_seed : boolean
            use same/fixed seed for valuation
        bf : int
            number of basis functions for regression
        full : Boolean
            return also full 1d array of present values
        '''
        instrument_values, inner_values, time_index_start, time_index_end = \
                    self.generate_payoff(fixed_seed=fixed_seed)
        time_list = self.underlying.time_grid[time_index_start:time_index_end + 1]
        discount_factors = self.discount_curve.get_discount_factors(
                            time_list, dtobjects=True)
        V = inner_values[-1]
        for t in range(len(time_list) - 2, 0, -1):
            # derive relevant discount factor for given time interval
            df = discount_factors[t, 1] / discount_factors[t + 1, 1]
            # regression step
            rg = np.polyfit(instrument_values[t], V * df, bf)
            # calculation of continuation values per path
            C = np.polyval(rg, instrument_values[t])
            # optimal decision step:
            # if condition is satisfied (inner value > regressed cont. value)
            # then take inner value; take actual cont. value otherwise
            V = np.where(inner_values[t] > C, inner_values[t], V * df)
        df = discount_factors[0, 1] / discount_factors[1, 1]
        result = df * np.sum(V) / len(V)
        if full:
            return round(result, accuracy), df * V
        else:
            return round(result, accuracy)