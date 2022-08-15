import mysql.connector
import time
now = time.time()
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='entertainer_details',
                                         user='root',
                                         password='root')

    mySql_insert_query = "SELECT DISTINCT movie_name FROM entertainer_details.kollywood_entertainer_films;"

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    result = cursor.fetchall()
    print(len(result))
    print(result[1341])
    '''for i in range(2000, len(result)):
        if "Dead Reckoning" == result[i][0]:
            print("index:", i)
            break'''
    #connection.commit()
    #print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

print("Time taken to finish", time.time()-now)