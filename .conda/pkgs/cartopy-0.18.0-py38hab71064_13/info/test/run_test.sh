

set -ex



python -c "import cartopy.crs as ccrs; import matplotlib.pyplot as plt; ax = plt.axes(projection=ccrs.PlateCarree())"
exit 0
