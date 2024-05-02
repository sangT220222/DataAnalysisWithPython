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
    plt.plot(firstLineX, firstLineY, color='red', label='Regression line')
    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
