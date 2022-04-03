from pandas import DataFrame
from typing import Union


class Transform:
    watchedSeriesAndFilms = list()  # type: list
    dataframe = DataFrame()  # type: DataFrame

    @staticmethod
    def seriesDump(rawString):
        # type: (str) -> tuple[int, str, str, str]
        title, season, ep_title = rawString.rsplit(": ", 2)
        return 2, title, season, ep_title

    @staticmethod
    def dataParser(rawString):
        # type: (str) -> Union[tuple[int, str, str, str], tuple[int, str]]
        if rawString.count(':') >= 2:
            return Transform.seriesDump(rawString)
        title = rawString
        return 1, title

    def transformData(self):
        # type: () -> None
        for rawString, date in self.dataframe.values:
            self.watchedSeriesAndFilms.append([
                * self.dataParser(rawString), date
            ])
