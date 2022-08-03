import imdb
import random
mi = imdb.Cinemagoer()
class Person:
    def __init__(self, name):
        self.name = name

    def get_list_of_matching_names(self):
        '''This function will search the given person name in the IMDB database and
        the return the matching persons list'''
        persons = mi.search_person(self.name)
        return persons

    def get_person_id(self):
        "This function will return person ID from given person object"
        persons = self.get_list_of_matching_names()
        if len(persons):
            return persons[0].personID

    def get_person_dic_obj(self):
        '''This function will get the person details object for the given person ID,
        if there is some issue in fetuching the person, it will return the object which has
        basic details of the person'''
        p_id = self.get_person_id()
        try:
            person_dict = mi.get_person(p_id)
        except:
            person_dict = self.get_list_of_matching_names()[0]

        return person_dict

    def get_person_award_dic_obj(self):
        "This function will return the dictionary object of person's awards and other details"
        a_id = self.get_person_id()
        try:
            person_award_dict = mi.get_person_awards(a_id)
        except:
            person_award_dict = self.get_list_of_matching_names()[0]

        return person_award_dict

class PersonOb:

    def get_person_name(self, person_dict):
        "This function will return the person name from the given object"
        if 'name' in person_dict.keys():
            return person_dict['name']

    def get_headshot_url(self, person_dict):
        "This function will get the headshot url from the given person object"
        keys = person_dict.keys()

        # Picture of the person
        if "full-size headshot" in keys:
            return person_dict["full-size headshot"]
        elif "headshot" in keys:
            return person_dict["headshot"]
        else:
            return None

    def get_person_height(self, person_dict):
        "This function will return the person height from the person object dic"
        # height
        if "height" in person_dict.keys():
            return person_dict["height"]

    def get_person_nicknames(self, person_dict):
        "This function will return the person's nicknames if any from the given person object dict"

        if 'nick names' in person_dict.keys():
            nick = person_dict['nick names']
            return ", ".join(nick)

    def get_person_dob(self, person_dict):
        "This function will return the DOB of the person from given person Object dict"

        if 'birth date' in person_dict.keys():
            return person_dict['birth date']

    def get_person_quote(self, person_dict):
        "This function will return the random quotes of the given person"

        if 'quotes' in person_dict.keys():
            quotes = person_dict['quotes']
            ran_ind = random.randint(0, len(quotes)-1)
            return quotes[ran_ind]

    def get_person_trade_mark(self, person_dict):
        "This function will return the trade marks of the given person if any"

        if 'trade mark' in person_dict.keys():
            trade = person_dict['trade mark']
            return ", ".join(trade)

    def get_person_mini_biography(self, person_dict):
        "This function will return the Mini biography of the person if it is available in the database"

        if "mini biography" in person_dict.keys():
            return person_dict["mini biography"][0]

    def get_list_of_films(self, person_dict):
        "This function will return the 'list' of movie objects acted by the given person"

        if 'filmography' in person_dict.keys():
            keys = person_dict["filmography"]
            if "actor" in keys:
                return person_dict["filmography"]["actor"]
            elif "actress" in keys:
                return person_dict["filmography"]["actress"]

    def get_person_salary_history(self, person_dict):
        "This function will return 'list' of the history of salary list from the database if any data is present"

        if 'salary history' in person_dict.keys():
            return person_dict['salary history']

    def get_person_award_list(self, person_award_dict):
        "This function will return a list of all awards of the person"
        if "data" in person_award_dict.keys():
            if "awards" in person_award_dict["data"].keys():
                return person_award_dict["data"]["awards"]

if __name__ == "__main__":
    pe = Person('Aretha Franklin')
    per_obj = pe.get_person_dic_obj()
    p = PersonOb()
    print("Headshot URL:", len(p.get_headshot_url(per_obj)))
    print("Height:", len(p.get_person_height(per_obj)))
    print("nicknames:", len(p.get_person_nicknames(per_obj)))
    print("DOB:", type(p.get_person_dob(per_obj)),p.get_person_dob(per_obj))
    print("quote:", len(p.get_person_quote(per_obj)))
    print("trade mark:", len(p.get_person_trade_mark(per_obj)))
    print("Mini Biography:", len(p.get_person_mini_biography(per_obj)))