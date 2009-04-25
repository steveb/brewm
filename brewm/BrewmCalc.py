#!/usr/bin/python
#
#    THIS FILE IS PART OF THE BREWM PROJECT AND LICENSED UNDER THE GPL. SEE
#    THE 'COPYING' FILE FOR DETAILS
#
#    Brewm's main class. It creates the majority of the main window GUI
#    and gets everything up and running.
#
#-------------------------------------------------------------------------------

def gravity_to_abv(og, fg):
    """Calculates ABV from original and final gravity.
    
    >>> gravity_to_abv(1.040, 1.010)
    5.0
    """
    pass
def abv_to_abg(abv):
    pass
def abg_to_abv(abg):
    pass
def abv_fg_to_og(abv, fg):
    pass
def og_atten_to_fg(og, atten):
    pass
def gravity_bitterness_to_bugu(og, fg, bitterness):
    pass
def gravity_bugu_to_bitterness(og, fg, bugu):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
