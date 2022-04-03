# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:07:25 2022

@author: walla
"""


# from .. import db
from .bases.extract import Extract
from .bases.transform import Transform
from .bases.load import Load


class NetFlixETpL(Extract, Transform, Load):
    """Class NetFlixETpL

    This class will extract data from csv on Google Drive, transform the data
    and pre load with an exported SQL Query.
    """

    __id: str

    def extractTransformProccess(self):
        # type: () -> None
        self.extractFromDrive(self.__id)
        self.transformData()

    def exportCsvToFile(self, name):
        # type: (str) -> None
        with open(name, 'wb') as file:
            file.write(self.rawData)

    def exportSQL(self):
        # type: () -> str
        self.createDatabaseQuery()
        self.insertDatabaseQuery(self.watchedSeriesAndFilms)

        export = self.createQuery
        export += self.insertQuery
        return export

    def exportSqlToFile(self, name):
        # type: (str) -> None
        with open(name, 'wb') as file:
            coded = self.exportSQL().encode("utf-8")
            file.write(coded)

    def __init__(self, id):
        # type: (str) -> None
        self.__id = id
        self.extractTransformProccess()
