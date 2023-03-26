class Options:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-D632DF2\SQLEXPRESS;DATABASE=BooksAndFilms;'
        # User
        self.getUsers = 'exec GetUsers'
        self.updateUser = 'exec UpdateUser'
        self.addValuesInUser = 'exec AddValuesInUser'
        self.deleteUser = 'exec DeleteUser'
        # Unit
        self.getUnits = 'exec GetUnits'
        self.getUnitsByUser = 'exec GetUnitsByUser'
        self.getUnitsByUsers = 'exec GetUnitsByUsers'
        self.getUnitsAndTitles = 'exec GetUnitsAndTitles'
        self.getPopularityOfUnit = 'exec GetPopularityOfUnit'
        self.getPopularityOfUnits = 'exec GetPopularityOfUnits'
        self.fullInformationAboutUnits = 'exec FullInformationAboutUnits'
        self.fullInformationAboutUnit = 'exec FullInformationAboutUnit'
        self.addValuesInUnit = 'exec AddValuesInUnit'
        self.updateUnit = 'exec UpdateUnit'
        self.deleteUnit = 'exec DeleteUnit'
        self.deleteTypeOfUnit = 'exec DeleteTypeOfUnit'
        # Title
        self.getTitle = 'exec GetTitle'
        self.addValuesInTitle = 'exec AddValuesInTitle'
        self.updateTitle = 'exec UpdateTitle'
        self.deleteTitle = 'exec DeleteTitle'
        self.deleteTypeOfTitle = 'exec DeleteTypeOfTitle'
        self.getUnitsAndTitles = 'exec GetUnitsAndTitles'
        self.getUsersAndTitles = 'exec GetUsersAndTitles'
        self.getTitlesByUsers = 'exec GetTitlesByUsers'
        self.getTitlesByUser = 'exec GetTitlesByUser'
        self.getTitlesByUnits = 'exec GetTitlesByUnits'
        self.getTitlesByUnit = 'exec GetTitlesByUnit'

