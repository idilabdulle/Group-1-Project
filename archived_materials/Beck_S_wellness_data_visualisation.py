import pandas as pd
import matplotlib.pyplot as plt

# Crime Data

crime_df = pd.read_csv("CLEANED-regional_forces_crime_data_2024-2025.csv")

crime_by_region_df = (
    crime_df
    .groupby("ITL1 region")["Number of Offences"]
    .sum()
    .reset_index()
)

crime_by_region_df["Region"] = (
    crime_by_region_df["ITL1 region"]
    .str.replace(" \\(England\\)", "", regex=True)
    .replace({"East": "East of England"})
)

print(crime_by_region_df)

# Life Expectancy

life_expectancy_df = pd.read_excel(
    "Wellness_Data.xlsx",
    sheet_name=5
)

crime_life_expectancy_df = pd.merge(
    crime_by_region_df,
    life_expectancy_df,
    on="Region",
    how="inner"
)

crime_life_expectancy_df["Average_Life_Expectancy"] = (
    crime_life_expectancy_df["Male_Life_Expectancy_Years"] +
    crime_life_expectancy_df["Female_Life_Expectancy_Years"]
) / 2

plt.scatter(
    crime_life_expectancy_df["Average_Life_Expectancy"],
    crime_life_expectancy_df["Number of Offences"]
)

plt.xlabel("Average Healthy Life Expectancy (Years)")
plt.ylabel("Number of Offences")
plt.title("Crime vs Average Healthy Life Expectancy")

for _, row in crime_life_expectancy_df.iterrows():
    plt.annotate(
        row["Region"],
        (
            row["Average_Life_Expectancy"],
            row["Number of Offences"]
        )
    )

plt.show()

life_expectancy_corr = crime_life_expectancy_df[
    "Average_Life_Expectancy"
].corr(
    crime_life_expectancy_df["Number of Offences"]
)

print(f"Average life expectancy correlation: {life_expectancy_corr:.3f}")

# Low Life Satisfaction

life_satisfaction_df = pd.read_excel(
    "Wellness_Data.xlsx",
    sheet_name=0
)

crime_life_satisfaction_df = pd.merge(
    crime_by_region_df,
    life_satisfaction_df,
    on="Region",
    how="inner"
)

plt.scatter(
    crime_life_satisfaction_df["Low_Life_Satisfaction_Percentage"],
    crime_life_satisfaction_df["Number of Offences"]
)

plt.xlabel("Low Life Satisfaction (%)")
plt.ylabel("Number of Offences")
plt.title("Crime vs Low Life Satisfaction")

for _, row in crime_life_satisfaction_df.iterrows():
    plt.annotate(
        row["Region"],
        (
            row["Low_Life_Satisfaction_Percentage"],
            row["Number of Offences"]
        )
    )

plt.show()

life_satisfaction_corr = crime_life_satisfaction_df[
    "Low_Life_Satisfaction_Percentage"
].corr(
    crime_life_satisfaction_df["Number of Offences"]
)

print(f"Low life satisfaction correlation: {life_satisfaction_corr:.3f}")


# Feeling Safe After Dark

safe_after_dark_df = pd.read_excel(
    "Wellness_Data.xlsx",
    sheet_name=13
)

safe_after_dark_df["Average_Safe_After_Dark"] = (
    safe_after_dark_df["Males_Who_Feel_Safe_Walking_Local_Area_Alone_After_Dark_Percentage"] +
    safe_after_dark_df["Females_Who_Feel_Safe_Walking_Local_Area_Alone_After_Dark_Percentage"]
) / 2

crime_safe_after_dark_df = pd.merge(
    crime_by_region_df,
    safe_after_dark_df,
    on="Region",
    how="inner"
)

plt.scatter(
    crime_safe_after_dark_df["Average_Safe_After_Dark"],
    crime_safe_after_dark_df["Number of Offences"]
)

plt.xlabel("Average Feeling Safe After Dark (%)")
plt.ylabel("Number of Offences")
plt.title("Crime vs Feeling Safe After Dark")

for _, row in crime_safe_after_dark_df.iterrows():
    plt.annotate(
        row["Region"],
        (
            row["Average_Safe_After_Dark"],
            row["Number of Offences"]
        )
    )

plt.show()

safe_after_dark_corr = crime_safe_after_dark_df[
    "Average_Safe_After_Dark"
].corr(
    crime_safe_after_dark_df["Number of Offences"]
)

print(f"Feeling safe after dark correlation: {safe_after_dark_corr:.3f}")

# Correlation Comparison

measures = [
    "Life Expectancy",
    "Low Life Satisfaction",
    "Safe After Dark"
]

correlations = [
    life_expectancy_corr,
    life_satisfaction_corr,
    safe_after_dark_corr
]

plt.figure(figsize=(8, 5))

plt.bar(
    measures,
    correlations
)

plt.ylabel("Correlation with Crime")
plt.title("Comparison of Wellness Measures")

plt.show()