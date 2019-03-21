import numpy as np
import matplotlib.pyplot as plt

class Animal:
    def __init__(self, number, fear=(0,1), hunger=(0,1), curiosity=(0,1)):
        """
        Args = number to create, upper and lower bounds for attributes
        """
        self.number = number
        self.fear = np.random.normal(fear[0], fear[1], number)
        self.hunger = np.random.normal(hunger[0], hunger[1], number)
        self.curiosity = np.random.normal(curiosity[0], curiosity[1], number)

    def step(self):
        self.number *= 2
        self.fear += -1
        self.hunger += np.random.uniform(-1,1)
        self.curiosity += np.random.uniform(-1,1)

p1 = Animal(number=100)

filtered_dir = list(filter(lambda x : not x.startswith("__"), dir(p1)))

print(p1.__dict__)

#
# for elt in range(len(filtered_dir)):
#     print(f"{p1}".format(elt))
#
# import pandas as pd
#
# def sim_step(genomeList, repRate):
#     newList = []
#     for creature in genomeList:
#         newList.append()
