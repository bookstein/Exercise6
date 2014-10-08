# import file

score_file = open("scores.txt")

#create empty dictionary
restaurant_ratings = {}

#iterate file, line by line
for line in score_file:
	# remove ending \n from file, save as line
	line = line.rstrip()
	# each file line becomes a list called ratings
	ratings = line.split(":")

	# put into dict using key assignment
	for restaurant in ratings:
		restaurant_ratings[ratings[0]] = int(ratings[1])

#alphabetize (sort) a list of keys
restaurant_list = restaurant_ratings.keys()
restaurant_list.sort()

# print in a for loop over the list of restaurant keys
	# use the key to get to the corresponding value in dict
for restaurant in restaurant_list:
	print "Restaurant %s is rated at %d" % (restaurant, restaurant_ratings[restaurant])


# this took about 15 minutes. 10/7