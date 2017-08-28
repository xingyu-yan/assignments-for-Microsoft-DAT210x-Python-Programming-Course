import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]
#print(df)
# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
#GP: Games Played
#G: Goals
#A: Assists
#PTS: Points
#+/-: Plus/Minus Rating
#PIM: Penalty Minutes
#PTS/G: Points Per Game
#SOG: Shots on Goal
#PCT: Shooting Percentage
#GWG: Game-Winning Goals
#G: Power-Play Goals
#A: Power-Play Assists
#G: Short-Handed Goals
#A: Short-Handed Assists

df.columns = ['RK','PLAYER','TEAM','Games_Played','Goals','Assists','Points',
              'Plus_Minus_Rating','Penalty_Minutes','Points_Per_Game',
              'Shots_on_Goal','Shooting_Percentage','Game_Winning_Goals',
              'Power_Play_Goals','Power_Play_Assists','Short_Handed_Goals',
              'Short_Handed_Assists'] 

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)
df = df.reset_index(drop=True)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
#print(df)

df = df.drop_duplicates(subset=['PLAYER'])
df = df.drop(labels=[0], axis=0)
df = df.reset_index(drop=True)
#print(df)

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'], axis=1)
df = df.reset_index(drop=True)
#print(df)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df.fillna(0)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
df.dtypes

df.Goals = pd.to_numeric(df.Goals, errors='coerce')
df.Assists = pd.to_numeric(df.Assists, errors='coerce')
df.Points = pd.to_numeric(df.Points, errors='coerce')
df.Plus_Minus_Rating = pd.to_numeric(df.Plus_Minus_Rating, errors='coerce')
df.Penalty_Minutes = pd.to_numeric(df.Penalty_Minutes, errors='coerce')
df.Points_Per_Game = pd.to_numeric(df.Points_Per_Game, errors='coerce')
df.Shots_on_Goal = pd.to_numeric(df.Shots_on_Goal, errors='coerce')
df.Shooting_Percentage = pd.to_numeric(df.Shooting_Percentage, errors='coerce')
df.Game_Winning_Goals = pd.to_numeric(df.Game_Winning_Goals, errors='coerce')
df.Power_Play_Goals = pd.to_numeric(df.Power_Play_Goals, errors='coerce')
df.Power_Play_Assists = pd.to_numeric(df.Power_Play_Assists, errors='coerce')
df.Short_Handed_Goals = pd.to_numeric(df.Short_Handed_Goals, errors='coerce')
df.Short_Handed_Assists = pd.to_numeric(df.Short_Handed_Assists, errors='coerce')

print(df.dtypes)

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
unique_PCT = df.Shooting_Percentage.unique()
len(unique_PCT)
