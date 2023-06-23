# JBG050---Group-4

The creation of our database can be found in the notebook "Creating_database.ipynb". The notebook first goes over all the files available from the london police.
Then it adds all the data to the database. The file contains the creation of the most recent table in the database. The other tables are created in the same way. 

The "Plotting_wards.ipynb" file is used to explore the data.

The "Time_series_model.ipynb" file splits the database into wards and then creates a model for each ward. In the end it evaluates the models and you
can find the test scores that are used in the technical report for the SARIMA model.

barnet_LSOA.geojson was used for some plots. Its origin is "https://github.com/gausie/LSOA-2011-GeoJSON".



The statistical evaluation for the KDE can be found in the notebook "KDE evaluation.ipynb" in the KDE folder.
This notebook loads the data from the SQL database, then performs the KDE statistical analysis found in the technical report


Other files:
Additional Models (VAR expanded, KDE).ipynb contains a rough exploration of a VAR model and KDE. (Unrelated to technical report)
Comparison Functions VAR-KDE.ipynb contains a rough comparison of the discarded VAR model and KDE. (Unrelated to technical report)
The "Old" folder contains exploration that was discarded or integrated into newer files. (Unrelated to technical report)
