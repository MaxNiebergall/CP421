import itertools

browsing = open("F:/Programming/CP421/browsing.txt")


items = dict()

browsing.seek(0)
line = browsing.readline()

while len(line) != 0:
    line_items = line.strip().split(" ")
    for i in range(len(line_items)):
            items[line_items[i]] = items.get(line_items[i], 0) + 1
    line = browsing.readline()


#get only items with at elast 100 occurances
#TODO Change this back to 100
#items_list = [k for k,v in items.items() if int(v) >= 100]
for k,v in list(items.items()):
    if int(v) <100:

        del items[k]

item_pairs_dict = dict()

browsing.seek(0)
line = browsing.readline()


while len(line) != 0:
    line_items = line.strip().split(" ")

    for i in range(len(line_items)):
        for j in range(i):
            if ( i!= j and line_items[i] in items and line_items[j] in items):
                item_pairs_dict[line_items[i] + " " + line_items[j]] = item_pairs_dict.get(line_items[i] + " " + line_items[j], 0) + 1

    line = browsing.readline()

item_trips_dict = dict()

for k,v in list(item_pairs_dict.items()):
    if(v > 100):
        print(k,v)


browsing.seek(0)
line = browsing.readline()


while len(line) != 0:
    line_items = line.strip().split(" ")

    for i in range(len(line_items)):
        for j in range(i):
            for k in range(j):
                if ( (i!=j and i!=k and j!=k) ):
                    item_trips_dict[line_items[i] + " " + line_items[j]+ " " + line_items[k]] = item_pairs_dict.get(line_items[i] + " " + line_items[j]+ " " + line_items[k], 0) + 1

    line = browsing.readline()


item_trips_dict[line_items[i] + " " + line_items[j]]
item_trips_dict[line_items[i] + " " + line_items[k]]
item_trips_dict[line_items[j]+ " " + line_items[k]]
item_trips_dict[line_items[i] + " " + line_items[j]+ " " + line_items[k]]


