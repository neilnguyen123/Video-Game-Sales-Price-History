# Video-Game-Sales-Price-History

In order, how the files should be opened:
  1. Pre-Data Prep: Video Game Sales Price History Data Prep_PUBLIC.ipynb
      > Prep work in order to define parameters for the data gathering process
  2. Data Gathering: isthereanydeal_spider.py, items.py, middlewares.py, pipelines.py, settings.py
      > To run this, open the console and type in 'scrapy isthereanydeal_spider -o items.csv'
  3. Data Analysis: Video Game Sales Price History Analysis.ipynb
      > Data prep for modeling


**Problem:** 

As a young millenial with many wants and needs, it is important that I can manage my personal finances. I love playing video games as a past time with friends and by myself. Video games cost money. I need to be able to anticipate the next video game sale, so my friends and I can better adjust our finances to purchase a video game on its next sale. 

**Goal:** 

The goal of this project is to predict the next sales price on a video game.

# 1. Define Parameters
Determined the top 500 popular games using the API to scrape data on

<img width="585" alt="Screen Shot 2021-12-12 at 11 27 20 AM" src="https://user-images.githubusercontent.com/85441922/145722801-dfaf421e-5126-4d7e-82a8-445611a03007.png">

# 2. Gather data
Scraper was built using Scrapy. Details on code can be found on isthereanydeal_spider.py. Used the built scraper to scrape price data and other relevant information on game 

<img width="911" alt="Screen Shot 2021-12-18 at 10 12 22 PM" src="https://user-images.githubusercontent.com/85441922/146663579-72cea31a-cf44-4867-8100-365ae773c1d1.png">

# 3. Clean data
Perform data cleaning and transformation to prep for model development

<img width="1007" alt="Screen Shot 2021-12-18 at 10 14 45 PM" src="https://user-images.githubusercontent.com/85441922/146663617-b3204245-e76b-4b3f-a927-51f102b7d9d4.png">

# 4. Analyze data

<img width="613" alt="Screen Shot 2021-12-18 at 10 16 53 PM" src="https://user-images.githubusercontent.com/85441922/146663677-f45a2ac3-d913-4b81-b2af-a96353f4d919.png">

<img width="934" alt="Screen Shot 2021-12-18 at 10 18 29 PM" src="https://user-images.githubusercontent.com/85441922/146663704-2365cf31-f9ec-41fc-b9eb-f4556335e5b6.png">

<img width="911" alt="Screen Shot 2021-12-18 at 10 17 22 PM" src="https://user-images.githubusercontent.com/85441922/146663686-f7298850-a962-478d-ad68-f5d36fa1e63a.png">

# 5. Apply prediction model
Used logistics regression to determine if there will be sales on a game at a particular store over the next 30 days. This is a sample output of the confusion matrix using training and test

<img width="580" alt="Screen Shot 2021-12-18 at 10 19 36 PM" src="https://user-images.githubusercontent.com/85441922/146663732-d77248f3-3656-4430-88b1-0c617374f625.png">

# 6. Deploy model
View model deployed in Flask: https://github.com/neilnguyen123/isthereanydeal_flask
 
