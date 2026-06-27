"""
Create the cleaned Wellness_Data workbook from the raw ONS workbook.
Input: ukmeasuresofnationalwellbeingfeb20251.xlsx
Output: Wellness_Data.xlsx

This script extracts the regional tables used in the project, keeps only the
columns needed for analysis, renames them to clear Python-friendly names, and
saves each cleaned measure to its own sheet.
"""

from pathlib import Path
import pandas as pd

RAW_FILE = Path("ukmeasuresofnationalwellbeingfeb20251.xlsx")
OUTPUT_FILE = Path("Wellness_Data.xlsx")

# Each entry has output sheet name, raw ONS sheet name, first data row in Excel, number of rows,
# and the raw Excel columns to keep.

SHEETS_TO_CLEAN = [
    {
        "output_sheet": "Sheet1",
        "raw_sheet": "1.1_Life_satisfaction",
        "start_row": 75,
        "nrows": 13,
        "columns": {1: "Region", 2: "Low_Life_Satisfaction_Percentage"},
    },
    {
        "output_sheet": "Sheet2",
        "raw_sheet": "1.2_Worthwhile",
        "start_row": 75,
        "nrows": 13,
        "columns": {1: "Region", 2: "Low_Worthwhileness_Percentage"},
    },
    {
        "output_sheet": "Sheet3",
        "raw_sheet": "1.3_Happiness",
        "start_row": 75,
        "nrows": 13,
        "columns": {1: "Region", 2: "Low_Happiness_Percentage"},
    },
    {
        "output_sheet": "Sheet4",
        "raw_sheet": "1.4_Feeling_anxious",
        "start_row": 75,
        "nrows": 13,
        "columns": {1: "Region", 2: "High_Anxiety_Percentage"},
    },
    {
        "output_sheet": "Sheet5",
        "raw_sheet": "2.1_Unhappy_partner_r'ships",
        "start_row": 30,
        "nrows": 13,
        "columns": {1: "Region", 2: "Unhappy_Relationships_Percentage"},
    },
    {
        "output_sheet": "Sheet6",
        "raw_sheet": "3.1_Healthy_life_expectancy",
        "start_row": 53,
        "nrows": 9,
        "columns": {
            1: "Region",
            2: "Male_Life_Expectancy_Years",
            5: "Female_Life_Expectancy_Years",
        },
    },
    {
        "output_sheet": "Sheet7",
        "raw_sheet": "3.3_Physical_health_cond'ns",
        "start_row": 26,
        "nrows": 9,
        "columns": {
            1: "Region",
            2: "Physical_Health_Conditions_Index",
            3: "Cancer_Index",
            4: "Cardiovascular_Conditions_Index",
            5: "Dementia_Index",
            6: "Diabetes_Index",
            7: "Kidney_And_Liver_Disease_Index",
            8: "Musculoskeletal_Conditions_Index",
            9: "Respiratory_Conditions_Index",
        },
    },
    {
        "output_sheet": "Sheet8",
        "raw_sheet": "3.4_Depression_or_anxiety",
        "start_row": 36,
        "nrows": 13,
        "columns": {1: "Region", 2: "Mild_To_Moderate_Depression_Or_Anxiety_Percentage"},
    },
    {
        "output_sheet": "Sheet9",
        "raw_sheet": "4.3_Time_spent_on_unpaid_work",
        "start_row": 29,
        "nrows": 13,
        "columns": {
            1: "Region",
            2: "Male_Daily_Unpaid_Work_Minutes",
            6: "Female_Daily_Unpaid_Work_Minutes",
        },
    },
    {
        "output_sheet": "Sheet10",
        "raw_sheet": "4.5_Engagement_arts_and_culture",
        "start_row": 33,
        "nrows": 9,
        "columns": {1: "Region", 2: "Engagement_With_Arts_Within_Year"},
    },
    {
        "output_sheet": "Sheet11",
        "raw_sheet": "4.6_Sports_participation",
        "start_row": 29,
        "nrows": 9,
        "columns": {1: "Region", 2: "Weekly_150_Minutes_Moderate_Intensity_Activity_Percentage"},
    },
    {
        "output_sheet": "Sheet12",
        "raw_sheet": "4.7_Visits_to_nature",
        "start_row": 72,
        "nrows": 10,
        "columns": {1: "Region", 2: "Green_And_Natural_Spaces_Visits_Within_Fortnight_Percentage"},
    },
    {
        "output_sheet": "Sheet13",
        "raw_sheet": "5.5_Crime",
        "start_row": 34,
        "nrows": 11,
        "columns": {1: "Region", 2: "Personal_Crime_Per_1000_Adults"},
    },
    {
        "output_sheet": "Sheet14",
        "raw_sheet": "5.6_Feeling_safe",
        "start_row": 35,
        "nrows": 12,
        "columns": {
            1: "Region",
            2: "Males_Who_Feel_Safe_Walking_Local_Area_Alone_After_Dark_Percentage",
            6: "Females_Who_Feel_Safe_Walking_Local_Area_Alone_After_Dark_Percentage",
        },
    },
    {
        "output_sheet": "Sheet15",
        "raw_sheet": "6.5_Gender_pay_gap",
        "start_row": 48,
        "nrows": 13,
        "columns": {
            1: "Region",
            2: "Gender_Pay_Gap_Residence_Percentage",
            3: "Gender_Pay_Gap_Workplace_Percentage",
        },
    },
    {
        "output_sheet": "Sheet16",
        "raw_sheet": "7.2_No_qualifications",
        "start_row": 41,
        "nrows": 13,
        "columns": {1: "Region", 2: "16_To_64_Year_Olds_No_Qualifications_Percentage"},
    },
    {
        "output_sheet": "Sheet17",
        "raw_sheet": "7.3_A-level_or_equiv_quals",
        "start_row": 23,
        "nrows": 13,
        "columns": {1: "Region", 2: "16_To_64_Year_Olds_At_Least_A-Levels_Percentage"},
    },
    {
        "output_sheet": "Sheet18",
        "raw_sheet": "8.1_Unemployment_rate",
        "start_row": 222,
        "nrows": 13,
        "columns": {1: "Region", 2: "Unemployed_Economically_Active_Adults_Percentage"},
    },
]


def clean_measure(raw_file: Path, config: dict) -> pd.DataFrame:
    """Extract and clean one regional table from the raw ONS workbook."""
    excel_cols = list(config["columns"].keys())
    pandas_cols = [col - 1 for col in excel_cols]

    df = pd.read_excel(
        raw_file,
        sheet_name=config["raw_sheet"],
        header=None,
        skiprows=config["start_row"] - 1,
        nrows=config["nrows"],
        usecols=pandas_cols,
    )

    df.columns = list(config["columns"].values())

    # Convert numeric-looking columns to numbers. Non-numeric values such as "NA"
    # are kept as text so nothing is silently lost. The ONS workbook uses "[u]"
    # for low-quality/unavailable values, but this project workbook used "NA".

    for column in df.columns:
        if column != "Region":
            df[column] = df[column].replace("[u]", "NA")
            converted = pd.to_numeric(df[column], errors="coerce")
            df[column] = converted.where(converted.notna(), df[column])

    return df


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {RAW_FILE}. Put this script in the same folder as the raw ONS workbook."
        )

    cleaned_sheets = {
        config["output_sheet"]: clean_measure(RAW_FILE, config)
        for config in SHEETS_TO_CLEAN
    }

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        for sheet_name, df in cleaned_sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Created {OUTPUT_FILE}")
    print(f"Cleaned {len(cleaned_sheets)} sheets from {RAW_FILE}")


if __name__ == "__main__":
    main()
