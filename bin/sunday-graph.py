from os import environ
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

HOME = environ['HOME']

sets = {}

with open(f"{HOME}/velocity", "r") as fp:
    for line in fp:
        date, discipline, count = line.split("\t")
        s = sets.get(discipline, [])
        s.append(count)
        sets[discipline] = s

keys = sets.keys()
values = zip(*[map(int, v) for tup in list(zip(sets.values())) 
                           for v in tup])
periods = len(list(sets.values())[0])


data = pd.DataFrame(values, list(range(0, periods)), columns=keys)
sns.lineplot(data=data, palette="tab10", linewidth=2.5)

# plt.show()
plt.savefig("build/velocity.png")
