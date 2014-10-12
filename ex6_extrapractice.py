def create_dictionary(filename):
	listings = {}

	f = open(filename)
	for line in f:
		restaurant, rating = line.strip().split(":")
		listings[restaurant] = int(rating)

	return listings

def sort_by_alphabet(dictionary):
	for key in sorted(dictionary.keys()):
		print "ALPHABETICAL Restaurant %s is rated: %d" % (key, dictionary[key])

def sort_by_rating(dictionary):
	ratings_list = dictionary.items()
	ratings_list.sort(key = lambda x: x[1], reverse = True)

	for listing in ratings_list:
		print "RATING Restaurant %s is rated %d" % (listing[0], listing[1])

def main():
	listings = create_dictionary("scores.txt")
	sort_alphabet = sort_by_alphabet(listings)
	sort_ratings = sort_by_rating(listings)


if __name__ == "__main__":
	main()