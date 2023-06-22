# JBG050---Group-4

The creation of our database can be found in the notebook "Creating_database.ipynb". The notebook first goes over all the files available from the london police.
Then it adds all the data to the database. 

The "Plotting_wards.ipynb" file is used to explore the data.

The "Time_series_model.ipynb" file splits the database into wards and then creates a model for each ward. In the end it evaluates the models and you
can find the test scores that are used in the technical report for the SARIMA model.

LSOA converted to geojson can be found at "https://github.com/gausie/LSOA-2011-GeoJSON"



The statistical evaluation for the KDE can be found in the notebook "KDE evaluation.ipynb" in the KDE folder.
This notebook loads the data from the SQL database, then performs the KDE statistical analysis found in the technical report
