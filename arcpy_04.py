##this is the secound script but now for the Python IDEL bcos we want the result as text
#in our desktop

import arcpy
import os

# Define the path to your project and the feature layer
project_path = r"C:\Users\amir\Documents\ArcGIS\Projects\Arypy_project\Arypy_project.aprx"

# Change this to the name of your layer
layer_name = "Point"

# Define the output text file path
output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "attribute_table.txt")

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
        # Open the output file in write mode
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


#test again inside of arcpro with another project