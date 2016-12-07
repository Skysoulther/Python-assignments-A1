'''
Created on 4 Nov 2016

@author: DDL
'''
import datetime

class Menu:
    def __init__(self,movControl,cliControl,renControl):
        '''
        Creates a menu which uses controllers
        '''
        self._manageMovieMenu=self.ManageMovie(movControl)
        self._manageClientMenu=self.ManageClient(cliControl,renControl)
        self._manageRentalMenu=self.ManageRental(renControl)
    
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
            optionsMovie={1:self.addMovie,2:self.removeMovie,3:self.showAllMovies,4:self.editMovie,
                          5:self.searchMovies}
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
            menuString+="3. Show available movies \n"
            menuString+="4. Edit the description of a movie \n"
            menuString+="5. Search movie \n"
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
        
        def editMovie(self):
            '''
            UI to edit a description of a movie
            '''
            try:
                editId=input("Enter the id of the movie that you want to edit: ")
                editDesc=input("Add the new description: ")
                self._movieController.edit_movie(editId,editDesc)
                print("-"*30+"\nMovie was updated\n"+"-"*30)
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
                self._press()
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
        def __init__(self,cliControl,renControl):
            '''
            Creates menu for managinh the clients
            '''
            self._clientController=cliControl
            self._rentalController=renControl
            
        def _readClient(self):
            '''
            read client's data
            Input: -
            Output: the client's properties as a list
            Exceptions: -
            '''
            client=[]
            client.append(input("Enter the ID of the client: "))
            client.append(input("Enter the name of the client: "))
            return client
        
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
                removeId=input("Enter the id of the client you want to remove: ")
                client=self._clientController.remove_client(removeId)
                self._rentalController.remove_rentals(client)
                print("-"*30+"\nClient was removed!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
        def printList(self,lists):
            '''
            Print a list of movies
            ''' 
            print("\nID    NAME\n"+"-"*40)
            if len(lists)==0:
                print("There are no clients... We are broke")
            else:
                for key in lists:
                    print(str(lists[key]))
            print("-"*40)
            
        def showAllClients(self):
            '''
            UI to show all the available clients
            '''
            try:
                clients=self._clientController.get_allClients()
                self.printList(clients)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
            
        def editClient(self):
            '''
            UI to edit a description of a movie
            '''
            try:
                editId=input("Enter the id of the client that you want to edit: ")
                editName=input("Enter the new name of the client: ")
                self._clientController.edit_client(editId,editName)
                print("-"*30+"\nClient was updated\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
            
        def _startSearch(self,field):
            '''
            Searches the partial string in the repository of movies
            '''
            messages=[0,"Enter the ID (or a part of it): ",
                      "Enter the Name (or a part of it): "]
            information=input(messages[field])
            askedClients=self._clientController.search_client(field,information)
            self.printList(askedClients)
            self._press()
        
        def searchClients(self):
            '''
            the main menu for searching movies
            '''
            fieldOptions=[1,2]
            while True:
                self.printSearchClientsFields()
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
            
        def printSearchClientsFields(self):
            '''
            Prints the menu of fields for movies
            '''
            menuString="\n Search a client by a field:\n"+"-"*30+"\n"
            menuString+="1. Search by ID\n"
            menuString+="2. Search by Name\n"
            menuString+="0. Go back to main menu\n"+"-"*30+"\n"
            print(menuString)
           
        def manageClients(self):
            '''
            the main menu for clients management
            '''
            optionsClient={1:self.addClient,2:self.removeClient,3:self.showAllClients,4:self.editClient,
                           5:self.searchClients}
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
            menuString+="4. Edit the name of a client\n"
            menuString+="5. Search clients\n"
            menuString+="0. Go back to main menu \n"+"-"*30
            print(menuString)
    
    #################################################################

    class ManageRental:
        '''
        Class for managing the rental
        '''   
        def __init__(self,renControl):
            '''
            Creates a rental management object
            '''
            self._rentalController=renControl
        
        def _press(self):
            '''
            Creates a pause to see what happens in the list
            '''
            input("Press any key to continue...")
        
        def returnMovie(self):
            '''
            UI to return a movie
            '''
            try:
                clientId=input("Enter the ID of the client: ")
                self._rentalController.checks_client(clientId)
                movieId=input("Enter the ID of the movie you want to return: ")
                self._rentalController.checks_movie2(movieId)
                self._rentalController.return_rental(clientId,movieId)
                print("-"*30+"\nMovie was returned!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()    
        
        def rentMovie(self):
            '''
            UI to rent a movie
            '''
            try:
                movieId=input("Enter the ID of the movie you want to rent: ")
                self._rentalController.checks_movie(movieId)
                clientId=input("Enter the ID of the client who rents the movie: ")
                self._rentalController.checks_client(clientId)
                today=datetime.date.today()
                rental=[int(movieId),int(clientId),today]
                self.RentMenu(rental)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
        def printRentMenu(self):
            '''
            shows the menu for renting
            '''
            menuString="\n Choose the period of time: \n"+"-"*30+"\n"
            menuString+="1. 3 days \n"
            menuString+="2. 5 days \n"
            menuString+="3. 1 week (7 days) \n"
            menuString+="4. 2 weeks (14 days)\n"
            menuString+="0. Go back to main menu \n"+"-"*30
            print(menuString)
                   
        def RentMenu(self,rental):
            '''
            The menu for renting a movie
            '''
            options={1:3,2:5,3:7,4:14}
            while True:
                self.printRentMenu()
                try:
                    opRent=int(input("Enter your option: "))
                    if opRent in options:
                        dueDate=rental[2]+datetime.timedelta(days=options[opRent])
                        rental.append(dueDate)
                        self._rentalController.rent_movie(rental)
                        print("-"*50+"\nThe movie was rented! Return Date: "+str(dueDate.strftime ("%d.%m.%Y"))+"\n"+"-"*50)
                        break
                    elif opRent==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\n"+"Enter a valid option!"+"\n"+"-"*30)
                    self._press()
        
        def printStatisticsMenu(self):
            '''
            Shows the menu for statistics
            '''
            menuString="\n Statistics: \n"+"-"*30+"\n"
            menuString+="1. Most rented movies \n"
            menuString+="2. Most active clients \n"
            menuString+="3. All rentals \n"
            menuString+="4. Late rentals\n"
            menuString+="0. Go back to main menu \n"+"-"*30
            print(menuString)
            
            
        def statisticsMenu(self):
            '''
            The menu for statistics
            '''
            statisticsOptions={1:self._mostRentedMovies,2:self._mostActiveClients,
                               3:self._allRentals,4:self._lateRentals}
            while True:
                self.printStatisticsMenu()
                try:
                    opStat=int(input("Enter your option: "))
                    if opStat in statisticsOptions:
                        statisticsOptions[opStat]()
                    elif opStat==0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("-"*30+"\n"+"Enter a valid option!"+"\n"+"-"*30)
                    self._press()
        
        def _allRentals(self):
            '''
            UI for all rentals list
            '''
            rentals=self._rentalController.all_rentals()
            print("The list of all rentals is:")
            print(self._createList(rentals,1))
            self._press()
            
        def _mostRentedMovies(self):
            '''
            UI for most rented movies
            '''
            options={1:self._rentalController.most_rented,2:self._rentalController.most_rented}
            self.printMostRentedMenu()
            try:
                option=int(input("Please enter an option: "))
                if option in options:
                    mostRented=options[option](option)
                    print("The list of most rented movies is:")
                    print(self._createList(mostRented,1))
                    self._press()
                else:
                    raise ValueError
            except ValueError:
                print("-"*30+"\nOption is invalid!\n"+"-"*30)
                self._press()
            
        def _mostActiveClients(self):
            '''
            UI for most active clients
            '''
            mostActive=self._rentalController.active_clients()
            print("The list of most active students is:")
            print(self._createList(mostActive,2))
            self._press()
        
        def _lateRentals(self):
            '''
            UI for late rentals
            '''
            lateRentals=self._rentalController.late_rentals()
            print("The list of late rentals in descending order is:")
            print(self._createList(lateRentals,1))
            self._press()
            
        def printMostRentedMenu(self):
            '''
            Shows the mini-menu for most-rented movies
            '''
            menuString="\nSort the rented movies\n"+"-"*30+"\n"
            menuString+="1. Sort by number of days\n"
            menuString+="2. Sort by number of times\n"
            menuString+="-"*30
            print(menuString)
        
        def _createList(self, lista,typeL):
            '''
            Turns a list into a string
            Input: lista - a list of objects
            Output: stringList -  the list as a string
            Exceptions: -
            '''
            if typeL==1:
                stringList="\nID    TITLE"+" "*47+"GENRE"+" "*10+"Sort"+"\n"+"-"*85
            elif typeL==2:
                stringList="\nID    NAME"+" "*21+"Sort"+"\n"+"-"*50
            if(len(lista)==0):
                stringList+="\n The list is empty!"
            else:
                for i in range(len(lista)):
                        stringList+="\n"+str(lista[i])
            if typeL==1:
                stringList+="\n"+"-"*85
            elif typeL==2:
                stringList+="\n"+"-"*50
            return stringList 
        
        def undo(self):
            '''
            UI for undo
            '''
            try:
                self._rentalController.undo()
                print("-"*30+"\nUndo completed!!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()
        
        def redo(self):
            '''
            UI for undo
            '''
            try:
                self._rentalController.redo()
                print("-"*30+"\nRedo completed!!\n"+"-"*30)
                self._press()
            except Exception as ex:
                print("-"*30+"\n"+str(ex)+"-"*30)
                self._press()    
        
    #########################################################################
    
    def _printMenu(self):
        '''
        Prints the main men8u of the app
        '''
        menuString="\n  Available options \n"+"-"*30+"\n"
        menuString+="1. Manage movies \n"
        menuString+="2. Manage clients \n"
        menuString+="3. Rent movies \n"
        menuString+="4. Return a movie\n"
        menuString+="5. Statistics\n"
        menuString+="6. Undo\n"
        menuString+="7. Redo\n"
        menuString+="0. Exit\n"+"-"*30
        print(menuString)
    
    def _press(self):
        '''
        Creates a pause to see what happens in the app
        '''
        input("Press any key to continue...")
        
    def run(self):
        options={1:self._manageMovieMenu.manageMovies, 2:self._manageClientMenu.manageClients,
                 3:self._manageRentalMenu.rentMovie, 4:self._manageRentalMenu.returnMovie, 5:self._manageRentalMenu.statisticsMenu,
                 6:self._manageRentalMenu.undo, 7:self._manageRentalMenu.redo }
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
    