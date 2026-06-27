# Group 1 Project

## Project Description

This project investigates crime, deprivation and wellness data across England - seeking to gain a better understanding of the deprivation and societal issues experienced across the country. 

We utilise a range of official statistics published by the UK Government for the year of 2025; this data source selection was an active decision, as employing a trusted source provides a level of assurance to the data and subsequent results and conclusions. The latest statistical release of the Index of Multiple deprivation (IMD) for England was on the 30th October 2025, hence the decision to utilise data from 2025. 

IMD rankings are only released by the UK Government every four to six years. This project has additional real-world benefit, as our machine learning implementation (to predict more recent/future IMD rankings) will provide valuable predicitions and insights in the interim between IMD publications. These predictions would support a range of individuals and groups, such as policymakers, disaster management professionals, resilience planners and researchers, in fields such as health and human geography.

This project answers the question: ''?

## Setup Instructions 

Please ensure that you have Python installed prior to project setup. Additionally, whilst this project can be run in a browser of your choice (using Jupyter Notebook), if you would like to use an IDE, such as Visual Studio Code, please ensure that this is also installed and setup.

 - Use your terminal to navigate to the folder that you would like to clone the repository into: use `cd` followed by your folder name or path
 - Clone the GitHub 'Group-1-Project' repository: copy the repository URL by clicking the green '<> Code' button and then clicking the HTTPS copy button, in your terminal use the command `git clone` and paste the URL
 - Install all dependencies: in your terminal use the command `pip install -r requirements.txt`

Using Jupyter Notebook in your browser:
 -  Navigate to your local repository: use `cd` and your folder name or path
 -  Initiate Jupyter Notebook: use the command `jupyter notebook` in your terminal
 -  Use Jupyter Notebook in your browser: copy the URL found directly underneath 'To access the server, open this file in a browser:', paste this URL into the browser of your choice

## Requirements list 

Please utilise the requirement.txt file, to install all required python packages. This can be done by using the following command `pip install -r requirements.txt`. The packages required for this project are also listed below, for ease of reference. 

**Requirements:**
 - numpy
 - pandas
 - matplotlib
 - seaborn
 - openpyxl
 - geopandas
 - scikit-learn

## How to execute the code

Please now find the Jupyter Notebook file called 'group_1_notebook.ipynb', this is the main notebook for this project. This file can be run in your IDE or browser. Please see the instructions above for guidance on how to run Jupyter Notebook files in your browser. 

Please run each code cell individually and in sequential order (from top to bottom). The cells of this notebook are a mixture of code cells and markdown cells - you do not need to run the markdown cells, these are solely for your reference and information. Please ensure that you have completed all setup instructions, found above, before executing the code. If you have not, for example, installed all of the required Python packages, the code will not run.  

Individual archived Python and Jupyter Notebook files can be found in the 'archived_materials' folder, however these are solely for archival purposes and not for active use. Please do not run these scripts.

# Data Sources

Five datasets were utilised for this project, these are also detailed in the Group Project Report. 

> **Crime dataset**
>  - The ‘Police recorded crime Police Force Area Open Data tables, from year ending March 2013 to year ending December 2025’ dataset was published by the Home Office and accessed on the 8th June 2026, using the link ‘https://www.gov.uk/government/statistical-data-sets/police-recorded-crime-and-outcomes-open-data-tables’.
>  - The original Excel file is called 'old_historical_crime_data.xlsx' and can be found in the 'old_data' folder. The cleaned csv file is called 'CLEANED-regional_forces_crime_data_2024-2025.csv', and can be found in the main repository.

> **Index of Multiple Deprivation (IMD) dataset**
>  - The ‘English Indices of Deprivation 2025 (IoD25) – Index of Multiple Deprivation’ dataset was published by the Ministry of Housing, Communities & Local Government (MHCLG) and accessed on 9th June 2026, using the link 'https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025' on 9th June 2026.
>  - The original Excel file is called 'old_2025_index_of_multiple_deprivation.xlsx' and can be found in the 'old_data' folder. The cleaned csv file is called 'clean_index_of_multiple_deprivation.csv' and can be found in the main repository.

> **Wellness dataset**
>  - The ‘UK Measures of National Well-being: February 2025’ dataset was published by the Office for National Statistics (ONS) and accessed on the 8th June 2026, using the link ‘https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/datasets/ukmeasuresofnationalwellbeing’.
>  - The original Excel file is called 'wellbeing_data.xlsx' and can be found in the 'old_data' folder. The cleaned Excel file is called 'Wellness_Data.xlsx' and can be found in the '_' folder.

> **Local Authority District Lookup dataset**
>  - The 'Local Authority District (December 2024) to LAU1 to ITL3 to ITL2 to ITL1 (January 2025) Lookup in the UK' dataset was published by the ONS and was accessed on 9th June 2026, using the link 'https://www.data.gov.uk/dataset/2b47adcc-62b6-4dd3-a6cb-271b3035e9fd/local-authority-district-december-2024-to-lau1-to-itl3-to-itl2-to-itl1-january-2025-lookup-in-t'.
>  - The csv file is called 'LAD_2024_to_ITL_2025.csv' and can be found in the 'old_data' folder.

> **Population Estimates dataset**
>  - The ‘Mid-Year Population Estimates, England and Wales, June 2024’ dataset was accessed on the 21st June 2026, using the link ’https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/estimatesofthepopulationforenglandandwales’.
>  - The csv file is called 'LAD_2024_to_ITL_2025.csv' and can be found in the '_' folder.

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
 - Data Visualisation (heatmap)
