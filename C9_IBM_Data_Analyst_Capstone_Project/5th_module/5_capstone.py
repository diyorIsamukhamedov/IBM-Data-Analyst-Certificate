# %%
import pandas as pd

# Load CSV into DataFrame
df = pd.read_csv("4_survey_data_prepared.csv")

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

# ====================== Current Technology Usage ======================
# ===================================================================================================
# %%
df.drop(columns=['Unnamed: 0'], inplace=True)

# %%
import matplotlib.pyplot as plt

# %%
# Split multiple languages in each row into separate rows
lang_series = df['LanguageHaveWorkedWith'].str.split(';').explode()

# Count occurrences and select Top 10 languages
top10_langs = lang_series.value_counts().head(10)

# Create bar chart
plt.figure(figsize=(10,6))
bars = plt.bar(top10_langs.index, top10_langs.values, color='skyblue')

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, str(height),
             ha='center', va='bottom', fontsize=10)

# Add chart title
plt.title('Top 10 Programming Languages (Have Worked With)', fontsize=14)

# Add axis labels
plt.xlabel('Programming Languages')
plt.ylabel('Number of Respondents')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Top 10 databases
top10_db = df['DatabaseHaveWorkedWith'].str.split(';').explode().value_counts().head(10)

# Column chart
bars = plt.bar(top10_db.index, top10_db.values, color='lightgreen')

# Show value labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(bar.get_height()), ha='center', va='bottom')

# Title
plt.title('Top 10 Databases (Have Worked With)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Number of Respondents')
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
!pip install wordcloud
from wordcloud import WordCloud

# Top 10 platforms
top10_platforms = df['PlatformHaveWorkedWith'].str.split(';').explode().value_counts().head(10)

# Word cloud
wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top10_platforms)

# Show word cloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Top 10 Platforms (Have Worked With)')
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
import plotly.express as px

# Top 10 web frameworks
top10_web = df['WebframeHaveWorkedWith'].str.split(';').explode().value_counts().head(10)

# Bubble chart (circles)
fig = px.scatter(top10_web, 
                 x=top10_web.index, 
                 y=[0]*len(top10_web),  # все пузырьки на одной линии
                 size=top10_web.values, 
                 color=top10_web.index,
                 text=top10_web.index,
                 title="Top 10 Web Frameworks (Have Worked With)")

fig.update_traces(textposition='top center')
fig.update_yaxes(visible=False)  # скрыть ось Y
fig.update_xaxes(visible=False)  # скрыть ось X
fig.show()
# ===================================================================================================

# ===================================================================================================

# ====================== Future Technology Trend ======================
# ===================================================================================================
# %%
# Top 10 languages
top10_lang_want = df['LanguageWantToWorkWith'].str.split(';').explode().value_counts().head(10)

# Bar chart
bars = plt.bar(top10_lang_want.index, top10_lang_want.values, color='orange')

# Value labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(bar.get_height()), ha='center', va='bottom')

# Title
plt.title('Top 10 Programming Languages (Want To Work With)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Number of Respondents')
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Top 10 databases
top10_db_want = df['DatabaseWantToWorkWith'].str.split(';').explode().value_counts().head(10)

# Column chart
bars = plt.bar(top10_db_want.index, top10_db_want.values, color='teal')

# Value labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(bar.get_height()), ha='center', va='bottom')

# Title
plt.title('Top 10 Databases (Want To Work With)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Number of Respondents')
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Top 10 platforms
top10_platform_want = df['PlatformWantToWorkWith'].str.split(';').explode().value_counts().head(10)

# Treemap chart
fig = px.treemap(
    names=top10_platform_want.index,
    parents=[""] * len(top10_platform_want),
    values=top10_platform_want.values,
    color=top10_platform_want.values,
    title="Top 10 Platforms (Want To Work With)"
)

fig.update_traces(textinfo="label+value")  # contrast labels
fig.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Top 10 web frameworks
top10_web_want = df['WebframeWantToWorkWith'].str.split(';').explode().value_counts().head(10)

# Bubble chart
fig = px.scatter(top10_web_want,
                 x=top10_web_want.index,
                 y=[0]*len(top10_web_want),
                 size=top10_web_want.values,
                 color=top10_web_want.index,
                 title="Top 10 Web Frameworks (Want To Work With)",
                 text=top10_web_want.index)

fig.update_traces(textposition='top center')
fig.update_xaxes(visible=False)
fig.update_yaxes(visible=False)
fig.show()
# ===================================================================================================

# ====================== Demographics  ======================
# ===================================================================================================
# %%
# Age mapping for correct order
age_order = {
    'Under 18 years old': 1,
    '18-24 years old': 2,
    '25-34 years old': 3,
    '35-44 years old': 4,
    '45-54 years old': 5,
    '55-64 years old': 6,
    '65 years or older': 7,
    'Prefer not to say': 8
}

# Count respondents by Age
age_counts = df['Age'].value_counts().sort_index(key=lambda x: x.map(age_order))

# Pie chart without labels
plt.figure(figsize=(8,6))
wedges, _, autotexts = plt.pie(
    age_counts,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors
)

# Legend with labels + percentages
labels = [f"{cat}: {val} ({pct.get_text()})" 
          for cat, val, pct in zip(age_counts.index, age_counts.values, autotexts)]
plt.legend(wedges, labels, title="Age Groups", loc="center left", bbox_to_anchor=(1,0.5))

plt.title('Respondent Distribution by Age', fontsize=14, weight='bold')
plt.show()
# ===================================================================================================

# ===================================================================================================

# %%
# Count respondents by country
country_counts = df['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

# Map chart
fig = px.choropleth(country_counts,
                    locations="Country",
                    locationmode="country names",
                    color="Count",
                    title="Respondent Count by Country")

fig.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Count respondents by Education Level
edu_counts = df['EdLevel'].value_counts()

# Line chart
plt.plot(edu_counts.index, edu_counts.values, marker='o')

# Value labels
for x, y in zip(edu_counts.index, edu_counts.values):
    plt.text(x, y, str(y), ha='center', va='bottom')

# Title and labels
plt.title('Respondent Distribution by Formal Education Level')
plt.xlabel('Education Level')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45, ha='right')
plt.show()
# ===================================================================================================

# ===================================================================================================

# ===================================================================================================

# %%
# Group data by Age and Education Level, count number of respondents
age_edu_counts = df.groupby(['Age', 'EdLevel'])['ResponseId'].count().unstack(fill_value=0)

# Create stacked bar chart
ax = age_edu_counts.plot(kind='bar', stacked=True, figsize=(10,6))

# Add value labels inside each bar section
for container in ax.containers:
    ax.bar_label(container, label_type='center')

# Add chart title and axis labels
plt.title('Respondent Count by Age, classified by Education Level')
plt.xlabel('Age')
plt.ylabel('Number of Respondents')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add legend to show Education Level
plt.legend(title='Education Level')

# Show the final chart
plt.show()
# ===================================================================================================