import re
class Salary:

    def get_salary_movie_name(self, person_salary_item):
        movie_name_pattern = '^(.*)\(\d'
        movie_name_match = re.findall(movie_name_pattern, person_salary_item)
        if movie_name_match:
            return movie_name_match[0]

    def get_salary_movie_year(self, person_salary_item):
        year_pattern = '\((\d{4})\)'
        year_match = re.findall(year_pattern, person_salary_item)
        if year_match:
            return year_match[0]

    def get_salary_amount(self, person_salary_item):
        first_salary_pattern = '\$([0-9,;]+\ *\.\d*)'
        second_salary_pattern = '\$([0-9,;]+)'
        first_salary_match = re.findall(first_salary_pattern, person_salary_item)

        if first_salary_match:
            if "," and "." not in first_salary_match[0]:
                if "." in first_salary_match[0]:
                    s_d = first_salary_match[0].split(".")
                    salary_str = ""
                    for i in range(len(s_d)):
                        salary_str += s_d[i].strip()
                    salary = int(salary_str)
                    return salary
                else:
                    salary = int(first_salary_match[0].strip())
                    return salary
            else:
                s_d = first_salary_match[0].split(".")
                new_s_d = s_d[0].split(",")
                salary_str = ""
                for i in range(len(new_s_d)):
                    salary_str += new_s_d[i].strip()
                salary = int(salary_str)
                return salary

        else:
            second_salary_match = re.findall(second_salary_pattern, person_salary_item)
            if second_salary_match:
                if "," in second_salary_match[0]:
                    s_d = second_salary_match[0].split(",")
                    salary_str = ""
                    for i in range(len(s_d)):
                        salary_str += s_d[i].strip()
                    salary = int(salary_str)
                    return salary
                else:
                    salary = int(second_salary_match[0].strip())
                    return salary

if __name__ == "__main__":
    s = Salary()
    print(s.get_salary_amount('The Bride Wore Red (1937)::$9,500 .00 per week'))