import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")

# Add 'overweight' column
df["overweight"] = ((df["weight"] / ((df["height"]/100) ** 2)) > 25).astype(int)
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0 #used loc to filter the rows based on the condition given
df.loc[df['gluc'] == 1, 'gluc'] = 0

df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars= 'cardio',value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])
    #create a DataFrame where the categorical variables are melted into a single column with the corresponding values
    #print(df_cat)

    # Group and reformat the data to split it by 'cardio'. 
    #Show the counts of each feature. #
    # Group by 'cardio' and the variable column, then count the occurrences
    grouped_df = pd.DataFrame(df_cat.groupby(['cardio','variable','value'],as_index=True)['value'].count())
    # Rename the 'variable' column to 'feature' to work correctly with catplot
    grouped_df = grouped_df.rename(columns= {'value': 'total'})
    #print(grouped_df)

    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(x='variable', y = 'total', col = 'cardio', hue = 'value', data = grouped_df, kind = 'bar')

    fig.set_titles("Count of Features by Cardio")
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #filter data where we want ap_low is <= ap_hi
    #filter data to include rows of height value within 2.5% and 97.5% percentile
    #filter data to include rows of weight calue within 2.5% and 97.5% percentile
    df_heat = df_heat = df.loc[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) & (df["weight"] <= df["weight"].quantile(0.975))]
    # print(df_heat)
    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(13, 10))

    # Draw the heatmap with 'sns.heatmap()'
    # annot shows the numbers on each cell
    # fmt formats the number, here it's one decimal place
    #center = 0 means the numbers will be mapped into center of cell
    sns.heatmap(corr, mask = mask, annot = True,linewidths=.5, vmin = -.16, vmax = .32, fmt=".1f", center=0 )
    plt.title('Correlation Matrix')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
