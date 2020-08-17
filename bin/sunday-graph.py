from os import environ
import matplotlib.pyplot as plt

HOME = environ['HOME']

sets = {}

with open(f"{HOME}/velocity", "r") as fp:
    for line in fp:
        date, discipline, count = line.split("\t")
        s = sets.get(discipline, [])
        s.append(count)
        sets[discipline] = s

for k, vals in sets.items():
    plt.plot(vals, label=k)
    plt.xlabel("date")
    plt.ylabel("done count")

plt.show()
