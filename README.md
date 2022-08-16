# Entertainers Data Analysis - iNeuron Internship

[PowerBi Report Link](https://www.novypro.com/project/entertainers-data-analysis)

## Project overview 👀

I have done this project as part of the iNeuron Internship. If you are looking for some remote internship opportunity you can check out [iNeuron Internship portal](https://internship.ineuron.ai/), 
where you can find internship for different technologies in different domains.


## Objective 🎯

Analyzing details about the entertainers by populating data and creating a dashboard in PowerBi

## Problem statement ❓

Normal life can be stressful, and people need to relax. Being entertained by others is a wonderful way to take some time out of life. It can reduce stress and make life's issues easier to face. The media and entertainment industry consists of film, television, radio and print. These segments include movies, TV shows, radio shows, news, music, newspapers, magazines, and books. Entertainment industry is a group of sub-industries devoted to entertainment. Entertainment industry is used to describe the mass media companies that control the distribution and manufacture of mass media entertainment.

## Dataset 📀

### Provided data
  
  1. **Entertainer-Basic Info:** It consists of list of 70 Entertainers Name, Birth year and Gender 
  2. **Entertainer-Breakthrough Info:** It consists of details about the 70 entertainers like breakthrough year, first major award, breakthrough movie name 
  3. **Entertainer-Last major work Info:** It consists of the details about the 70 entertainers last major  work and if died, Year of death details

### Data populating flow 

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/Documents/Populating_data_flow.png">

- You can refer this page to understand the design and flow of the code - [Code design](https://github.com/Naveen-S6/Entertainers_Data_Analysis/tree/main/src_code)
- The beauty of designing a code is, you can use them for other data as well, I have populated some extra data for Indian industry entertainers, which I didn't use it in this project. You can find the sql dump in this page [SQL dump](https://github.com/Naveen-S6/Entertainers_Data_Analysis/tree/main/Populated_Data/Indian%20Entertainers%20dataset)

### Populated data

  1. **Entertainers_basics_populated:**
     - Name: Entertainer’s name 
     - DOB: Date of birth of the Entertainer 
     - Height: Height of the entertainer 
     - Nicknames: Nicknames of the entertainers, that is used by fans or cinema industry 
     - Quotes: Entertainers quote or statements they made in public 
     - Mini-biography: Mini biography of the entertainer 
     - Trademark: Trademark style or behaviour of the entertainer 
     - Headshot: URL of the entertainers headshot
  2. **Entertainers_film_list:**
     - Entertainer name: Name of the entertainer 
     - Movie name: Movie name which the entertainer acted 
     - Year: Release year of the movie
  3. Entertainers_awards:
     - Name: Entertainer’s name 
     - Award: Award name 
     - Year: Year of the award 
     - Prize: Type of award 
     - Category: Under which category the award has been given 
     - Result: Whether entertainer won the award or just a Nominee (Winner/Nominee)
     - Movie_name: For which movie the award was given 
     - Shared_with: with they shared the award with someone, there name
  4. Entertainer_salary:
     - Name: Entertainer’s name 
     - Movie_name: Movie name of the salary they received 
     - Year: Movie released year 
     - Salary: Amount they received for that movie

## Architecture 🪵

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/79de0381eb3e30d2a6740a6b19692dc13b7bbfb2/Documents/Architecture.png">

for the detailed architecture explanation, you can refer this file - [Architecture](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/79de0381eb3e30d2a6740a6b19692dc13b7bbfb2/Documents/PDFs/Architecture.pdf)

## Report 📈

#### Live report - [Link](https://www.novypro.com/project/entertainers-data-analysis)

### Homepage 

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/51b341efba1dfe4b1c5aff99ab04bd43a6c958ad/Documents/home_page.png">


### Entertainer Page

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/51b341efba1dfe4b1c5aff99ab04bd43a6c958ad/Documents/Entertainer_analysis_page.png">

### Movie Analysis Page

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/51b341efba1dfe4b1c5aff99ab04bd43a6c958ad/Documents/movie_analysis_page.png">


## Few Insights from the Report: 💡

- Meryl Streep is the entertainer who received the highest number of awards among other
entertainers 
- Top 6 entertainers who received most of the awards 
  - Meryl Streep 
  - Lady Gaga 
  - Leonardo DiCaprio 
  - Mariah Carey 
  - Justin Timberlake 
  - Will Smith
- James Dean has the highest average rating of movies among others 
- Highest number of movies (55) released till date was on 1998 
- Highest average rating of movies was on 1949 
- Donald Sutherland acted in the highest number of movies till date, which was 198 movies

---

- As it is a entertainer’s analysis project, based on the end user need they can consume a lot of insights from the dashboard.
- For the filtering purpose based on the end user need, in entertainers analysis page, there is a drop down filter to select the particular entertainer.
- In Movie analysis page, Included several filters like rating and year, so the 
end user can filter the data according to their interest

---