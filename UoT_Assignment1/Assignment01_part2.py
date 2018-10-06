""" Script: Assignment01_part2
   	Description: This script is responsible to create two dictionaries (provinces and capitals) and
    print out all combinations of the province names and the corresponding capitals.
   	Created by: Fábio Queiroz
   	Creation Date: 19.09.2018
   	Version: 1.0
"""
# Creating the dictionaries
provinces = {
    "Ontario" : "ON",
    "Quebec" : "QC",
    "British Columbia" : "BC",
    "Yukon" : "YT"
	#"Alberta" : "AB",
	#"Manitoba" : "MB",
	#"Nova Scotia" : "NS"
			}

capitals = {
    "ON" : "Toronto",
	"BC" : "Victoria",
	"QC" : "Quebec City",
	"YT" : "Whitehorse"
	#"AB" : "Edmonton",
	#"MB" : "Winnipeg",
    #"NS" : "Halifax"
			}
#Another way to add more provinces and capitals to the dictionaries.

# provinces ["Alberta"] = "AB"
# provinces ["Manitoba"] = "MB"
# provinces ["Nova Scotia"] = "NS"
#
# capitals ["AB"] = "Edmonton"
# capitals ["MB"] = "Winnipeg"
# capitals ["NS"] = "Halifax"

# Solution 1
# for province in provinces:
#     # Getting the value of the province using the function get().
#     prov = (provinces.get(province))
#     for capital in capitals:
#         # Comparing the province value to capital key.
#         if prov == capital:
#      	   print ("The capital of", province, "is", capitals.get(prov))

# Solution 2 - Refactored
for province in provinces:
    print ("The capital of", province, "is", (capitals.get(provinces.get(province))))
