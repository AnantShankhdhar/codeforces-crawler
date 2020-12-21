# codeforces-crawler
A website that recommends problems, virtual contests and shows user statistics for users of the coding platform codeforces.

It has 3 parts:
- User statistics:   
It shows the following features for a single user-   
  - General information
  - Recommendation of Virtual contests
  - Recommendation of Problems for practise
  - Languages used
  - Level of questions(i.e. A,B,C) solved
  - Rating of questions solved
  - Submission Verdict
  - Rating and ranks in contests
  - Rating changes in contests
  - Solved count for a tag
  - Average rating for a solved tag
  - Submission heatmap
  - Accepted submission heatmap
- Comparison of two users   
It compares the following featuures for two users-   
  - General information
  - Languages used
  - Level of questions(i.e. A,B,C) solved
  - Rating of questions solved
  - Submission Verdict
  - Rating and ranks in contests
  - Solved count for a tag
  - Average rating for a solved tag
- Team rating   
It calculates team rating, rank and color for 1-4 users.

This project uses Django as its Web framework. Though Beautiful Soup was used initially for web scraping, Codeforces API was used a lot later.

It has been developed by-
- Divyam Singal
- Manish Prajapati
- Anant Shankhdhar
