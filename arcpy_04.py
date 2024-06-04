#. so now we can see the result of the script inside of the our scripte

import arcpy
import os

# Define the path to your project and the feature layer
project_path = r"C:\Users\amir\Documents\ArcGIS\Projects\MyProject_test170424\MyProject_test170424.aprx"

# Specify the map name explicitly
map_name = "Map"  # Change this to the actual map name if different
layer_name = "Baum_Clip_Weg"

# Define the output text file path
output_file_path = r"C:\Users\amir\Desktop\attribute_table.txt"

# Open the project
print(f"Opening project: {project_path}")
aprx = arcpy.mp.ArcGISProject(project_path)

# Access the map by name
print(f"Accessing map: {map_name}")
maps = aprx.listMaps(map_name)
if not maps:
    raise Exception(f"Map '{map_name}' not found in the project.")
else:
    print(f"Found map: {map_name}")

# There should be only one map with the name, if not, this will handle the first match
map_obj = maps[0]

# List all layers in the map for debugging
print("Available layers in the map:")
for lyr in map_obj.listLayers():
    print(f"Layer Name: {lyr.name}, Layer Type: {'Feature Layer' if lyr.isFeatureLayer else 'Other'}")

# Access the layer by name
print(f"Accessing layer: {layer_name}")
layers = map_obj.listLayers(layer_name)
if len(layers) == 0:
    raise Exception(f"Layer '{layer_name}' not found in the map.")
else:
    print(f"Found layer: {layer_name}")
layer = layers[0]

# Check if the layer is a feature layer
print(f"Checking if layer '{layer_name}' is a feature layer")
if not layer.isFeatureLayer:
    raise Exception(f"Layer '{layer_name}' is not a feature layer.")
else:
    print(f"Layer '{layer_name}' is a feature layer")

# Get the path to the layer's data source
data_source = layer.dataSource
print(f"Data source for layer '{layer_name}': {data_source}")

# Open a search cursor to read through the attribute table
print(f"Reading attribute table for layer '{layer_name}'")
with arcpy.da.SearchCursor(data_source, ["*"]) as cursor:
    # Open the output file in write mode
    print(f"Writing attribute table to file: {output_file_path}")
    with open(output_file_path, 'w') as file:
        # Write the header (field names)
        field_names = [field.name for field in arcpy.ListFields(data_source)]
        file.write("\t".join(field_names) + "\n")

        # Write each row of the attribute table to the file
        for row in cursor:
            file.write("\t".join(map(str, row)) + "\n")

print(f"Attribute table saved to {output_file_path}")

# Clean up
del aprx

# after that we wrote the scripte inside of the our pythión file (here is export_attribute_table) 
# we must run our script and then we must do this scipte after the line: (running ArcGIS Pro Python environmen)
"C:\Path\To\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" C:\Path\To\Your\Script\export_attribute_table.py

#the next we can do our Project insdie of it 

