'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Rental

class rentalController:
    '''
    Contains functions which operates on rentals
    '''
    def __init__(self,repoRental):
        '''
        Creates a controller for rentals
        '''
        self._repository=repoRental