import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(df['Year'].min(), 2051)
    plt.plot(x, line.intercept + line.slope*x, 'r')

    # Create second line of best fit
    line2 = linregress(df.loc[df['Year'] >= 2000,'Year'], df.loc[df['Year'] >= 2000,'CSIRO Adjusted Sea Level'])
    x = range(2000, 2051)
    plt.plot(x, line2.intercept + line2.slope*x, 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()