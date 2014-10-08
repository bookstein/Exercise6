# Open text file of scores. Read in the data contained
restaurant = {}

ratings = open("scores.txt")


# Slice data by colon to get name of restaurant and scores in a for loop line by line
#for line in f

for line in ratings:
    line = line.rstrip()
    rest_name, rest_score = line.split(':')
    restaurant[rest_name] = int(rest_score)

# get values out of dictionary and sort by alphabetical order

for rest in sorted(restaurant):
    print "Restaurant %s is rated at %d" % (rest, restaurant[rest])