#
# DX Library Frame
# market_environment.py
#

class market_environment(object):
    ''' Class to model a market environment relevant for valuation.
    
    Attributes
    ==========
    name: string
        name of the market environment
    pricing_date : datetime object
        date of the market environment
    
    Methods
    =======
    add_constant :
        adds a constant (e.g. model parameter)
    get_constant :
        gets a constant
    add_list :
        adds a list (e.g. underlyings)
    get_list :
        gets a list
    add_curve :
        adds a market curve (e.g. yield curve)
    get_curve :
        gets a market curve
    add_environment :
        adds and overwrites whole market environments
        with constants, lists, and curves
    '''

    def __init__(self, name, pricing_date):
        self.name = name
        self.pricing_date = pricing_date
        self.constants = {}
        self.lists = {}
        self.curves = {}

    def add_constant(self, key, constant):
        self.constants[key] = constant

    def get_constant(self, key):
        return self.constants[key]

    def add_list(self, key, list_object):
        self.lists[key] = list_object

    def get_list(self, key):
        return self.lists[key]

    def add_curve(self, key, curve):
        self.curves[key] = curve

    def get_curve(self, key):
        return self.curves[key]

    def add_environment(self, env):
        # overwrites existing values, if they exist
        for key in env.constants:
            self.constants[key] = env.constants[key]
        for key in env.lists:
            self.lists[key] = env.lists[key]
        for key in env.curves:
            self.curves[key] = env.curves[key]
        