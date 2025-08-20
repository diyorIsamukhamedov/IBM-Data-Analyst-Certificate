# ===================================================================================================
# %%
# Import necessary libraries
!pip install pandas
!pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# ===================================================================================================

# ===================================================================================================
# Load job postings data
job_df = pd.read_excel('job-postings-technologies.xlsx')

# Sort by number of postings
job_df = job_df.sort_values(by="Number of Job Postings", ascending=False)

# Plot bar chart
plt.bar(job_df['Technology'], job_df['Number of Job Postings'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Job Postings by Technology")
plt.ylabel("Number of Postings")
plt.show()
# ===================================================================================================

# ===================================================================================================
# %%
# Load CSV
df = pd.read_csv("popular-languages.csv")

# Clean salary column (remove $ and , then convert to int)
df["Average Annual Salary"] = df["Average Annual Salary"].replace('[\\$,]', '', regex=True).astype(int)

# Sort by salary
df = df.sort_values(by="Average Annual Salary", ascending=False)

# Bar chart
bars = plt.bar(df["Language"], df["Average Annual Salary"], color="orange")

# Value labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             str(bar.get_height()), ha="center", va="bottom")

# Title and labels
plt.title("Popular Languages by Average Annual Salary")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Average Annual Salary (USD)")
plt.show()
# ===================================================================================================