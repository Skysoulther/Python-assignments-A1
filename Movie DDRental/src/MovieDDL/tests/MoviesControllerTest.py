'''
Created on 27 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import Movie
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import MovieValidator
from MovieDDL.repository.RepositoryMovies import movieRepository
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.controller.ControllerMovie import movieController

class MoviesControllerTest(unittest.TestCase):
    '''
    Unit test-case for testing ControllerMovies Module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        validator1=MovieValidator()
        repoTest=movieRepository(validator1,"testMovies.txt")
        self.controlTest=movieController(repoTest)

    def testControllerMovies(self):
        '''
        Test the controller for MoviesRepositoryTest
        '''
        self.assertRaises(ControllerException,self.controlTest.add_movie,["aba","Test24","drama","Description24"])
        self.assertEqual(len(self.controlTest.get_allMovies()),5)
        self.controlTest.add_movie([24,"Test24","drama","Description24"])
        self.assertEqual(len(self.controlTest.get_allMovies()),6)
        self.assertRaises(RepositoryException,self.controlTest.add_movie,[24,"Test24","drama","Description24"])
        self.assertRaises(ControllerException,self.controlTest.remove_movie,"aba")
        self.controlTest.remove_movie(24)
        self.assertEqual(len(self.controlTest.get_allMovies()),5)
        self.assertRaises(ControllerException,self.controlTest.edit_movie,12,"Block him!")
        self.assertEqual(self.controlTest.get_allMovies()[5].get_description(),"Description5")
        self.controlTest.edit_movie(5, "The Description")
        self.assertEqual(self.controlTest.get_allMovies()[5].get_description(),"The Description")
        self.assertEqual(self.controlTest.return_movie_Id(5),self.controlTest.get_allMovies()[5])
        self.assertEqual(len(self.controlTest.search_movie(4, "the")),1)
        self.assertEqual(len(self.controlTest.search_movie(3, "act")),2)
        self.assertEqual(len(self.controlTest.search_movie(2, "test")),5)
        self.controlTest.edit_movie(5, "Description5")