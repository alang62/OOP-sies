class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self, members):
        return True if members in self.__myTeam else False
    
    def __iter__(self):
        return iter(self.__myTeam)
    

    

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    x = iter(classmates)
    print(len(classmates))  
    print('Tim' in classmates)
    print('Sam' in classmates)
    
    for i in classmates:
        print(next(x))
        
    
main()

#4)
"""The difference between interfaces and implementation are that interfaces are what the user is able to
see and manipulate themselves thanks to the implementation running in the background. The idea is that
there are components to the implementation that allow the program to run, or the process to instantiate,
onto the interface, though the user does not need to know or understand the components of the implementation,
only that they are or are not giving them the result they expect in the interface."""
#5)
"""I would create an interface that allows the user to choose and access all of these storage mediums.
To begin, I would create an interactive application that shows storage options and management. To ensure
that there is less confusion for the masses, I would label subcategories for each one: Local, Cloud, etc.
and allow the user to choose and illustrate some visible metric depicting total storage available. This way,
it shows all of the possible storage mediums to access and give the user the simple option of choosing
which one to store their data to."""
