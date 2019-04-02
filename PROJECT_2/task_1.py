import pandas as pd
from ast import literal_eval
import gmplot

trainSet = pd.read_csv(
    'train_set.csv', # replace with the correct path
    converters={"Trajectory": literal_eval}, 
    index_col='tripId'
)

latitudes = []
longitudes = []
i = 0;

for rownum, row in trainSet.iterrows():
    i = i + 1
    name = "mymap" + str(i) + ".html"
    latitudes = []
    longitudes = []
    if(i > 5):
        break
    for trajectories in row["Trajectory"]:
        latitudes.append(trajectories[1])
        longitudes.append(trajectories[2])
    gmap = gmplot.GoogleMapPlotter(longitudes[0], latitudes[0], 14)
    gmap.plot(longitudes, latitudes, 'cornflowerblue', edge_width=10)
    gmap.draw(name)

