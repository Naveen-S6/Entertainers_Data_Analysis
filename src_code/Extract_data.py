from src_code.Person_class import Person
from src_code.Person_class import PersonOb
from src_code.Movie_class import Movie
from src_code.Movie_class import Movie_ob

class Entertainer:
    def __init__(self, name):
        self.name = name

    def get_person_details(self):
        p = Person(self.name)
        p_obj = p.get_person_dic_obj()
        po = PersonOb()

        dob = po.get_person_dob(p_obj)
        height = po.get_person_height(p_obj)
        nicknames = po.get_person_nicknames(p_obj)
        quotes = po.get_person_quote(p_obj)
        mini_biography = po.get_person_mini_biography(p_obj)
        trade_mark = po.get_person_trade_mark(p_obj)
        headshot = po.get_headshot_url(p_obj)

        out = (self.name, dob, height, nicknames, quotes, mini_biography, trade_mark, headshot)
        return out

    def get_person_movie_list(self):
        p = Person(self.name)
        p_obj = p.get_person_dic_obj()
        po = PersonOb()
        movies_list = po.get_list_of_films(p_obj)

        return movies_list

    def get_person_awards(self):
        p = Person(self.name)
        p_award_obj = p.get_person_award_dic_obj()
        po = PersonOb()
        awards_list = po.get_person_award_list(p_award_obj)

        return awards_list

    def get_person_salary_list(self):
        p = Person(self.name)
        p_obj = p.get_person_dic_obj()
        po = PersonOb()
        salary_list = po.get_person_salary_history(p_obj)

        return salary_list

    def get_movie_details(self):
        m = Movie(self.name)
        m_obj = m.get_movie_obj()
        mo = Movie_ob()

        rating = mo.get_movie_rating(m_obj)
        plot = mo.get_movie_plot(m_obj)
        runtime = mo.get_movie_runtime(m_obj)
        cover_url = mo.get_movie_cover_url(m_obj)
        year = mo.get_movie_year_of_release(m_obj)
        genres = mo.get_movie_genres(m_obj)
        languages = mo.get_movie_languages(m_obj)
        directors = mo.get_movie_directors_name(m_obj)
        writers = mo.get_movie_writers_name(m_obj)
        producers = mo.get_movie_producers_name(m_obj)
        composers = mo.get_movie_composers_name(m_obj)
        cinematographers = mo.get_movie_cinematographers_name(m_obj)
        editors = mo.get_movie_editors_name(m_obj)

        out = (self.name, rating, plot, runtime, cover_url, year, genres, languages, directors, writers, producers, composers, cinematographers, editors)

        return out

if __name__ == "__main__":
    e = Entertainer("Entourage")
    p = e.get_movie_details()
    print(p)







