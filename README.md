# QGIS-Spatial-Information-Systems-
A basic QGIS Project that plots farms(polygons) and farmer houses(points) given the csv files.

We are given with csv files that give the details of Farmer-(i.e., Farmers.csv) and Lands (Farm-Copy.csv)(owned by the farmer).
There is another csv file giving the information about the Livestock of farmers-(Livestock.csv).
A python code was written to embed the livestock of each farmer into the 'Farmer.csv' file.
Another python code was written to convert the available raw data entries into WKT(well known text) format so as to plot the polygons in QGIS. The changed values will be written into 'Farm.csv'.
Some of the polygons in raw data were only given with single points(bad data). So, based on the area of each farm the points are inflated resulting in genereting four vertices so as to form a polygon.
