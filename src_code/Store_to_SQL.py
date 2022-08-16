import mysql.connector
from src_code.Extract_data import Entertainer
from src_code.Movie_class import Movie
from src_code.Movie_class import Movie_ob
from src_code.awards_class import Awards
from src_code.salary_class import Salary
class Store:

    def insert_person_details_into_sql(self, name, database_name, table_name):
        "This function will insert the details about the person into MySQL database"
        ent = Entertainer(name)
        person_details = ent.get_person_details()

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=database_name,
                                                 user='root',
                                                 password='root')

            mySql_insert_query = "INSERT INTO " + table_name + " (name, DOB, height, nicknames, quotes, mini_biography, trade_mark, headshot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, person_details)
            connection.commit()
            print(cursor.rowcount, "Record inserted " + table_name + " successfully into  table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into " + table_name + " table {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    def insert_list_of_movies(self, name, database_name, table_name):
        "This function will insert the list of movies acted by the person into the MySQL database"
        ent = Entertainer(name)
        movies_list = ent.get_person_movie_list()
        mo = Movie_ob()
        if movies_list:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database=database_name,
                                                     user='root',
                                                     password='root')
                mySql_insert_query = "INSERT INTO " + table_name + '''(entertainer_name, movie_name, year) 
                                    VALUES (%s, %s, %s)'''
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM "+table_name)
                rows_count = cursor.fetchall()[0][0]
                for i in range(len(movies_list)):
                    movie_name = mo.get_movie_name(movies_list[i])
                    movie_year = mo.get_movie_year_of_release(movies_list[i])
                    input_data = (name, movie_name, movie_year)
                    cursor.execute(mySql_insert_query, input_data)
                    connection.commit()
                cursor.execute("SELECT COUNT(*) FROM " + table_name)
                print(cursor.fetchall()[0][0]-rows_count, "Record inserted " + table_name + " successfully into  table")
                cursor.close()

            except mysql.connector.Error as error:
                print("Failed to insert record into " + table_name + "table {}".format(error))

            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection is closed")

    def insert_person_award_details(self, name, database_name, table_name):
        "This function will insert the Person's award details into MySQL database"
        ent = Entertainer(name)
        awards_list = ent.get_person_awards()
        awa = Awards()
        if awards_list:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database=database_name,
                                                     user='root',
                                                     password='root')
                mySql_insert_query = "INSERT INTO " + table_name + " (entertainer_name, award, year, prize, category, result, movie_name, shared_with) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM "+ table_name)
                rows_count = cursor.fetchall()[0][0]
                for i in range(len(awards_list)):
                    award_dic = awards_list[i]
                    award = awa.get_award_name(award_dic)
                    year = awa.get_year(award_dic)
                    prize = awa.get_prize(award_dic)
                    category = awa.get_category(award_dic)
                    result = awa.get_result(award_dic)
                    movie_name = awa.get_award_movie_name(award_dic)
                    shared_with = awa.get_shared_with(award_dic)
                    input_data = (name, award, year, prize, category, result, movie_name, shared_with)
                    cursor.execute(mySql_insert_query, input_data)
                    connection.commit()
                cursor.execute("SELECT COUNT(*) FROM " + table_name)
                print(cursor.fetchall()[0][0]-rows_count, "Record inserted " + table_name + " successfully into  table")
                cursor.close()

            except mysql.connector.Error as error:
                print("Failed to insert record into " + table_name + " table {}".format(error))

            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection is closed")

    def insert_person_salary_details(self, name, database_name, table_name):
        ent = Entertainer(name)
        salary_list = ent.get_person_salary_list()
        sal = Salary()

        if salary_list:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database=database_name,
                                                     user='root',
                                                     password='root')
                mySql_insert_query = "INSERT INTO " + table_name + '''(entertainer_name, movie_name, year, salary) 
                                    VALUES (%s, %s, %s, %s)'''
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM "+table_name)
                rows_count = cursor.fetchall()[0][0]
                for i in range(len(salary_list)):
                    salary_item = salary_list[i]
                    movie_name = sal.get_salary_movie_name(salary_item)
                    year = sal.get_salary_movie_year(salary_item)
                    salary = sal.get_salary_amount(salary_item)
                    input_data = (name, movie_name, year, salary)
                    cursor.execute(mySql_insert_query, input_data)
                    connection.commit()
                cursor.execute("SELECT COUNT(*) FROM " + table_name)
                print(cursor.fetchall()[0][0]-rows_count, "Record inserted " + table_name + " successfully into  table")
                cursor.close()

            except mysql.connector.Error as error:
                print("Failed to insert record into " + table_name + "table {}".format(error))

            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection is closed")

    def get_movie_list_and_store_movie_details(self, database_name, table_name):

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database="entertainer_details",
                                                 user='root',
                                                 password='root')

            mySql_insert_query = "SELECT DISTINCT movie_name FROM entertainer_details.kollywood_entertainer_films;"

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            movie_list = cursor.fetchall()
            print("Movie list has been fetched from database")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into entertainer_films table {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection for fetching the movie list is closed")


        if movie_list:
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database=database_name,
                                                     user='root',
                                                     password='root')
                mySql_insert_query = "INSERT INTO " + table_name + '''(movie_name, rating, plot, runtime, cover_url, year, genres, languages, directors, writers, producers, composers, cinematographers, editors) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM "+table_name)
                rows_count = cursor.fetchall()[0][0]
                for i in range(len(movie_list)):
                    movie_name = movie_list[i][0]
                    print("Starting to fetch details about:", movie_name)
                    ent = Entertainer(movie_name)
                    movie_details = ent.get_movie_details()
                    cursor.execute(mySql_insert_query, movie_details)
                    connection.commit()
                    print("Added details about:", movie_name)
                    print("   ")
                cursor.execute("SELECT COUNT(*) FROM " + table_name)
                print(cursor.fetchall()[0][0]-rows_count, "Record inserted " + table_name + " successfully into  table")
                cursor.close()

            except mysql.connector.Error as error:
                print("Failed to insert record into " + table_name + "table {}".format(error))

            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection to store data is closed")

if __name__ == "__main__":
    s = Store()
    s.get_movie_list_and_store_movie_details("movie_details", "movie_all_details")
