'''
Created on 4 Nov 2016

@author: DDL
'''

class Menu:
    def __init__(self,movControl,cliControl,renControl):
        '''
        Creates a menu which uses controllers
        '''
        #self._movieController=movControl
        #self._clientController=cliControl
        #self._rentalController=renControl
        self._manageMovieMenu=self.ManageMovie(movControl)
        self._manageClientMenu=self.ManageClient(cliControl)
        self._manageRentalMenu=self.ManageRental(movControl,cliControl,renControl)
    
    class ManageMovie:
        '''
        Class for the manageMovieMenu
        '''
        def __init__(self,movControl):
            '''
            Creates manage menu
            '''
            self._movieController=movControl
        
        def _press(self):
            '''
            Creates a pause to see what happens in the app
            '''
            input("Press any key to continue...")
        
        def manageMovies(self):
            '''
            The main menu for movies management
            '''
            optionsMovie={1:self.addMovie,2:self.removeMovie,3:self.showAllMovies}
            while True:
                self.printMoviesMenu()
                try:
                    opMovie=int(input("Please enter an option: "))
                    if opMovie in optionsMovie:
                        optionsMovie[opMovie]()
                    elif opMovie==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\nOption is invalid!\n"+"-"*30)
                    self._press()
        
        def printMoviesMenu(self):
            '''
            Prints the menu for managing movies
            '''
            menuString="\n  Manage Movies \n"+"-"*30+"\n"
            menuString+="1. Add movie \n"
            menuString+="2. Remove movie \n"
            menuString+="3. Show all movies \n"
            menuString+="0. Go back to main menu \n"+"-"*30
            print(menuString)
                
        def _readMovie(self):
            '''
            read movie's data
            Input: -
            Output: the movie's properties as a list
            Exceptions: -
            '''
            movie=[]
            movie.append(input("Enter the ID of the movie: "))
            movie.append(input("Enter the title of the movie: "))
            movie.append(input("Enter the genre of the movie: "))
            movie.append(input("Add a description: "))
            return movie
        
        def addMovie(self):
            '''
            UI to add a movie in the repository
            '''
            try:
                movie=self._readMovie()
                self._movieController.add_movie(movie)
                print("-"*30+"\nMovie was added!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
                
        def removeMovie(self):
            '''
            UI to remove a movie from the repository
            '''
            try:
                removeId=input("Enter the id of the movie that you want to remove: ")
                self._movieController.remove_movie(removeId)
                print("-"*30+"\nMovie was removed\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
            
        def seeDescrisption(self):
            '''
            UI to see the description of a movie by ID
            '''
            try:
                seeId=input("Enter the id of the movie whose description you want to see: ")
                movie=self._movieController.return_movie_Id(seeId)
                print("\nTitle: "+movie.get_title())
                print("Description: "+movie.get_description()+"\n")
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
                
        def printSeeDescription(self):
            '''
            prints a mini-menu for seeing the description or going back
            '''
            menuString="-"*35+"\n1. See the description of a movie\n"
            menuString+="0. Go back to Manage Movies menu\n"
            menuString+="-"*35
            print(menuString)
            
        def seeDescriptionMenu(self):
            '''
            The menu for seeing the descriptions
            '''
            while True:
                self.printSeeDescription()
                try:
                    opDescription=int(input("Enter your option: "))
                    if opDescription==1:
                        self.seeDescrisption()
                    elif opDescription==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\n"+"Enter a valid option!"+"\n"+"-"*30)
                    self._press()
         
        def printList(self,lists):
            '''
            Print a list of movies
            ''' 
            print("\nID    TITLE"+" "*47+"GENRE\n"+"-"*65)
            if len(lists)==0:
                print("There are no movies!")
            else:
                for key in lists:
                    print(str(lists[key]))
            print("-"*65)          
                    
        def showAllMovies(self):
            '''
            UI to show all the available movies
            '''
            try:
                movies=self._movieController.get_allMovies()
                self.printList(movies)
                self.seeDescriptionMenu()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
        def RentSelectMovie(self,movies):
            '''
            UI to rent a movie
            '''
            while True:
                try:
                    movieId=int(input("Enter the ID of the movie you want to rent (it should be from the list of movies you searched): "))
                    if movieId in movies:
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\nThe ID is invalid!\n"+"-"*30)
        
        def printRentMenu(self):
            '''
            Prints a mini-menu for renting
            '''
            menuString="-"*35+"\n1. Rent one of these movies\n"
            menuString+="0. Go back to choosing a field\n"+"-"*35
            print(menuString)
        
        def RentMenu(self,movies):
            '''
            The menu for renting a movie
            '''
            while True:
                self.printRentMenu()
                try:
                    opRent=int(input("Enter your option: "))
                    if opRent==1:
                        self.RentSelectMovie(movies)
                    elif opRent==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\n"+"Enter a valid option!"+"\n"+"-"*30)
                    self._press()
            
        def _startSearch(self,field):
            '''
            Searches the partial string in the repository of movies
            '''
            messages=[0,"Enter the ID (or a part of it): ",
                      "Enter the Title (or a part of it): ",
                      "Enter the Genre (or a part of it): ",
                      "Enter the Description (or a part of it): "]
            information=input(messages[field])
            askedMovies=self._movieController.search_movie(field,information)
            self.printList(askedMovies)
            if len(askedMovies)>0:
                self.RentMenu(askedMovies)
            else:
                self._press()
        
        def searchMovies(self):
            '''
            the main menu for searching movies
            '''
            fieldOptions=[1,2,3,4]
            while True:
                self.printSearchMoviesFields()
                try:
                    field=int(input("Enter your option: "))
                    if field in fieldOptions:
                        self._startSearch(field)
                    elif field==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\nOption is invalid!\n"+"-"*30)
                    self._press()
            
        def printSearchMoviesFields(self):
            '''
            Prints the menu of fields for movies
            '''
            menuString="\n Search a movie by a field:\n"+"-"*30+"\n"
            menuString+="1. Search by ID\n"
            menuString+="2. Search by Title\n"
            menuString+="3. Search by Genre\n"
            menuString+="4. Search by Description\n"
            menuString+="0. Go back to main menu\n"+"-"*30+"\n"
            print(menuString)
        
    ###################################################################################
    
    
    class ManageClient:
        '''
        Class for managing client menu
        '''
        def __init__(self,cliControl):
            '''
            Creates menu for managinh the clients
            '''
            self._clientController=cliControl
            
        def _readClient(self):
            '''
            read client's data
            Input: -
            Output: the client's properties as a list
            Exceptions: -
            '''
            client=[]
            try:
                client.append(int(input("Enter the ID of the client: ")))
                client.append(input("Enter the name of the client: "))
                return client
            except ValueError:
                print("The ID should be a number!")
        
        def _press(self):
            '''
            Creates a pause to see what happens in the list
            '''
            input("Press any key to continue...")
        
        def addClient(self):
            '''
            UI to add a client in the repository
            '''
            try:
                client=self._readClient()
                self._clientController.add_client(client)
                print("-"*30+"\nClient was added\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
        def removeClient(self):
            '''
            UI to remove a client from the repository
            '''
            try:
                removeId=input("Enter the id of the client you wnat to remove: ")
                self._clientController.remove_client(removeId)
                print("-"*30+"\nClient was removed!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
            
        def showAllClients(self):
            '''
            UI to show all the available clients
            '''
            try:
                clients=self._clientController.get_allClients()
                print("\nID   NAME\n"+"-"*40)
                if len(clients)==0:
                    print("There are no clients... We are broke")
                else:
                    for key in clients:
                        print(str(clients[key]))
                print("-"*40)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
                
        def manageClients(self):
            '''
            the main menu for clients management
            '''
            optionsClient={1:self.addClient,2:self.removeClient,3:self.showAllClients}
            while True:
                self.printClientsMenu()
                try:
                    opClient=int(input("Please enter an option: "))
                    if opClient in optionsClient:
                        optionsClient[opClient]()
                    elif opClient==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\nOption is invalid!\n"+"-"*30)
                    self._press()
                
            
        def printClientsMenu(self):
            '''
            Prints the menu for clients management
            '''
            menuString="\n  Manage Clients \n"+"-"*30+"\n"
            menuString+="1. Add client \n"
            menuString+="2. Remove client \n"
            menuString+="3. Show all clients \n"
            menuString+="0. Go back to main menu \n"+"-"*30
            print(menuString)
    
    #################################################################

    class ManageRental:
        '''
        Class for managing the rental
        '''   
        def __init__(self,movControl,cliControl,renControl):
            '''
            Creates a rental mangement object
            '''
            self._movieController=movControl
            self._clientController=cliControl
            
    #########################################################################
    
    def _printMenu(self):
        '''
        Prints the main men8u of the app
        '''
        menuString="\n  Available options \n"+"-"*30+"\n"
        menuString+="1. Manage movies \n"
        menuString+="2. Manage clients \n"
        menuString+="3. Search movies & Rent movies \n"
        menuString+="4. Return a movie\n"
        menuString+="0. Exit\n"+"-"*30
        print(menuString)
    
    def _press(self):
        '''
        Creates a pause to see what happens in the app
        '''
        input("Press any key to continue...")
        
    def run(self):
        options={1:self._manageMovieMenu.manageMovies, 2:self._manageClientMenu.manageClients,
                 3:self._manageMovieMenu.searchMovies}
        while True:
            self._printMenu()
            try:
                option=int(input("Please enter an option: "))
                if option in options:
                    options[option]()
                elif option==0:
                    print("Thanks for using the app! Have a nice day!:)")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("-"*30+"\nOption is invalid!\n"+"-"*30)
                self._press()
    