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
array = re.split('(\n)', to_print)
player_array = []
new_array = []
for item in array:
    player_array.append(item)
    if len(player_array) == 80:
        player_array = filter(lambda x: x != '\n', player_array)
        new_array.append(player_array)
        player_array = []

# print(new_array[4])
# print(len(new_array))
# print(new_array)
list_of_players = []
for item in new_array:
    list_of_players.append(Player(item[0], team = item[2], bye = item[3], passing_yrd = item[20], passing_td = item[21], passing_int = item[22], rushing_att = item[25], rushing_yrd = item[27], rushing_td = item[27], receiving_trg = item[29], receiving_rec = item[30], receiving_yrd = item[31], receiving_td = item[32], misc_2pt = item[36], fum_lost = item[38], games_played = item[16], games_started = item[17]))

    # (tack_solo = item[], tack_ast = item[], sack = item[], safety = item[], pass_deff = item[], blk_kick = item[], turnover_int = item[], fum_force = item[], fum_recover = item[], defensive_td = item[], fgm_0_19 = item[], fgm_20_29 = item[], fgm_30_39 = item[], fgm_40_49 = item[], fgm_50 = item[], pat = item[],  return_yrd = item[], return_td = item[], age = item[]) items not tracked yet


print(list_of_players[1].team)
print(list_of_players[1].name)
print(list_of_players[1].bye)
print(list_of_players[4].name + " " + list_of_players[4].team + " " + list_of_players[4].rushing_att)



# matt = Player("matt", age=32)
# print(matt.name)


# from pyth.plugins.rtf15.reader import Rtf15Reader
# from pyth.plugins.plaintext.writer import PlaintextWriter
#
# doc = Rtf15Reader.read(open('football_stats.txt'))
#
# print PlaintextWriter.write(doc).getvalue()
