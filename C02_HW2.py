import matplotlib.pyplot as py
import csv, csv, datetime

# open the file
with open("ubike.csv", "r", encoding = "cp950") as f:
    station = {}
    count = {}
    lat = {}
    lon = {}
    capacity = {}

    for row in csv.DictReader(f):
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if time == 17 or time == 18:
            id = int(row["id"])
            if id not in station:
                lat[id] = float(row["latitude"])
                lon[id] = float(row["longitude"])
                capacity[id] = int(row["lot"])
                station[id] = int(row["bike"])
                count[id] = 1
            else:
                station[id] += int(row["bike"])
                capacity[hour] += int(row["lot"])
                count[hour] += 1

# preparation for plotting
id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = []
redlon = []
yellowlat = []
yellowlon = []
greenlon = []
bluelat = []
bluelon = []

for k in id_seq:
    capacity[k] = (float(capacity[k]) / count[k])

py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
py.plot(redlat, redlon)
py.plot(yellowlat, yellowlon)
py.plot(bluelat, bluelon)
py.axis([25.01, 25.05, 121.52, 121.56])
py.legend(loc = "lower right")
py.show()
