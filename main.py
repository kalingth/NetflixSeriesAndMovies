from Netflix.Views.ETLSQL import NetFlixETpL


if __name__ == "__main__":
    nfl = NetFlixETpL("1BDPAq0Rp6iHcQLLe2zu_fVWaAbtOEQVO")
    nfl.exportCsvToFile("sample.csv")
    nfl.exportSqlToFile("sample.sql")
    # Por padrão, exporta para SQLite
    nfl.loadDatabase()
    # Exportando para o DB do Postgres
    nfl.loadDatabase("postgresql", "kalingth", "changeme", "netflix")
    # Exportando para o DB do MYSQL
    nfl.loadDatabase("mysql", "kalingth", "changeme", "netflix")
