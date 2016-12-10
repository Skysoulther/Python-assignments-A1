'''
Created on 9 Dec 2016

@author: DDL
'''

from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryMovies import movieRepository
import pickle

class moviePickleRepository(movieRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, fileName="movies.pickle"):
        '''
        Constructor for file repository
        Input: fileName - the name of the file
        Output: -
        '''
        movieRepository.__init__(self)
        self.__fName=fileName
        self.__loadFromFile()
        
    def add_movie(self, movie):
        '''
        Method to add a new movie
        Input: movie - object of Class movie
        Output: -
        '''
        movieRepository.add_movie(self, movie)
        self.__storeToFile()
    
    def remove_movie(self, Id):
        '''
        Method to remove a movie
        Input: Id - Id of the movie to remove
        Output: -
        '''
        movie=movieRepository.remove_movie(self, Id)
        self.__storeToFile()
        return movie
    
    def update_movie(self, Id, Desc):
        '''
        Method to edit the description of a movie
        Input: Id - id of the movie to edit
               Desc - The new description of the movie
        output: -
        '''
        movieRepository.update_movie(self, Id, Desc)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f=open(self.__fName,"rb")
        try:
            movies=pickle.load(f)
            for key in movies:
                movieRepository.add_movie(self, movies[key])
        except EOFError:
            movieRepository.__movies={}
        except Exception as e:
            raise FileRepositoryException(e)
        finally:
            f.close()
    
    def __storeToFile(self):
        f=open(self.__fName, "wb")
        self.__movies=movieRepository.get_all(self)
        pickle.dump(self.__movies, f)
        f.close