import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# genome is created as blank slate {"hunger":0, "curiosity":0, "fear":0}
genome = [1,1,1]

genomeList = [genome, list(map((lambda x : x * 2), genome))]

print(genomeList)


def sim_step(genomeList, repRate):
    newList = []
    for creature in genomeList:
        newList.append()
