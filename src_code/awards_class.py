from src_code.Movie_class import Movie_ob
from src_code.Person_class import PersonOb

class Awards:
    def get_award_name(self, per_award_obj):
        "This function will return the award name"

        if 'award' in per_award_obj.keys():
            return per_award_obj['award']

    def get_year(self, per_award_obj):
        "This function will return the award year"

        if "year" in per_award_obj.keys():
            return per_award_obj["year"]

    def get_prize(self, per_award_obj):
        "This function will return the prize details"

        if "prize" in per_award_obj.keys():
            return per_award_obj['prize']

    def get_category(self, per_award_obj):
        "This funcation will return the category of the award"

        if 'category' in per_award_obj.keys():
            return per_award_obj['category']

    def get_result(self, per_award_obj):
        "This function will return the result of the award wether winner or nominee"

        if 'result' in per_award_obj.keys():
            return per_award_obj['result']

    def get_award_movie_name(self, per_award_obj):
        "This function will return the movie name for which the award is given"

        if 'movies' in per_award_obj.keys():
            movie_obj = per_award_obj['movies']
            mo = Movie_ob()
            movie_name = mo.get_movie_name(movie_obj)
            return movie_name

    def get_shared_with(self, per_award_obj):
        "This funtion will return the person shared with details if any"

        if 'shared with' in per_award_obj.keys():
            per_obj = per_award_obj['shared with']
            po = PersonOb()
            person_name = po.get_person_name(per_obj)
            return person_name



