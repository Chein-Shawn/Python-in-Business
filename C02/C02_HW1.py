import matplotlib.pyplot as py
import csv, datetime

# open the file
with open("ubike.csv", "r", encoding = "cp950") as f:
    bike = {}
    capacity = {}
    count = {}

    for row in csv.DictReader(f):
        if row["station"] == "Roosevelt & Xinsheng S. Intersection":
            time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
            hour = time.hour
            if hour not in bike:
                bike[hour] = int(row["bike"])
                capacity[hour] = int(row["lot"])
                count[hour] = 1

            else:
                bike[hour] += int(row["bike"])
                capacity[hour] += int(row["lot"])
                count[hour] += 1

# preparation for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []
lot = []
for k in time_seq:
    avg.append(float(bike[k]) / count[k])
    lot.append(float(capacity[k] / count[k]))

py.plot(time_seq, lot, label = "Capacity", color = "orange")
py.plot(time_seq, avg, label = "Average", color = "b")
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
# py.ylim(1, 115)
py.ylim(0, max(lot)+30)
py.legend(loc = "upper right")
py.show()
