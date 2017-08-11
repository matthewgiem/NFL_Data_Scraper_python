import re
import urllib2
from bs4 import BeautifulSoup



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
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

doc = Rtf15Reader.read(open('QB_season_2016.txt')) 

print PlaintextWriter.write(doc).getvalue()
