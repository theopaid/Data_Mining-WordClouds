import pandas as pd
from ast import literal_eval
import gmplot
from fastdtw import fastdtw
from haversine import haversine

testSet = pd.read_csv(
    # replace with the correct path
    'test_set_a1.csv', converters={"Trajectory": literal_eval}, sep="\n"
)

i = -1
testSet_coordinates = []

for rownum, row in testSet.iterrows():
    testSet_coordinates = []
    i = -1
    for trajectories in row["Trajectory"]:
        i = i + 1
        #append double list
        testSet_coordinates.append([])
        testSet_coordinates[i].append(trajectories[1])
        testSet_coordinates[i].append(trajectories[2])

#distance, path = fastdtw()
print testSet_coordinates
