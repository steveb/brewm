#!/usr/bin/python
#
#    THIS FILE IS PART OF THE BREWM PROJECT AND LICENSED UNDER THE GPL. SEE
#    THE 'COPYING' FILE FOR DETAILS
#
#    Brewm's main class. It creates the majority of the main window GUI
#    and gets everything up and running.
#
#-------------------------------------------------------------------------------

import math

def abv_to_abw(abv):
    """Approximately converts from alcohol by volume to alcohol by weight.
    
    >>> '%.2f' % abv_to_abw(5)
    '4.00'
    >>> '%.2f' % abv_to_abw(4)
    '3.20'
    >>> '%.2f' % abv_to_abw(10)
    '8.00'
    >>> '%.2f' % abv_to_abw(0)
    '0.00'
    """
    return abv / 1.25
def abw_to_abv(abw):
    """Approximately converts from alcohol by weight to alcohol by volume.
    
    >>> '%.2f' % abw_to_abv(4.00)
    '5.00'
    >>> '%.2f' % abw_to_abv(3.20)
    '4.00'
    >>> '%.2f' % abw_to_abv(8.00)
    '10.00'
    >>> '%.2f' % abw_to_abv(0)
    '0.00'
    """
    return abw * 1.25

def gravity_to_plato(g):
    """Converts specific gravity to extract in degrees plato.
    
    >>> '%.1f' % gravity_to_plato(1.040)
    '10.0'
    >>> '%.1f' % gravity_to_plato(1.028)
    '7.1'
    >>> '%.1f' % gravity_to_plato(1.061)
    '15.0'
    >>> '%.1f' % gravity_to_plato(1.004)
    '1.0'
    """
    return 668.72 * g - 463.37 - 205.347 * g * g

def plato_to_gravity(e):
    """Converts from extract in degrees plato to specific gravity.
    
    >>> '%.3f' % plato_to_gravity(10.0)
    '1.040'
    >>> '%.3f' % plato_to_gravity(7.1)
    '1.028'
    >>> '%.3f' % plato_to_gravity(15.0)
    '1.061'
    >>> '%.3f' % plato_to_gravity(1.0)
    '1.004'
    """
    return 1.000082636 + e * (3.8480 + e * 0.014563)/ 1000.0 ;

def gravity_to_abv(og, fg):
    """Estimates the alcohol by volume from the original and apparent final gravity
    
    >>> '%.2f' % gravity_to_abv(1.050, 1.010)
    '5.20'
    >>> '%.2f' % gravity_to_abv(1.042, 1.012)
    '3.88'
    >>> '%.2f' % gravity_to_abv(1.100, 1.024)
    '9.98'
    """
    return abw_to_abv(gravity_to_abw(og, fg))

def gravity_to_abw(og, fg):
    """Estimates the alcohol by weight from the original and apparent final gravity
    
    >>> '%.2f' % gravity_to_abw(1.050, 1.010)
    '4.16'
    >>> '%.2f' % gravity_to_abw(1.042, 1.012)
    '3.10'
    >>> '%.2f' % gravity_to_abw(1.100, 1.024)
    '7.99'
    """
    return plato_to_abw(og, fg)

def plato_to_abw(ogp, fgp):
    """Estimates the alcohol by weight from the original and apparent final gravity
    
    >>> '%.2f' % plato_to_abw(12.4, 2.6)
    '4.15'
    >>> '%.2f' % plato_to_abw(10.5, 3.1)
    '3.10'
    >>> '%.2f' % plato_to_abw(23.7, 6.1)
    '7.95'
    """
    c = 0.8192
    d = 2.0665
    e = 0.010665
    rep = fgp*c+ogp*(1-c)
    return (ogp-rep)/(d-e*ogp)

def og_fg_atten(og, fg):
    """Calculates apparent attenuation from original and final gravity
    
    >>> '%.2f' % og_fg_atten(1.050, 1.010)
    '0.80'
    >>> '%.2f' % og_fg_atten(1.055, 1.008)
    '0.85'
    >>> '%.2f' % og_fg_atten(1.050, 1.010)
    '0.80'
    """
    return (og - fg) / (og - 1)

def og_atten_to_fg(og, atten):
    """Calculates apparent attenuation from original and final gravity
    
    >>> '%.3f' % og_atten_to_fg(1.050, 0.80)
    '1.010'
    >>> '%.3f' % og_atten_to_fg(1.055, 0.85)
    '1.008'
    >>> '%.3f' % og_atten_to_fg(1.050, 0.80)
    '1.010'
    """
    return - (atten * (og - 1) - og)
def gravity_bitterness_to_bugu(og, fg, bitterness):
    pass
def gravity_bugu_to_bitterness(og, fg, bugu):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
