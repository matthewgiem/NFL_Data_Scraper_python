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
list_of_players = []
for item in new_array:
    list_of_players.append(Player(item[0], team = item[2], position = item[1], bye = item[3], passing_yrd = item[20], passing_td = item[21], passing_int = item[22], rushing_att = item[25], rushing_yrd = item[26], rushing_td = item[27], receiving_trg = item[29], receiving_rec = item[30], receiving_yrd = item[31], receiving_td = item[32], misc_2pt = item[36], fum_lost = item[38], games_played = item[16], games_started = item[17]))


# order the players based on how much they are expected to produce

for player in list_of_players:
    player.expected_points = float(player.passing_yrd)/25 + float(player.passing_td)*6 + float(player.passing_int)*(-1) + float(player.rushing_yrd)/10 + float(player.rushing_td)*6 + float(player.receiving_yrd)/13 + float(player.receiving_td)*6 + float(player.misc_2pt)*2 + float(player.fum_lost)*(-2)

list_of_players.sort(key=lambda x: x.expected_points, reverse=True)

for player in list_of_players:
    print("{} is expected to get {} points".format(player.name, player.expected_points))


# print("name " + list_of_players[29].name + " plays the position {}".format(list_of_players[29].position))
# print("bye week for the {} is {} ".format(list_of_players[29].team, list_of_players[29].bye))
# print("passing yards = " + list_of_players[29].passing_yrd)
# print("passing touchdowns = " + list_of_players[29].passing_td)
# print("passing interceptions = " + list_of_players[29].passing_int)
# print("rushing touchdowns = " + list_of_players[29].rushing_td)
# print("rushing yards = " + list_of_players[29].rushing_yrd)
# print("receptions = " + list_of_players[29].receiving_rec)
# print("recieving touchdowns = " + list_of_players[29].receiving_td)
# print("recieving yards = " + list_of_players[29].receiving_yrd)
# print("2pt conversions = " + list_of_players[29].misc_2pt)
# print("fumbles lost = " + list_of_players[29].fum_lost)
# print("games played = " + list_of_players[29].games_played)
# print("games started = " + list_of_players[29].games_started)
#
# print("expected points = " + str(list_of_players[29].expected_points))


    # (tack_solo = item[], tack_ast = item[], sack = item[], safety = item[], pass_deff = item[], blk_kick = item[], turnover_int = item[], fum_force = item[], fum_recover = item[], defensive_td = item[], fgm_0_19 = item[], fgm_20_29 = item[], fgm_30_39 = item[], fgm_40_49 = item[], fgm_50 = item[], pat = item[],  return_yrd = item[], return_td = item[], age = item[]) items not tracked yet

# test to see if it works

# print(list_of_players[1].team)
# print(list_of_players[1].name)
# print(list_of_players[1].bye)
# print(list_of_players[4].name + " " + list_of_players[4].team + " " + list_of_players[4].rushing_att)


# for player in list_of_players:
#     print('the expected points for {}, is {}'.format(player.name, int(player.expected_points)))
