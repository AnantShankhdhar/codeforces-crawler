# codeforces-crawler
A website that recommends problems, virtual contests and shows user statistics for users of the coding platform codeforces.   
Link of the website: [CodeForces Crawler](http://cfcrawler.pythonanywhere.com/)

## Requirements
**[Django](https://www.djangoproject.com/)**  
**[Requests](https://pypi.org/project/requests/)**  
**[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)**  

## Installing requirements
Navigate to the directory and run  
### pip install -r requirements.txt

## Running the project
Navigate to the directory and run  
### python manage.py runserver --insecure

It has 3 parts:
- User statistics:   
It shows the following features for a single user-   
  - General information
  - Recommendation of Virtual contests
  - Recommendation of Problems for practise
  - Languages used
  - Level of questions (i.e. A,B,C) solved
  - Rating of questions solved
  - Submission Verdict
  - Rating and ranks in contests
  - Rating changes in contests
  - Solved count for a tag
  - Average rating for a solved tag
  - Submission heatmap
  - Accepted submission heatmap
- Comparison of two users   
It compares the following features for two users-   
  - General information
  - Languages used
  - Level of questions (i.e. A,B,C) solved
  - Rating of questions solved
  - Submission Verdict
  - Rating and ranks in contests
  - Solved count for a tag
  - Average rating for a solved tag
- Team rating   
It calculates team rating, rank and color for 1-4 users.

This project uses Django as its Web framework. Though Beautiful Soup was used initially for web scraping, Codeforces API was used later.

It has been developed by-
- Divyam Singal
- Manish Prajapati
- Anant Shankhdhar
