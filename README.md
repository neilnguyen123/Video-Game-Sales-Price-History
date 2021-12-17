# Video-Game-Sales-Price-History

In order, how the files should be opened:
  1. Pre-Data Prep: Video Game Sales Price History Data Prep_PUBLIC.ipynb
      > Prep work in order to define parameters for the data gathering process
  2. Data Gathering: isthereanydeal_spider.py, items.py, middlewares.py, pipelines.py, settings.py
      > To run this, open the console and type in 'scrapy isthereanydeal_spider -o items.csv'
  3. Data Analysis: Video Game Sales Price History Analysis.ipynb
      > Data prep for modeling


Obtained top 500 games to scape through
<img width="585" alt="Screen Shot 2021-12-12 at 11 27 20 AM" src="https://user-images.githubusercontent.com/85441922/145722801-dfaf421e-5126-4d7e-82a8-445611a03007.png">

Results from the scraping
<img width="910" alt="Screen Shot 2021-12-12 at 6 34 13 PM" src="https://user-images.githubusercontent.com/85441922/145736221-35639b0a-22ad-4471-b77d-c28bb2b60677.png">

Applied functions to have dataframe ready for time-series forecasting

 
