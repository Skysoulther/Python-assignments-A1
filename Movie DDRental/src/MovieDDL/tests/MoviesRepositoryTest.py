'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import Movie
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import MovieValidator
from MovieDDL.repository.RepositoryMovies import movieRepository

class MoviesRepositoryTest(unittest.TestCase):
    '''
    Unit test-case for testing RepositoryMovies module
    '''
    
    def setUp(self):
        '''
        the setup of data
        '''
        self.movieList1=[17,"Test17","western","Description17"]
        self.movieList2=[2,"Test56","horror","Description56"]
        validator1=MovieValidator()
        self.repoTest=movieRepository(validator1,"testMovies.txt")

    def testRepositoryMovies(self):
        '''
        Test the repository of movies
        '''
        self.repoTest.add_movie(self.movieList1)
        self.assertRaises(RepositoryException,self.repoTest.add_movie,self.movieList1)
        self.assertRaises(RepositoryException,self.repoTest.add_movie,self.movieList2)
        self.assertRaises(RepositoryException,self.repoTest.remove_movie,6)
        self.repoTest.remove_movie(17)
        self.assertRaises(RepositoryException,self.repoTest.return_movie_Id,17)
        self.assertEqual(self.repoTest.return_movie_Id(5).get_title(),"Test5")
        self.assertTrue(self.repoTest.find_by_ID,2)
        self.assertFalse(self.repoTest.find_by_ID(17))
        self.assertEqual(self.repoTest.search_movie(1, "6"),{})
        self.assertEqual(len(self.repoTest.search_movie(2, "test")),5)
        self.assertEqual(len(self.repoTest.search_movie(4, "descr")),5)
        self.assertEqual(len(self.repoTest.search_movie(3, "ho")),1)