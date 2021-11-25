#!/usr/bin/env python
# coding: utf-8

# As a young millenial with many wants and needs, it is important that I can manage my personal finances. I love playing video games as a past time with friends and by myself. Video games cost money. I need to be able to anticipate the next video game sale, so my friends and I can better adjust our finances to purchase a video game on its next sale. 
# 
# This model pulls from IsThereAnyDeal.com. This website aggregates deals on a video game from multiple websites, excluding third party gray market resellers. 

# In[1]:


# scrape website for historical prices of all video games
# put dataset into pondas or a database
# clean dataset


# Let's try pulling data on Popularity and Collection info on all games using the API. These can be possible predictors on discounts. This may also provide a list of all games on IsThereAnyDeal.com
# 
# From the API documentation (https://itad.docs.apiary.io/):
# - Collection: Games sorted from most collected to least collected
# - Popularity: Game sorted from most popular to least popular, where popularity is computed as normalized count in Waitlist + normalized count in Collection, and rank is set based on the position in sorted list

# In[2]:


import requests
import pandas as pd


# In[3]:

KEY = '154e245bb12710b94af87ac253b17bcc99c6c86b'
OFFSET = '0'
LIMIT = '500'


URL_3 = 'https://api.isthereanydeal.com/v01/web/stores/all/'
r3 = requests.get(URL_3)
r3_json = r3.json()
print(f"There are {len(r3_json['data'])} covered shops")

stores_id = [r3['id'] for r3 in r3_json['data']]
stores_title = [r3['title'] for r3 in r3_json['data']]

# Initialize dataset with the created lists
data = {
    'stores_id': stores_id,
    'stores_title': stores_title
}

# Create DataFrame
df = pd.DataFrame(data)
# Check for duplicates
print(f"There are {df.duplicated().sum()} duplicate rows.")


# The API is unable to pull the remaining 17 shops (only 73% covered). This may be an issue but for now let's move forward with looping the 45 shops to get all the games.

game_list = []
for shop in stores_id:
    URL_4 = f'https://api.isthereanydeal.com/v01/game/plain/list/?key={KEY}&shops={shop}'
    r4 = requests.get(URL_4)
    game_list.append(r4.json())
game_list


# This is list of all games for the 45 shops. Games are listed by their plain titles (no spaces and all lower cases). Let's put this into a dataframe and remove duplicates.

# I'm checking out the JSON structure, so I can parse the game titles. Looks like I will have to run several iterations to parse the names.
game_name_list = []

for game_json in game_list:
    for game_json_1 in game_json['data'].values():
        for game in game_json_1.values():
            game_name_list.append(game)

# There may be some duplicate titles, so let's load all the titles into a dataframe and remove duplicates.
data = {
    'game_name': game_name_list
}

def game_names_list():
    df_game_names = pd.DataFrame(data)
    # Remove duplicate titles and return cleaned dataframe
    df_game_names.drop_duplicates(inplace=True)
    return df_game_names