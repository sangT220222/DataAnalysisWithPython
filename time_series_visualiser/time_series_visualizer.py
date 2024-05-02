import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("/workspace/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv",index_col='date', parse_dates=True)
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
# print(df)

def draw_line_plot():
    #making a copy of dataframe
    df_for_line = df
    #defining the figure and the size of the subplot
    fig, ax = plt.subplots(figsize=(20, 8))
    # Draw line plot
    line = ax.plot(df_for_line)

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Group by month and year, and calculate the mean of other columns
    df_bar = df_bar.resample('M').mean()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    labels = [i for i in range(2016, 2020)] 
    data_dict={'Year': labels} #we will have {'Year' : 2016, 'Year': 2017 etc}
    
    #collects data for each month and year combination from a DataFrame
    #,handles missing data by appending 0s, 
    # and stores the collected data in a dictionary with the month index as the key.
    for index, month in enumerate(months):            
        month_data = []
        for i in labels:
            try:
                month_data.append(df_bar['{}-{}'.format(i, index+1)].iloc[0]['value'])
            except KeyError:
                month_data.append(0)
        data_dict[index] = month_data
    
    df_bar = pd.DataFrame(data_dict)
    df_bar.columns = ["Year"] + months
    # Draw bar plot
    pos = list(range(len(df_bar['Year'])))
    width = 0.05
    fig, ax = plt.subplots(figsize=(10, 8))
    for q in range(12): #looping through 12 months
        plt.bar([p + width*q for p in pos], df_bar[months[q]], width)
    #[p + width*q for p in pos] generates a list of x-axis positions for the bars. For each position p in the list pos, it calculates the position for the current month's bars by adding width*q, where width is the width of each bar and q is the index of the current month.
    #df_bar[months[q]] retrieves the data for the current month from the DataFrame df_bar. months[q] is the name of the current month.
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    
    ax.set_xticks([p + 5 *width for p in pos])
    ax.set_xticklabels(df_bar['Year'])
    plt.legend(months, title='Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
