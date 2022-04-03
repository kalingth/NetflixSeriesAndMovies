import requests
import pandas as pd
from io import BytesIO


class Extract:
    uri: str
    rawData: bytes
    dataframe: pd.DataFrame

    def getData(self):
        # type: () -> None
        response = requests.get(self.uri)
        self.rawData = response.content

    def loadRawDataToDataframe(self):
        # type: () -> None
        file = BytesIO(self.rawData)
        self.dataframe = pd.read_csv(file, parse_dates=["Date"], dayfirst=True)

    def extractFromCSV(self, file):
        # type: (str) -> None
        self.dataframe = pd.read_csv(file, parse_dates=["Date"], dayfirst=True)

    def extractFromDrive(self, identifier):
        # type: (str) -> None
        base_uri = "https://drive.google.com/uc?export=download&id="
        self.uri = f"{base_uri}{identifier}"
        self.getData()
        self.loadRawDataToDataframe()
