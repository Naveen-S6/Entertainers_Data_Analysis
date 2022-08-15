import imdb
mi = imdb.Cinemagoer()
from Person_class import PersonOb

class Movie:
    def __init__(self, name):
        self.name = name

    def get_list_of_matching_movies(self):
        '''This function will search the given movie name in the IMDB database and
        the return the matching movies list'''
        try:
            movies = mi.search_movie(self.name)
            return movies
        except:
            return []


    def get_movie_id(self):
        "This function will return the ID of the Movie"
        movies = self.get_list_of_matching_movies()
        leen = len(movies)
        if leen:
            for i in range(leen):
                m_id = movies[i].movieID
                movi = mi.get_movie(m_id)
                if "title" in movi.keys():
                    if movi["title"] == self.name:
                        return m_id

    def get_movie_obj(self):
        "This function will return the dictionary object file of the movie"
        mo_id = self.get_movie_id()
        try:
            movie_dict = mi.get_movie(mo_id)
        except :
            movies_list = self.get_list_of_matching_movies()
            if len(movies_list):
                movie_dict = movies_list[0]
            else:
                movie_dict = None
        return movie_dict

class Movie_ob:

    def get_movie_name(self, movie_obj):
        "This function will return the movie name"
        if movie_obj:
            keys = movie_obj.keys()
            if 'title' in keys:
                return movie_obj['title']
            elif 'original title' in keys:
                return movie_obj['original title']
            elif 'canonical title' in keys:
                return movie_obj['canonical title']
            elif 'long imdb title' in keys:
                return movie_obj['long imdb title']
            elif 'smart canonical title' in keys:
                return movie_obj['smart canonical title']


    def get_movie_cover_url(self, movie_obj):
        "This function will return the cover URL of the movie from given movie object"
        if movie_obj:
            keys = movie_obj.keys()
            if 'full-size cover url' in keys:
                return movie_obj['full-size cover url']
            elif 'cover url' in keys:
                return movie_obj['cover url']
            else:
                return None

    def get_movie_year_of_release(self, movie_obj):
        "This function  will return the year of release of the given movie"
        if movie_obj:
            if "year" in movie_obj.keys():
                return movie_obj["year"]

    def get_movie_genres(self, movie_obj):
        "This function will return the genres of the given movie object"
        if movie_obj:
            if 'genres' in movie_obj.keys():
                gen = movie_obj['genres']
                if len(gen):
                    return ", ".join(gen)

    def get_movie_languages(self, movie_obj):
        "This function will return the languages of the movie"
        if movie_obj:
            if 'languages' in movie_obj.keys():
                lan = movie_obj['languages']
                if len(lan):
                    return ", ".join(lan)

    def get_movie_directors_name(self, movie_obj):
        "This function will return the director names of the movie from the given movie object"
        if movie_obj:
            if "director" in movie_obj.keys():
                persons_id = movie_obj["director"]
                director_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        director_names.append(name)

                if len(director_names):
                    return ", ".join(director_names)

    def get_movie_writers_name(self, movie_obj):
        "This function will return the writer names of the movie from the given movie object"

        if movie_obj:
            if 'writer' in movie_obj.keys():
                persons_id = movie_obj['writer']
                writer_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        writer_names.append(name)

                if len(writer_names):
                    return ", ".join(writer_names)

    def get_movie_producers_name(self, movie_obj):
        "This function will return the producers names of the movie from the given movie object"

        if movie_obj:
            if 'producer' in movie_obj.keys():
                persons_id = movie_obj['producer']
                producer_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        producer_names.append(name)

                if len(producer_names):
                    return ", ".join(producer_names)

    def get_movie_composers_name(self, movie_obj):
        "This function will return the composers names of the movie from the given movie object"

        if movie_obj:
            if 'composer' in movie_obj.keys():
                persons_id = movie_obj['composer']
                composer_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        composer_names.append(name)

                if len(composer_names):
                    return ", ".join(composer_names)

    def get_movie_cinematographers_name(self, movie_obj):
        "This function will return the cinematographer names of the movie from the given movie object"

        if movie_obj:
            if 'cinematographer' in movie_obj.keys():
                persons_id = movie_obj['cinematographer']
                cinematographer_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        cinematographer_names.append(name)

                if len(cinematographer_names):
                    return ", ".join(cinematographer_names)

    def get_movie_editors_name(self, movie_obj):
        "This function will return the editor names of the movie from the given movie object"

        if movie_obj:
            if 'editor' in movie_obj.keys():
                persons_id = movie_obj['editor']
                editor_names = []
                pp = PersonOb()
                for i in range(len(persons_id)):
                    name = pp.get_person_name(persons_id[i])
                    if name:
                        editor_names.append(name)

                if len(editor_names):
                    return ", ".join(editor_names)

    def get_movie_runtime(self, movie_obj):
        "This function will return the runtime of the movie"
        if movie_obj:
            if "runtimes" in movie_obj.keys():
                return movie_obj["runtimes"][0]

    def get_movie_plot(self, movie_obj):
        "This function will return the movie plot"
        if movie_obj:
            keys = movie_obj.keys()
            if 'plot outline' in keys:
                return movie_obj["plot outline"]

            elif "plot" in keys:
                return ", ".join(movie_obj["plot"])

    def get_movie_rating(self, movie_obj):
        "This function will returun the rating of the movie form the given movie object"

        if movie_obj:
            if "rating" in movie_obj.keys():
                return movie_obj["rating"]


if __name__ == "__main__":
    mo = Movie("Because of You")
    mo_obj = mo.get_movie_obj()
    cp = Movie_ob()
    print("Cover URL",cp.get_movie_cover_url(mo_obj))
    print("Movie rating:", type(cp.get_movie_rating(mo_obj)))
    print("Runtime:", cp.get_movie_runtime(mo_obj))
    print("Plot:", cp.get_movie_plot(mo_obj))
    print("Year of release:", cp.get_movie_year_of_release(mo_obj))
    print("Languages released:", cp.get_movie_languages(mo_obj))
    print("Genres:", cp.get_movie_genres(mo_obj))
    print("Director Name:", cp.get_movie_directors_name(mo_obj))
    print("Writer names:", cp.get_movie_writers_name(mo_obj))
    print("Producer names:", cp.get_movie_producers_name(mo_obj))
    print("Editor names", cp.get_movie_editors_name(mo_obj))
    print("Cinematographer names:", cp.get_movie_cinematographers_name(mo_obj))
    print("Composer names:", cp.get_movie_composers_name(mo_obj))





