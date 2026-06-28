## Cleaning 2026 data to use to predict

import pandas as pd

df_2026 = pd.read_excel("old_data\old_historical_crime_data.xlsx",
            sheet_name="2025_26",
            index_col=0)

# Need to clean the data from Force Name
ITL_1_matches = { # Note I don't have any Scotland or Northern Ireland data due to the various devolved powers. I have mapped the Welsh and national english forces but will remove these at a later stage, so that a deep dive of english regional data only can be done.
    "Avon and Somerset": "South West (England)",
    "Bedfordshire": "East (England)",
    "British Transport Police": "UK",
    "Cambridgeshire": "East (England)",
    "Cheshire": "North West (England)",
    "Cleveland": "North East (England)",
    "Cumbria": "North West (England)",
    "Derbyshire": "East Midlands",
    "Devon and Cornwall": "South West (England)",
    "Dorset": "South West (England)",
    "Durham": "North East (England)",
    "Dyfed-Powys": "Wales",
    "Essex": "East (England)",
    "Gloucestershire": "South West (England)",
    "Greater Manchester": "North West (England)",
    "Gwent": "Wales",
    "Hampshire": "South East (England)",
    "Hertfordshire": "East (England)",
    "Humberside": "Yorkshire and The Humber",
    "Kent": "South East (England)",
    "Lancashire": "North West (England)",
    "Leicestershire": "East Midlands",
    "Lincolnshire": "East Midlands",
    "London, City of": "London",
    "Merseyside": "North West (England)",
    "Metropolitan Police": "London",
    "Norfolk": "East (England)",
    "North Wales": "Wales",
    "North Yorkshire": "Yorkshire and The Humber",
    "Northamptonshire": "East Midlands",
    "Northumbria": "North East (England)",
    "Nottinghamshire": "East Midlands",
    "South Wales": "Wales",
    "South Yorkshire": "Yorkshire and The Humber",
    "Staffordshire": "West Midlands",
    "Suffolk": "East (England)",
    "Surrey": "South West (England)",
    "Sussex": "South East (England)",
    "Thames Valley": "South East (England)",
    "Warwickshire": "West Midlands",
    "West Midlands": "West Midlands",
    "West Mercia": "West Midlands",
    "West Yorkshire": "Yorkshire and The Humber",
    "Wiltshire": "South West (England)",
    "Action Fraud": "UK",
    "CIFAS": "UK",
    "UK Finance": "UK"
    }

df_2026["ITL1 region"] = df_2026["Force Name"].map(ITL_1_matches) # Mapping regions to the various police forces

print(df_2026["ITL1 region"].isnull().sum()) # To test every police force has been mapped to make sure there are no null values
print(df_2026["ITL1 region"].info()) # To test every police force has been mapped by counting the number of rows in this column vs the document

# Our other data doesn't have Wales in it and as there is no Scotland or Northern Irish data it is best to stick to England. Therefore I have deleted Wales from the dataset

updated_df = df_2026.copy() #Making a copy which is where I remove a lot of data

welsh_forces = updated_df[updated_df["ITL1 region"] == "Wales"] # Filtering to only include Wales forces

# Can be removed but an example of filtering data to only Welsh forces
welsh_forces.drop_duplicates(subset='ITL1 region', inplace=True) # Removing all with Wales
welsh_forces.reset_index(inplace=True) # Setting the index to numbers so its easy to remove
welsh_forces.drop(0, inplace=True) # Now I have no welsh forces in this filter
# updated_df.info()


updated_df.loc[updated_df["ITL1 region"] == "Wales", "ITL1 region"] = None # Making this null values so I can remove the data
updated_df.dropna(inplace=True) # Removing Welsh data
print(updated_df.info()) # Checking to make sure it has been removed

