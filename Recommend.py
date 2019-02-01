browsing = open("./browsing.txt")
# items_fv = open("./items.txt", "w")
pairs_fv = open("./pairs.txt", "w")
trips_fv = open("./triples.txt", "w")

items = dict()

browsing.seek(0)
line = browsing.readline()

while len(line) != 0:
    line_items = line.strip().split(" ")
    for i in range(len(line_items)):
        items[line_items[i]] = items.get(line_items[i], 0) + 1
    line = browsing.readline()

# get only items with at elast 100 occurances
# TODO Change this back to 100
# items_list = [k for k,v in items.items() if int(v) >= 100]

for k, v in list(items.items()):
    if int(v) < 100:
        del items[k]

items_list = list(items.items())

items_list.sort()

# ----------------------------- pairs count
item_pairs_dict = dict()

browsing.seek(0)
line = browsing.readline()

while len(line) != 0:
    line_items = line.strip().split(" ")

    for i in range(len(line_items)):
        for j in range(len(line_items)):
            if (i != j and line_items[i] in items and line_items[j] in items):
                item_pairs_dict[(line_items[i], line_items[j])] = item_pairs_dict.get(
                    (line_items[i], line_items[j]), 0) + 1
    line = browsing.readline()

# -------------------------------------------------- pairs confidence

for k, v in list(item_pairs_dict.items()):
    if int(v) < 100:
        del item_pairs_dict[k]

item_pairs_list = list(item_pairs_dict.items())

item_pairs_list.sort()

item_pairs_list_sorted_by_conf = []

for k, v in item_pairs_list:
    conf = items.get(k[0])
    item_pairs_list_sorted_by_conf.append((k, v / conf))

item_pairs_list_sorted_by_conf = sorted(item_pairs_list_sorted_by_conf, key=lambda k: k[0][1])
item_pairs_list_sorted_by_conf = sorted(item_pairs_list_sorted_by_conf, key=lambda k: k[0][0])
item_pairs_list_sorted_by_conf = sorted(item_pairs_list_sorted_by_conf, key=lambda k: k[1], reverse=True)

for k, v in item_pairs_list_sorted_by_conf:
    pairs_fv.write(str(k) + " " + str(v) + "\n")

# ------------------------------------------------------------------- triples
item_trips_dict = dict()

for i in range(len(item_pairs_list)):
    for j in range(i):
        if (i != j):
            first = item_pairs_list[i][0]
            second = item_pairs_list[j][0]
            if first[0] == second[0]:
                item_trips_dict[(first[0], first[1],second[1])] = 0

# ---------------------- read in triples
browsing.seek(0)
line = browsing.readline()

while len(line) != 0:
    line_items = line.strip().split(" ")

    for i in range(len(line_items)):
        for j in range(len(line_items)):
            for k in range(len(line_items)):
                if (i != j and i != k and j != k):
                    combo = (line_items[i], line_items[j],line_items[k])
                    if (combo in item_trips_dict):
                        item_trips_dict[combo] = item_trips_dict.get(combo) + 1

    line = browsing.readline()

for k, v in list(item_trips_dict.items()):
    if int(v) < 100:
        del item_trips_dict[k]



# -------------------------------------------------- triples confidence

item_trips_list_sorted_by_conf = []
for k, v in list(item_trips_dict.items()):
    items_local = k

    count_of_pair = item_pairs_dict.get((items_local[0], items_local[1]))
    item_trips_list_sorted_by_conf.append((k, v / count_of_pair))





item_trips_list_sorted_by_conf = sorted(item_trips_list_sorted_by_conf, key=lambda k: k[0][2])
item_trips_list_sorted_by_conf = sorted(item_trips_list_sorted_by_conf, key=lambda k: k[0][1])
item_trips_list_sorted_by_conf = sorted(item_trips_list_sorted_by_conf, key=lambda k: k[0][0])
item_trips_list_sorted_by_conf = sorted(item_trips_list_sorted_by_conf, key=lambda k: k[1], reverse=True)

for v, k in item_trips_list_sorted_by_conf:
    trips_fv.write(str(v) + " " + str(k) + "\n")

browsing.close()
# items_fv.close()
pairs_fv.close()
trips_fv.close()
