import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x = df['Year'].values, y = df['CSIRO Adjusted Sea Level'].values)
    # Create first line of best fit

    #Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    #Plot the line of best fit over the top of the scatter plot. 
    #Make the line go through the year 2050 to predict the sea level rise in 2050.
    slope, y_intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    firstLineX = range(df['Year'][0], 2050)
    firstLineY = firstLineX * slope + y_intercept
    #plotting regression line
    plt.plot(firstLineX, firstLineY, color='red')

    # Create second line of best fit
    #Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset.
    #Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues 
    #as it has since the year 2000.
    df2  = df[(df['Year'] >= 2000)]
    #reset index so we are able to get the first row in line 30
    df2.reset_index(drop=True, inplace=True)
    slope2, y_intercept2, _, _, _ = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    secondLineX = range(df2['Year'][0], 2050)
    secondLineY = secondLineX * slope2 + y_intercept2
    
    plt.plot(secondLineX, secondLineY, color='green')


    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
