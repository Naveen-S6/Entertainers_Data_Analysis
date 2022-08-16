# Entertainers_Data_Analysis

### Objective 🎯

Analyzing details about the entertainers by populating data and creating a dashboard in PowerBi

### Dataset 📀

#### Provided data
  
  1. **Entertainer-Basic Info:** It consists of list of 70 Entertainers Name, Birth year and Gender 
  2. **Entertainer-Breakthrough Info:** It consists of details about the 70 entertainers like breakthrough year, first major award, breakthrough movie name 
  3. **Entertainer-Last major work Info:** It consists of the details about the 70 entertainers last major  work and if died, Year of death details

#### Data populating flow 

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/main/Documents/Populating_data_flow.png">

- To understand the design and flow of the code, I have explained the code design in this page [Code design](https://github.com/Naveen-S6/Entertainers_Data_Analysis/tree/main/src_code)
- The beauty of designing a code is, you can use them for other data as well, I have populated some extra data for Indian industry entertainers, which I didn't use it in this project. You can find the sql dump in this page [SQL dump](https://github.com/Naveen-S6/Entertainers_Data_Analysis/tree/main/Populated_Data/Indian%20Entertainers%20dataset)

#### Populated data

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

### Architecture

<img src="https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/79de0381eb3e30d2a6740a6b19692dc13b7bbfb2/Documents/Architecture.png">

for the detailed architecture explanation, you can refer this file - [Architecture](https://github.com/Naveen-S6/Entertainers_Data_Analysis/blob/79de0381eb3e30d2a6740a6b19692dc13b7bbfb2/Documents/PDFs/Architecture.pdf)


