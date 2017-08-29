import re
import urllib2
from bs4 import BeautifulSoup
from player_object import Player



# # rename the files using python!!
# import os
#
# positions = ["QB", "RB", "WR", "TE"]
# years = ["2014", "2015", "2016"]
#
# for position in positions:
#     for year in years:
#         os.rename("NFL {0} {1}.rtf".format(position, year), "{0}_season_{1}.txt".format(position, year))



# QB_season_2014 = open("QB_season_2014.txt")
# QB_season_2015 = open("QB_season_2015.txt")
# QB_season_2016 = open("QB_season_2016.txt")
#
# QB_2014_data = QB_season_2014.read()
# QB_season_2014.close()
#
# QB_2015_data = QB_season_2015.read()
# QB_season_2015.close()
#
# QB_2016_data = QB_season_2016.read()
# QB_season_2016.close()
#
# print(QB_2016_data)

data = open("football_stats.txt")
to_print = data.read()
data.close()
# print(re.split('(\W)', to_print))
array = []
array = re.split('(\W)', to_print)
player_array = []
new_array = []
for item in array:
    player_array.append(item)
    if len(player_array) == 80:
        new_array.append(player_array)
        player_array = []

# print(new_array[3])
print(len(array))
# for i, j in enumerate(array):
#     if i%80==0:
#         print(j)


# matt = Player("matt", age=32)
# print(matt.name)


# from pyth.plugins.rtf15.reader import Rtf15Reader
# from pyth.plugins.plaintext.writer import PlaintextWriter
#
# doc = Rtf15Reader.read(open('football_stats.txt'))
#
# print PlaintextWriter.write(doc).getvalue()
