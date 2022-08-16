from src_code.Store_to_SQL import Store
import pandas as pd
import time

#df = pd.read_excel(r"D:\Naveen\Entertainer_PowerBi\Provided_Dataset\Entertainer - Basic Info.xlsx", engine="openpyxl", usecols=[0])
df = pd.read_csv(r"D:\Naveen\Entertainer_PowerBi\Populated_Data\Sandalwood_actors\sandalwood_actors_basics.csv", usecols=[0])

class Operator:

    def add_person_details(self):
        for i in range(len(df)):
            #ent_name = df.Entertainer[i]
            ent_name = df.Name[i]
            print("Start-->", ent_name)
            s = Store()
            s.insert_person_details_into_sql(ent_name, "entertainer_details", "sandalwood_entertainer_basics_details")
            print("Done-->", ent_name)

    def add_person_films(self):
        for i in range(len(df)):
            #ent_name = df.Entertainer[i]
            ent_name = df.Name[i]
            print("Start-->", ent_name)
            s = Store()
            s.insert_list_of_movies(ent_name, "entertainer_details", "sandalwood_entertainer_films")
            print("Done--->", ent_name)

    def add_person_awards(self):
        for i in range(len(df)):
            #ent_name = df.Entertainer[i]
            ent_name = df.Name[i]
            print("Start-->", ent_name)
            s = Store()
            s.insert_person_award_details(ent_name, "entertainer_details", "sandalwood_entertainer_awards")
            print("Done--->", ent_name)

    def add_salary_details(self):
        for i in range(len(df)):
            #ent_name = df.Entertainer[i]
            ent_name = df.Name[i]
            print("Start-->", ent_name)
            s = Store()
            s.insert_person_salary_details(ent_name, "entertainer_details", "sandalwood_entertainer_salary")
            print("Done--->", ent_name)

    def add_movie_details(self):
        s = Store()
        now = time.time()
        print("Starting the opertaion of adding movie details")
        s.get_movie_list_and_store_movie_details("movie_details", "kollywood_movie_all_details")
        print('Time taken to finish:', time.time()-now )

if __name__ == "__main__":
    op = Operator()
    op.add_person_details()
    op.add_person_films()
    op.add_person_awards()
    op.add_salary_details()
    op.add_movie_details()
