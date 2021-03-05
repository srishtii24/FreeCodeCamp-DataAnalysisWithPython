import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = lr.slope
    intercept = lr.intercept
    
    df_2 = df[df['Year']>=2000]
    lr_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    slope_2 = lr_2.slope
    intercept_2 = lr_2.intercept

    # Create scatter plot
    fig, ax = plt.subplots()
    fig.set_size_inches(12,12)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='green')
    
    # Create first line of best fit
    x = range(1880, 2050)
    y = slope * x + intercept
    ax.plot(x, y, color='red')

    # Create second line of best fit
    x_2 = range(2000, 2050)
    y_2 = slope_2 * x_2 + intercept_2
    ax.plot(x_2, y_2, color='blue')

    # Add labels and title
    ax.set(title="Rise in Sea Level")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()