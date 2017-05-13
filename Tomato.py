class Tomato:
    __tomatoName = None
    __tomatoColour = None
    __tomatoNationality = None

    def __init__(self, tomatoName, tomatoColour, tomatoNationality):
        if tomatoName is not None and tomatoColour is not None and tomatoNationality is not None:
            self.__tomatoName = tomatoName
            self.__tomatoColour = tomatoColour
            self.__tomatoNationality = tomatoNationality

    def getName(self):
        if self.__tomatoName is not None:
            return self.__tomatoName

    def getColour(self):
        if self.__tomatoColour is not None:
            return self.__tomatoColour

    def getTomatoNationality(self):
        if self.__tomatoNationality is not None:
            return self.__tomatoNationality
