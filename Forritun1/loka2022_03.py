d = {}
name_views = {}

with open(r"C:\Users\Tommi\Forritun Visual stud\videos_textfiles\videos_01.txt") as f:
    for line in f:
        (key, val, gal) = line.split(",")
        d[(val, key)] = int(gal)

        if val not in name_views:
            name_views[val] = {"total_views": 0, "count": 0}

        name_views[val]["total_views"] += int(gal)
        name_views[val]["count"] += 1

for val, stats in name_views.items():
    total_views = stats["total_views"]
    count = stats["count"]
    monthly_views = total_views / count
    print(f"Name: {val}, Total views: {total_views}, Monthly views: {monthly_views}")
