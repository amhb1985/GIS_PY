
#this is about some training inside of my pc

import arcpy

# Define the path to your project and the feature layer
project_path = r"C:\Users\amir\Documents\ArcGIS\Projects\Arypy_project\Arypy_project.aprx"

# Change this to the name of your layer
# we have inside of our test arcpy project 3 different Layers(Point, Line, Insel) we use one of them:
ayername =  "Point"


# Open the project
aprx = arcpy.mp.ArcGISProject(project_path)

# Access the first map in the project (modify this if you have multiple maps)
#inside of parallel we have another problem that with [] i cannot find the exact Keyborad and i must ust the google translator to insetr it with the click of Mouse instead of Keyboard.

map = aprx.listMaps()[0]

# Access the layer by name
layer = map.listLayers(layer_name)[0]

# Check if the layer is a feature layer
if layer.isFeatureLayer:
    # Get the path to the layer's data source
    data_source = layer.dataSource

    # Open a search cursor to read through the attribute table
    with arcpy.da.SearchCursor(data_source, ["*"]) as cursor:
        for row in cursor:
            print(row)  # Print each row in the attribute table

# Clean up
del aprx
