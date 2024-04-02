import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x= pd.Series(df["Year"])
    y= df["CSIRO Adjusted Sea Level"]
    fig, ax = plt.subplots()
    plt.scatter(x, y, alpha= 0.5)

    # Create first line of best fit
    reg= linregress (x= x, y=y)
    x_to2050 = pd.Series([i for i in range (1880,2051)])
    y_pred2050 = reg.intercept + reg.slope * x_to2050

    # Create second line of best fit
    x_from2000 = x.copy()
    x_from2000 = x_from2000.loc[120:]
    y_from2000 = y.copy()
    y_from2000 = y_from2000.loc[120:]
    reg_2000= linregress (x= x_from2000, y=y_from2000)
    ## For that I need to select only the years from 2000
    x_2000to2050 = pd.Series([i for i in range (2000,2051)])
    y_predfrom2000 = reg_2000.intercept + reg_2000.slope * x_2000to2050

    # Add labels and title
    plt.scatter(x=x, y=y, alpha= 0.5)
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    plt.plot(x_to2050, y_pred2050, '--r')
    plt.plot(x_2000to2050, y_predfrom2000, '-g')
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()