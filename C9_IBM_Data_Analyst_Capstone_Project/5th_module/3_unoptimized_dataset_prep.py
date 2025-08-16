# %%
import pandas as pd

# ===================================================================================================
# Working with these key columns from the survey dataset
columns_of_interest = [
    'ResponseId',              # Unique identifier for each respondent
    'Age',                     # Respondent's age
    'Country',                 # Respondent's country
    'EdLevel',                 # Formal education level
    'LanguageHaveWorkedWith',  # Programming languages the respondent has experience with
    'DatabaseHaveWorkedWith',  # Databases the respondent has experience with
    'PlatformHaveWorkedWith',  # Platforms the respondent has experience with
    'WebframeHaveWorkedWith',  # Web frameworks the respondent has experience with
    'LanguageWantToWorkWith',  # Programming languages the respondent wants to work with
    'DatabaseWantToWorkWith',  # Databases the respondent wants to work with
    'PlatformWantToWorkWith',  # Platforms the respondent wants to work with
    'WebframeWantToWorkWith'   # Web frameworks the respondent wants to work with
]
# ===================================================================================================

# Load CSV using only the selected columns
df = pd.read_csv("2_survey_data_updated.csv", usecols=columns_of_interest)

df.head()
# ===================================================================================================

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# ===================================================================================================

# ===================================================================================================
# My automatized get_summary_stats function
def get_summary_stats(df):
    """
    Returns summary statistics for each column in the DataFrame.
    """
    return pd.DataFrame({
        "Column name": df.columns,  # Column names
        "DataType": df.dtypes.values,  # Data types of columns
        "Number of rows": df.shape[0],  # Total number of rows
        "Number of columns": df.shape[1],  # Total number of columns
        "Not-Null Columns": df.notnull().sum().values,  # Count of non-missing values
        "Missing Count": df.isnull().sum().values,  # Count of missing values
        "Missing Percentage": (df.isnull().mean() * 100).values  # Percentage of missing values
    })

summary_stats = get_summary_stats(df)

# # Print the summary statistics
print(summary_stats)
# ===================================================================================================

# Display unique values of all columns
# for col in columns_of_interest:
#     unique_vals = df[col].dropna().unique()
#     print(f"Unique values in '{col}':")
#     print(unique_vals)
#     print("-" * 50) # Incrementing dashes 50 times. I found it cool ;)

# ===================================================================================================

# %%
# Map long country names to short names
country_mapping = {
    'United Kingdom of Great Britain and Northern Ireland': 'UK',
    'United States of America': 'USA',
    'Republic of North Macedonia': 'North Macedonia',
    'United Republic of Tanzania': 'Tanzania',
    'Russian Federation': 'Russia',
    'Viet Nam': 'Vietnam',
    'Venezuela, Bolivarian Republic of...': 'Venezuela',
    'Hong Kong (S.A.R.)': 'Hong Kong',
    'Iran, Islamic Republic of...': 'Iran',
    'Democratic Republic of the Congo': 'DR Congo',
    'Republic of Korea': 'South Korea',
    'Côte d\'Ivoire': 'Ivory Coast',
    'Congo, Republic of the...': 'Congo'
    # Add other countries as needed
}

# Replace long country names with short names
df['Country'] = df['Country'].replace(country_mapping)

# Check unique values after mapping
# display(df['Country'].unique())
#print(df['Country'].unique())
# ===================================================================================================

# %%
# Map long education levels to short names
edlevel_mapping = {
    "Bachelor's degree (B.A., B.S., B.Eng., etc.)": "Bachelor's",
    "Master's degree (M.A., M.S., M.Eng., MBA, etc.)": "Master's",
    'Professional degree (JD, MD, Ph.D, Ed.D, etc.)': 'Professional',
    'Some college/university study without earning a degree': 'Some College',
    'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 'Secondary',
    'Associate degree (A.A., A.S., etc.)': 'Associate',
    'Something else': 'Other',
    'Primary/elementary school': 'Primary'
    # Add other education level as needed
}

# Replace long education levels with short names
df['EdLevel'] = df['EdLevel'].replace(edlevel_mapping)

# Check unique values after mapping
#display(df['EdLevel'].unique())
#print(df['EdLevel'].unique())
# ===================================================================================================

# ===================================================================================================
# My automatized split_and_explode function
# (Function to split a semicolon-separated column and explode it into multiple rows)

def split_and_explode(df, column, sep=';'):
    """
    Split a column by a separator and explode it into multiple rows.
    Also strips leading/trailing spaces from each element.

    df: input DataFrame
    column: name of the column to split & explode
    sep: separator to split the string (default: ';')
    """
    df_copy = df.copy()
    df_copy[column] = df_copy[column].str.split(sep) # Split the column by separator
    df_copy = df_copy.explode(column)                # Explode the list into multiple rows
    df_copy[column] = df_copy[column].str.strip()    # Remove leading/trailing spaces
    
    return df_copy
# ===================================================================================================

# ===================================================================================================

# Explode multiple-choice columns to make one value per row
columns_to_explode = [
    'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith', 'PlatformHaveWorkedWith', 'WebframeHaveWorkedWith',
    'LanguageWantToWorkWith', 'DatabaseWantToWorkWith', 'PlatformWantToWorkWith', 'WebframeWantToWorkWith'
]

for col in columns_to_explode:
    df = split_and_explode(df, col)
    print(f"Unique values in '{col}' after explode:")
    print(df[col].unique())
# ===================================================================================================

print(df.memory_usage(deep=True).sum() / 1024**2, "MB")

# Save transformed data
df.to_csv('5_survey_data_prepared.csv')
# ===================================================================================================