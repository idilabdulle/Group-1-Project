# Group 1 Project

## Project Description

The purpose of our project is to understand the relationship between crime in English regions and their index of multiple deprivation. Our hypothesis is that areas with higher levels of deprivation (the closer to 1 they are ranked the more deprived they are) are more likely to experience higher levels of crime.

Whilst the primary focus of this project was the relationship between crime and deprivation, we also explored selected ONS wellbeing indicators to investigate whether similar regional patterns were observed beyond the IMD framework. This provided additional context for interpreting regional differences in recorded crime and allowed comparisons between deprivation and broader measures of wellbeing.

The IMD data comes out every four - five years so by completing our analysis and then building a machine learning model which predicts the IMD score for an ITL2 region, based on the level of crime it has experienced that year we aim to provide annual estimates for local (ITL2 regions) areas based on our model.

This matters for both the police and local authorities and can help with future planning for care by local authorities. Additionally, the broader wellness data helps to give another dimension of detail which can help to inform the level of crime and impact on deprivation within an area. This can help local authorities ensure both enforcement and medical help are provided.

## Setup Instructions 

Please ensure that you have Python installed prior to project setup. Additionally, whilst this project can be run in a browser of your choice (using Jupyter Notebook), if you would like to use an IDE, such as Visual Studio Code, please ensure that this is also installed and setup.

 - Use your terminal to navigate to the folder that you would like to clone the repository into: use `cd` followed by your folder name or path
 - Clone the GitHub 'Group-1-Project' repository: copy the repository URL by clicking the green '<> Code' button and then clicking the HTTPS copy button, in your terminal use the command `git clone` and paste the URL
 - Install all dependencies: use the command `pip install -r requirements.txt`

Using Jupyter Notebook in your browser:
 -  Navigate to your local repository: use `cd` and your folder name or path
 -  Initiate Jupyter Notebook: use the command `jupyter notebook` in your terminal
 -  Use Jupyter Notebook in your browser: copy the URL found directly underneath 'To access the server, open this file in a browser:', paste this URL in the browser of your choice

## Requirements list 

Please utilise the [requirement.txt](requirement.txt]) file, to install all required python packages. This can be done by using the following command `pip install -r requirements.txt`. The packages required for this project are also listed below, for ease of reference. 

**Requirements:**
 - numpy
 - pandas
 - matplotlib
 - seaborn
 - openpyxl
 - geopandas
 - scikit-learn
 - os
 - LB_shp Folder

## How to execute the code

Please now find the Jupyter Notebook file called 'group_1_notebook.ipynb', this is the main notebook for this project. To run this file, please open this in your browser by following the instructions above, or open this in an IDE of your choice, as you would open any other file. Please run each code cell individually and in sequential order (from top to bottom). The cells of this notebook are a mixture of code cells and markdown cells, you do not need to run the markdown cells - these are solely for your reference and information. Please ensure that you have completed all of the set up steps above before executing the code. If you have not, for example, installed all required Python packages, then the code will not run.

Also please find the [clean_2026_data.py](machine_learning\clean_2026_data.py) file needs to be run to predict the machine learning model.

Individual archived Python and Jupyter Notebook files can be found in the 'archived_materials', however these are solely for archival purposes and not for active use. Please do not run these scripts. 

# Data Sources

Five datasets were utilised for this project, these are also detailed in the Group Project Report. 

> **Crime dataset**
>  - The ‘Police recorded crime Police Force Area Open Data tables, from year ending March 2013 to year ending December 2025’ dataset was published by the Home Office and accessed on the 8th June 2026, using the link ‘https://www.gov.uk/government/statistical-data-sets/police-recorded-crime-and-outcomes-open-data-tables’. 
>  - The original Excel file is called [old_historical_crime_data.xlsx](old_data\old_historical_crime_data.xlsx) and can be found in the 'old_data' folder. The cleaned csv file with regional data is called [CLEANED-regional_forces_crime_data_2024-2025.csv](clean_materials\CLEANED-regional_forces_crime_data_2024-2025.csv), and can be found in the clean materials folder.

