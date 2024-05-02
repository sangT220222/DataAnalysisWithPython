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


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
