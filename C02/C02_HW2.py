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
        if hour == 17 or hour == 18:
            id = int(row["id"])
            if id not in station:
                lat[id] = float(row["latitude"])
                lon[id] = float(row["longitude"])
                capacity[id] = int(row["lot"])
                station[id] = int(row["bike"])
                count[id] = 1
            else:
                station[id] += int(row["bike"])
                capacity[id] += int(row["lot"])
                count[id] += 1
            

# preparation for plotting
id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = []
redlon = []
yellowlat = []
yellowlon = []
greenlat = []
greenlon = []
bluelat = []
bluelon = []
perc = {}

for k in id_seq:
    capacity[k] = (float(capacity[k]) / count[k])
    station[k] = (float(station[k]) / count[k])
    perc[k] = (float(station[k]) / capacity[k])

for id in id_seq:
    if perc[id] < 0.2:
        redlat.append(lat[id])
        redlon.append(lon[id])
    elif 0.2 <= perc[id] < 0.3:
        yellowlat.append(lat[id])
        yellowlon.append(lon[id])
    elif 0.3 <= perc[id] < 0.4:
        greenlat.append(lat[id])
        greenlon.append(lon[id])
    elif 0.4 <= perc[id]:
        bluelat.append(lat[id])
        bluelon.append(lon[id])

py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
# py.plot(redlat, redlon, color = 'r', marker = 'o', linestyle='none')
py.plot(redlat, redlon, 'ro', linestyle='none', label = "<20%")

py.plot(yellowlat, yellowlon, marker = 'o', color = 'y', linestyle='none', label = "20%~30%")
py.plot(greenlat, greenlon, marker = 'o', color = 'g', linestyle='none', label = "30%~40%")
py.plot(bluelat, bluelon, marker = 'o', color = 'b', linestyle='none', label = ">=40%")
py.axis([25.01, 25.05, 121.52, 121.56])
py.legend(loc = "lower right")
py.show()
