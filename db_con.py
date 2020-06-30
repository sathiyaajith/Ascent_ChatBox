import sqlite3

try:
    sqliteConnection = sqlite3.connect("C:\\Users\\sathi\\rasa_new\\database_rasa.sqlite")
    cursor = sqliteConnection.cursor()

    sqlite_select_Query = "select * from trainee_details;"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print(record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()


