'''
Created on 5 Nov 2016

@author: DDL
'''
from MovieDDL.domain import Validator
from MovieDDL.controller import ControllerMovie
from MovieDDL.controller import ControllerClient
from MovieDDL.controller import ControllerRental
from MovieDDL.controller import UndoController
from MovieDDL.ui import MenuUI
from MovieDDL.ui import GUI
from MovieDDL.repository import FileRepositoryMovies
from MovieDDL.repository import FileRepositoryClients
from MovieDDL.repository import FileRepositoryRentals
from MovieDDL.repository import RepositoryMovies
from MovieDDL.repository import RepositoryClients
from MovieDDL.repository import RepositoryRentals
from MovieDDL.repository import PickleRepositoryMovies
from MovieDDL.repository import PickleRepositoryClients
from MovieDDL.repository import PickleRepositoryRentals
from MovieDDL.repository import JSONRepositoryMovies
from MovieDDL.repository import JSONRepositoryClients
from MovieDDL.repository import JSONRepositoryRentals

class Application:
    
    def __init__(self):
        '''
        Creates the application
        ''' 
        self.__settings=Settings()
        movieValid=Validator.MovieValidator()
        clientValid=Validator.ClientValidator()
        rentalValid=Validator.RentalValidator()
        try:
            datas=self.__settings.getDatas()
            repository=self.__setRepositories(datas)
            undoController=UndoController.undoController()
            self.__movieControl=ControllerMovie.movieController(repository[0],movieValid,undoController)
            self.__clientControl=ControllerClient.clientController(repository[1],clientValid,undoController)
            self.__rentalControl=ControllerRental.rentalController(repository[0],repository[1],repository[2],rentalValid,undoController)
            self.__setUI(datas["ui"])
        except Exception as ve:
            print(str(ve))
    
    def run(self):
        '''
        run the application
        '''
        self.__mainMenu.run()
    
    def __setRepositories(self,datas):
        '''
        Set the proper repositories if possible
        Input: datas - a dictionary containing the properties from settings
        Output: repositories - a list containing all repositories
        '''
        repositories=[]
        files=[datas["movies"],datas["clients"],datas["rentals"]]
        if datas["repository"]=="inmemory":
            repositories.append(RepositoryMovies.movieRepository())
            repositories.append(RepositoryClients.clientRepository())
            repositories.append(RepositoryRentals.rentalRepository(repositories[0]))
        elif datas["repository"]=="textfiles":
            self.__validateFiles(files, "text")
            repositories.append(FileRepositoryMovies.movieFileRepository(datas["movies"]))
            repositories.append(FileRepositoryClients.clientFileRepository(datas["clients"]))
            repositories.append(FileRepositoryRentals.rentalFileRepository(repositories[0],datas["rentals"]))
        elif datas["repository"]=="binaryfiles":
            self.__validateFiles(files, "binary")
            repositories.append(PickleRepositoryMovies.moviePickleRepository(datas["movies"],))
            repositories.append(PickleRepositoryClients.clientPickleRepository(datas["clients"]))
            repositories.append(PickleRepositoryRentals.rentalPickleRepository(repositories[0],datas["rentals"]))
        elif datas["repository"]=="JSONfiles":
            self.__validateFiles(files, "json")
            repositories.append(JSONRepositoryMovies.movieJSONRepository(datas["movies"]))
            repositories.append(JSONRepositoryClients.clientJSONRepository(datas["clients"]))
            repositories.append(JSONRepositoryRentals.rentalJSONRepository(repositories[0],datas["rentals"]))
        else:
            raise ValueError("Repository property is invalid!")
        return repositories
    
    def __setUI(self,ui):
        '''
        Set the ui if possible
        Input: ui - a string
        Output: - 
        Exceptions: ValueError when the ui string is not valid
        '''
        uis={"menu":MenuUI.Menu,
              "gui":GUI.MenuGUI}
        ui=ui.lower()
        if ui in uis:
            self.__mainMenu=uis[ui](self.__movieControl,self.__clientControl,self.__rentalControl)
        else:
            raise ValueError("UI property is invalid!")
    
    def __validateFormat(self,string,format):
        '''
        validate the format of files
        Input: string - the file's name
               format - the format test
        Output: -
        Exceptions: ValueError if the format is not found in the file's name
        '''
        formats={"json":".json","text":".txt","binary":".pickle"}
        if string.find(formats[format])==-1:
            raise ValueError("The format of file \""+string+"\" is invalid!")
        return
    
    def __validateFiles(self,files,format):
        '''
        Validate the format of files
        Input: files - a list with the name of files
        Output: True if the validity of the files is right
        '''
        for file in files:
            self.__validateFormat(file, format)
        return True
            
class Settings:
    '''
    class for settings
    '''
    def __init__(self,fname="settings.properties"):
        '''
        initialize settings
        '''
        self.__fName=fname
        self.__loadData()
    
    def __loadData(self):
        '''
        load the info from settings file into a dictionary
        '''
        datas={}
        f=open(self.__fName,"r")
        for line in f:
            line.rstrip()
            if not "=" in line:
                continue
            attrs=line.split("=",1)
            datas[attrs[0].strip()]=attrs[1].strip()
        f.close
        self.__datas=datas
    
    def getDatas(self):
        '''
        get the datas from settings
        '''
        return self.__datas
try:
    app=Application()
    app.run()
except:
    pass