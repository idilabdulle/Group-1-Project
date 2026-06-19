import pandas as pd
import numpy as np
import statistics 
import openpyxl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

crime_df = pd.read_csv("CLEANED-regional_forces_crime_data_2024-2025.csv")
imd_df = pd.read_csv("clean_index_of_multiple_deprivation.csv")

# print(crime_df.columns)
# print(imd_df.columns)

crime_df.rename(columns={"ITL1 region": "ITL1", "ITL2 region": "ITL2"}, inplace=True)

ITL1_grouped_crimes = crime_df.groupby("ITL1")["Number of Offences"].sum()
print(ITL1_grouped_crimes)

# print(crime_df.columns)
# crime_and_imd_df_df = pd.merge(crime_df, imd_df, on="ITL2", how="outer")

# print(crime_and_imd_df_df.info())
