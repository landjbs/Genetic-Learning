import numpy as np
import matplotlib.pyplot as plt

class Animal:
    def __init__(self, number, fear, hunger, curiosity):
        self.number = number
        self.fear = fear
        self.hunger = hunger
        self.curiosity = curiosity

p1 = Animal(number=10, hunger= np.random.normal(0,1, 10), fear=1, curiosity=1)

print(p1.number)

plt.hist(p1.hunger)
plt.show()

# import pandas as pd
#
# genome is created as blank slate {"hunger":0, "curiosity":0, "fear":0}
# genome = [1,1,1]
#
# genomeList = [genome, list(map((lambda x : x * 2), genome))]
#
# print(genomeList)
#
#
# def sim_step(genomeList, repRate):
#     newList = []
#     for creature in genomeList:
#         newList.append()
