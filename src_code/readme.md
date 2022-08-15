## Code Functionality Flow

As a first step, to understand the IMDBpy library and other functionalities
I have written code in Jupyter notebook for each specific functionality and then designed the code
in OOPs concept. 

[Notebooks](https://github.com/Naveen-S6/Entertainers_Data_Analysis/tree/main/Notebooks)

---
## List of classes

- Person
- PersonOb
- Movie
- Movie_ob
- Salary
- Awards
- Store
- Operator

---
## Person_class Python File

It contains of two classes, Person and PersonOb

### Person

This class takes a input parameter Name of the entertainer while creating the class.
It is used to search the entertainer name in IMDB database and return the ID and person object.

### PersonOb

This class takes no input, and it is used to extract the details of the person from person Object file.
Methods in this class takes the Person object as input while calling the methods.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/Person_class.py)


## Movie_class Python File

### Movie

This class takes a input parameter Name of the movie while creating the class.
It is used to search the movie name in IMDB database and return the ID and movie object.


### Movie_ob

This class takes no input, and it is used to extract the details of the movie from movie Object file.
Methods in this class takes the Movie object as input while calling the methods.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/Movie_class.py)


## Salary_class Python File

This class takes a input of person salary dictionary object which is extracted from person object file.
I have regex pattern matching to extract the movie_name, year and salary of the entertainer for that particular movie.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/salary_class.py)


## Awards_class Python File

This class takes input of person awards dictionary object which is extracted from person object file.
Methods of this class is used to extract the specific details of the awards.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/awards_class.py)


## Store_to_SQL Python File.

This class is used to make connection to SQL and store the extracted details of the entertainers and movies to the local database.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/Store_to_SQL.py)


## Operator Python File

This class is used to combine all the classes and execute the code for the given entertainers and movies.

[Code](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/src/operator.py)

---