> **Index of Multiple Deprivation (IMD) dataset**
>  - The ‘English Indices of Deprivation 2025 (IoD25) – Index of Multiple Deprivation’ dataset was published by the Ministry of Housing, Communities & Local Government (MHCLG) and accessed on 9th June 2026, using the link 'https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025' on 9th June 2026.
>  - The original Excel file is called [old_2025_index_of_multiple_deprivation.xlsx](old_data\old_2025_index_of_multiple_deprivation.xlsx) and can be found in the 'old_data' folder. The cleaned csv file is called [][clean_index_of_multiple_deprivation.csv](clean_materials\clean_index_of_multiple_deprivation.csv) and can be found in the clean materials folder.

> **Wellness dataset**
>  - The ‘UK Measures of National Well-being: February 2025’ dataset was published by the Office for National Statistics (ONS) and accessed on the 8th June 2026, using the link ‘https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/datasets/ukmeasuresofnationalwellbeing’.
>  - The original Excel file is called [ukmeasuresofnationalwellbeingfeb20251.xlsx](old_data\ukmeasuresofnationalwellbeingfeb20251.xlsx) and can be found in the 'old_data' folder. The cleaned Excel file is called [CLEANED-Wellness_Data.xlsx](clean_materials\CLEANED-Wellness_Data.xlsx) and can be found in the clean materials folder.

> **Local Authority District Lookup dataset**
>  - The 'Local Authority District (December 2024) to LAU1 to ITL3 to ITL2 to ITL1 (January 2025) Lookup in the UK' dataset was published by the ONS and was accessed on 9th June 2026, using the link 'https://www.data.gov.uk/dataset/2b47adcc-62b6-4dd3-a6cb-271b3035e9fd/local-authority-district-december-2024-to-lau1-to-itl3-to-itl2-to-itl1-january-2025-lookup-in-t'.
>  -  The csv file is called [LAD_2024_to_ITL_2025.csv](clean_materials\extra_materials\LAD_2024_to_ITL_2025.csv) and can be found in the 'extra_materials', within the 'clean_materials' folder.

> **Population Estimates dataset**
>  - The ‘Mid-Year Population Estimates, England and Wales, June 2024’ dataset was accessed on the 21st June 2026, using the link ’https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/estimatesofthepopulationforenglandandwales’.
>  - The csv file is called 
[Mid-2024_Estimates_population.xlsx](clean_materials\extra_materials\Mid-2024_Estimates_population.xlsx) and can be found in the 'extra_materials', within the 'clean_materials' folder.

# Extra Info
All members original code are in the [archived_materials](archived_materials) folder where you can see line by line the different notebooks / scripts that team members used throughout the process. These have all been condensed into the [group_1_notebook.ipynb](group_1_notebook.ipynb) for clarity and simplicity.


## Team member contributions 
Team members:
 - **Jade McFarlane**
 - Project Manager, Data Loading (crime), Data Cleaning and Preprocessing (crime), Data Visualisations (UK wide), Machine Learning Implementation, Jupyter Notebook & GitHub Organisation

 - **Rebecca Parker**
 - Data Loading (IMD), Data Cleaning and Preprocessing (IMD), Data Visualisations (North, Midlands & South), Machine Learning Implementation, README Write Up, Methods Section of Project Report

 - **Idil Abdulle**
 - Exploratory Data Analysis, Data Visualisations (South of England), Project Presentation Creation

 - **Kelly O’Keefe**
 - Exploratory Data Analysis, Data Visualisations (London), Project Report Write Up

 - **Rebecca Swarbrick**
 - Data Loading (wellness), Data Cleaning (wellness), Data Visualisations (UK wide), Project Presentation

 - **Maeve Finneran**
 - Intro/background Project Report

 - **Hong Tu**
 - Review of Report
