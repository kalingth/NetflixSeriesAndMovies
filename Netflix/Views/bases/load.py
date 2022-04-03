from copy import copy
from ...conf.db_session import createTables, createSession
from ...Models.movies import Movies
from ...Models.series import Series
from tqdm import tqdm


class Load:
    createQuery: str
    insertQuery: str

    @staticmethod
    def sanitizeString(string):
        return string.replace("'", "''")\
                     .replace("`", "``")

    @staticmethod
    def sanitize(row):
        # type: (list) -> list
        for column in range(len(row)):
            if type(row[column]) is str:
                row[column] = Load.sanitizeString(row[column])
        return row

    def createDatabaseQuery(self):
        # type: () -> None
        output = (
            "CREATE TABLE IF NOT EXISTS series(\n"
            "  id INT PRIMARY_KEY AUTOINCREMENT,\n"
            "  title VARCHAR(50) NOT NULL, \n"
            "  season VARCHAR(20),\n"
            "  ep_title VARCHAR(50),\n"
            "  lastView DATETIME NOT NULL\n"
            ");\n"
            "CREATE TABLE IF NOT EXISTS movies(\n"
            "  id INT PRIMARY_KEY AUTOINCREMENT,\n"
            "  title VARCHAR(50) NOT NULL, \n"
            "  lastView DATETIME NOT NULL\n"
            ");\n"
        )
        self.createQuery = output

    def insertDatabaseQuery(self, data):
        # type: (list) -> None
        sqlInsert = ""
        for watched in data:
            buffer = copy(watched)
            audioVisualScope, audioVisualData = buffer.pop(0), buffer
            if audioVisualScope == 2:
                sqlInsert += ("INSERT INTO series"
                              "(title, season, ep_title, lastView) "
                              "VALUES('{}', '{}', '{}', '{}');\n")\
                    .format(* self.sanitize(audioVisualData))
            else:
                sqlInsert += ("INSERT INTO movies"
                              "(title, lastView) "
                              "VALUES('{}', '{}');\n")\
                    .format(* self.sanitize(audioVisualData))
        self.insertQuery = sqlInsert

    def insertData(self, session):
        for count in tqdm(range(len(self.watchedSeriesAndFilms)),
                          desc="Inserindo dados", unit=" dados"):
            buffer = copy(self.watchedSeriesAndFilms[count])
            audioVisualScope, audioVisualData = buffer.pop(0), buffer
            if audioVisualScope == 2:
                serie = Series(* audioVisualData)
                session.add(serie)
            else:
                movie = Movies(* audioVisualData)
                session.add(movie)
            session.commit()

    def loadDatabase(self, *args, **kwargs):
        createTables(*args, **kwargs)

        with createSession(*args, **kwargs) as session:

            self.insertData(session)
            session.add

            session.commit()
