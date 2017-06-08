# pylint: disable=I0011,C0103,R0903
"""
Module name: temperatureunits

Calculate and return a value of one temperature unit converted from another
temperature unit.

Example:
    TemperatureUnit(32, 'F', 'C').doconvert()
    returns: 32.0 F is 0.0 C

Exportables:
    Classes:
        TemperatureUnit
            Functions:
                doconvert: Return calculated conversion between two units
"""


class TemperatureUnit(object):
    """placeholder docstring"""
    def __init__(self, amt, ufrom, uto):
        self.amt = amt
        self.ufrom = ufrom
        self.uto = uto

    def _getuval(self, argument):
        """Return a function to calculate the unit's value"""
        function = '_unit_{0}'.format(str(argument))
        function = getattr(self, function, lambda: None)
        return function()

    def doconvert(self):
        """Return calculated conversion between two units"""
        conv = self._getuval(self.ufrom)[0][self.uto]
        return "{0} {1} is {2} {3}".format(self.amt, self.ufrom, conv, self.uto)

    def _unit_F(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from F to F, C, and K"""
        calc = {
            'C': (self.amt - 32.0) * 5 / 9,
            'K': (self.amt + 459.67) * 5 / 9,
            'F': self.amt
        },
        return calc

    def _unit_C(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from C to F, C, and K"""
        calc = {
            'F': (self.amt * 9) / 5 + 32.0,
            'K': self.amt + 273.15,
            'C': self.amt
        },
        return calc

    def _unit_K(self):
        """Return a dictionary containing Fahrenheit (F), Celsius (C), or
        Kelvin (K) keys (F, C, K) and values converted from K to F, C, and K"""
        calc = {
            'F': self.amt * 9 / 5 - 459.67,
            'C': self.amt - 273.15,
            'K': self.amt
        }
        return calc
