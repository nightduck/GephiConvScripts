# GephiConvScripts
Python Scripts to convert arbitrary files into Gephi friendly formats

osm_gdf_conv.py:
Vertices represent intersections and edges represent the streets between them. Certain streets such as private drives and service roads are ignored. Geocoding is also available. Placing a shapefile and related files into a directory named "SHP" will be used to map a location (typically a city) to each set of coordinates. To bypass geocoding, find the appropriate part in the script and comment it out. This will not affect the rest of the script.
