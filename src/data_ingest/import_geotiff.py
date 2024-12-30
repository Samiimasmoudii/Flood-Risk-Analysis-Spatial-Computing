import rasterio
from rasterio.plot import show

# Load the DEM data (GeoTIFF file)
dem_file_path = 'path_to_elevation_data.tif'  # Replace with your DEM file path
with rasterio.open(dem_file_path) as dem:
    dem_data = dem.read(1)  # Read the first band
    show(dem)  # Display the elevation map
