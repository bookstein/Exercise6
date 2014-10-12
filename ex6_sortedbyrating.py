def main():
    restaurant = sort_file("scores.txt")
    print_file(restaurant)

def sort_file(filename):

    # Open text file of scores. Read in the data contained
    restaurant = {}

    ratings = open(filename)


    # Slice data by colon to get name of restaurant and scores in a for loop line by line
    #for line in f

    for line in ratings:
        line = line.rstrip()
        rest_name, rest_score = line.split(':')
        restaurant[rest_name] = int(rest_score)

    return restaurant


# get values out of dictionary and sort by rating, then alphabetical order
def sort_by_rating(dictionary):
    l = dictionary.items()
    sorted_list = []
    for item in l:
        sorted_list.append((item[1], item[0]))
    return sorted_list


# print sorted_rest
def print_file(restaurant):
    for rating, rest in sorted(sort_by_rating(restaurant)):
        # restaurant[rest] = rating
        print "Restaurant %s is rated at %d" % (rest, int(rating))


if __name__ == "__main__":
    main()