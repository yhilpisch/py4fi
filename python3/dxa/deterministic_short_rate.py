'''
==== Deterministic Short Rate

Interest rates in general and short rates in particular are not constant over time. You rather observe something called a term structur of insterest rates in financial markets. Simply speaking, this means that a ZCB maturing at latexmath:[$s \geq 0$] will have a different yield than another bond of the same type maturing at latexmath:[$t \geq s$]. _Yield_ in this case is defined as the quantity latexmath:[$y_t$] that solves the equation latexmath:[$D_0(t)=e^{-y_t t}$] for a ZCB maturing at latexmath:[$t$]. Analogously, yield is also the quantity latexmath:[$y_s$] that solves the equation latexmath:[$D_0(s)=e^{-y_s s}$] for a ZCB maturing at latexmath:[$s$].'''

from constant_short_rate import *
class deterministic_short_rate(object):
    ''' Class for discounting based on deterministic short rates,
    derived from a term structure of unit Zero-Coupon Bond yields
    
    Attributes
    ==========
    name : string
        name of the object
    yield_list : list/array of (time, yield) tuples
        input yields with time attached
    
    Methods
    =======
    get_interpolated_yields : 
        return interpolated yield curve given a time list/array
    get_forward_rates :
        return forward rates given a time list/array
    get_discount_factors :
        return discount factors given a time list/array
    '''
    def __init__(self, name, yield_list):
        self.name = name
        self.yield_list = np.array(yield_list)
        if np.sum(np.where(self.yield_list[:, 1] < 0, 1, 0)) > 0:
            raise ValueError, 'Negative yield(s).'
    def get_interpolated_yields(self, time_list, dtobjects=True):
        ''' time_list either list of datetime objects or list of
        year deltas as decimal number (dtobjects=False)
        '''
        if dtobjects is True:
            tlist = get_year_deltas(time_list)
        else:
            tlist = time_list
        dlist = get_year_deltas(self.yield_list[:, 0])
        if len(time_list) <= 3:
            k = 1
        else:
            k = 3
        yield_spline = sci.splrep(dlist, self.yield_list[:, 1], k=k)
        yield_curve = sci.splev(tlist, yield_spline, der=0)
        yield_deriv = sci.splev(tlist, yield_spline, der=1)
        return np.array([time_list, yield_curve, yield_deriv]).T
    def get_forward_rates(self, time_list, dtobjects=True):
        yield_curve = self.get_interpolated_yields(time_list, dtobjects)
        if dtobjects is True:
            tlist = get_year_deltas(time_list)
        else:
            tlist = time_list
        forward_rate = yield_curve[:, 1] + yield_curve[:, 2] * tlist
        return np.array((time_list, forward_rate)).T
    def get_discount_factors(self, time_list, dtobjects=True):
        discount_factors = []
        if dtobjects is True:
            dlist = get_year_deltas(time_list)
        else:
            dlist = time_list
        forward_rate = self.get_forward_rates(time_list, dtobjects)
        for no in range(len(dlist)):
            factor = 0.0
            for d in range(no, len(dlist) - 1):
                factor += ((dlist[d + 1] - dlist[d])
                        * (0.5 * (forward_rate[d + 1, 1] + forward_rate[d, 1])))
            discount_factors.append(np.exp(-factor))
        return np.array((time_list, discount_factors)).T