'''
Created on 10 Dec 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryMovies import movieRepository
from MovieDDL.domain.Entities import Movie
import json
import pickle

class movieJSONRepository(movieRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, fileName="movies.json"):
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
        f=open(self.__fName,"r")
        try:
            movies=json.load(f)
            for key in movies:
                movie=self._JSONtoMovie(movies[key])
                movieRepository.add_movie(self, movie)
        except EOFError:
            movieRepository.__movies={}
        except Exception as e:
            raise FileRepositoryException(e)
        finally:
            f.close()
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        movies={}
        self.__movies=movieRepository.get_all(self)
        for key in self.__movies:
            movies[key]=json.dumps(self.__movies[key].__dict__)
        json.dump(movies, f)
        f.close
    
    def _JSONtoMovie(self,object):
        '''
        Convert JSON object to Movie
        '''
        object=json.loads(object)
        title=object["_Movie__title"]
        description=object["_Movie__description"]
        id=object["_Movie__movieID"]
        genre=object["_Movie__genre"]
        return Movie(id,title,description,genre)
        
        