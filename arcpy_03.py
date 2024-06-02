
#this is about some training inside of my pc

import arcpy

# Define the path to your project and the feature layer

project_path = r"C:\Path\To\Your\ArcGISProject.aprx"
layer_name = "YourLayerName"  # Change this to the name of your layer

# Open the project
aprx = arcpy.mp.ArcGISProject(project_path)

# Access the first map in the project (modify this if you have multiple maps)
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