ITL_2_matches = {
    "Avon and Somerset": "West of England;North Somerset, Somerset and Dorset",
    "Bedfordshire": "Bedfordshire and Hertfordshire",
    "British Transport Police": "UK",
    "Cambridgeshire": "Cambridgeshire and Peterborough",
    "Cheshire": "Cheshire",
    "Cleveland": "Tees Valley",
    "Cumbria": "Cumbria",
    "Derbyshire": "Derbyshire and Nottinghamshire",
    "Devon and Cornwall": "Devon;Cornwall and Isles of Scilly",
    "Dorset": "North Somerset, Somerset and Dorset",
    "Durham": "Northumberland, Durham and Tyne & Wear",
    "Dyfed-Powys": "Mid and South West Wales",
    "Essex": "Essex",
    "Gloucestershire": "Gloucestershire and Wiltshire",
    "Greater Manchester": "Greater Manchester",
    "Gwent": "South East Wales",
    "Hampshire": "Hampshire and Isle of Wight",
    "Hertfordshire": "Bedfordshire and Hertfordshire",
    "Humberside": "East Yorkshire and Northern Lincolnshire",
    "Kent": "Kent",
    "Lancashire": "Lancashire",
    "Leicestershire": "Leicestershire, Rutland and Northamptonshire",
    "Lincolnshire": "Lincolnshire",
    "London, City of": "Inner London - West",
    "Merseyside": "Merseyside",
    "Metropolitan Police": "Inner London - West;Inner London - East;Outer London - East and North East;Outer London - South;Outer London - West and North West",
    "Norfolk": "Norfolk",
    "North Wales": "North Wales",
    "North Yorkshire": "North Yorkshire",
    "Northamptonshire": "Leicestershire, Rutland and Northamptonshire",
    "Northumbria": "Northumberland, Durham and Tyne & Wear",
    "Nottinghamshire": "Derbyshire and Nottinghamshire",
    "South Wales": "South East Wales;Mid and South West Wales",
    "South Yorkshire": "South Yorkshire",
    "Staffordshire": "Shropshire and Staffordshire",
    "Suffolk": "Suffolk",
    "Surrey": "Surrey, East and West Sussex",
    "Sussex": "Surrey, East and West Sussex",
    "Thames Valley": "Berkshire, Buckinghamshire and Oxfordshire",
    "Warwickshire": "Herefordshire, Worcestershire and Warwickshire",
    "West Mercia": "Shropshire and Staffordshire;Herefordshire, Worcestershire and Warwickshire",
    "West Midlands": "West Midlands",
    "West Yorkshire": "West Yorkshire",
    "Wiltshire": "Gloucestershire and Wiltshire",
    "Action Fraud": "UK",
    "CIFAS": "UK",
    "UK Finance": "UK",
}

updated_df["ITL2 region"] = updated_df["Force Name"].map(ITL_2_matches) # Mapping the ITL2 regions if we would like them
# print(updated_df.head(3)) # Checking to make sure it ran correctly
# updated_df["ITL2 region"] = updated_df["ITL2 region"].apply(lambda x: x.split(";"))
print(updated_df.info())

updated_df.to_csv("CLEANED-regional_forces_crime_data_2024-2025.csv")



national_forces = updated_df[updated_df["ITL1 region"] == "UK"]
national_forces.reset_index(inplace=True)
# national_forces.to_csv("CLEANED-national_forces_crime_data_2024-2025.csv") # Creating new data set

print(updated_df.info())
# Removing from regional data set
updated_df.loc[updated_df["ITL1 region"] == "UK", "ITL1 region"] = None # Making this null values so I can remove the data
updated_df.dropna(inplace=True) # Removing UK data
print(updated_df.info()) # Checking to make sure it has removed
print(updated_df[updated_df["ITL1 region"] == "UK"]) # DOuble checking there are no more of these rows

#ITL2 scatter graph
updated_df["ITL2 region"] = updated_df["ITL2 region"].apply(lambda x: x.split(";")) # This converts the values into a list so that I can find all of their IMD ratings
# print(crime_df["ITL2"])
individual_ITL2 = updated_df.explode("ITL2 region")

regional_summary = individual_ITL2.groupby("ITL2 region").agg( # Now I will find the average IMD score per ITL2 region
    total_offences = ("Number of Offences", "sum"))
regional_summary.to_csv("machine_learning\machine_learning_test.csv")
