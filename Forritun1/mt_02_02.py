d = {}
name_views = {}

length = 0

with open(r"C:\Users\Tommi\Forritun Visual stud\mt_02_textfiles\eurovision01.txt") as f:
    for line in f:
        (key, val, gal) = line.split(" ")
        d[(val, key)] = int(gal)

        length = length + 1

        if val not in name_views:
            name_views[val] = {"total_views": 0, "count": 0}

        name_views[val]["total_views"] += int(gal)

        if val < key:
            country_pair = val + "-" + key
        else:
            country_pair = key + "-" + val

        if country_pair not in d:
            d[country_pair] = 0
        d[country_pair] += int(gal)


for val, stats in sorted(name_views.items()):
    total_views = stats["total_views"]
    print(f"Name: {val}, Total views: {total_views}")

if length > 10:
    pairlist = []
    for key, val in d.items():
        pairlist.append([val, key])

    pairlist.sort()
    pairlist.reverse()

    for i in range(5):
        print(i + 1, pairlist[i][1], pairlist[i][0])
