import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

mpl.rcParams["font.size"] = 20

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

# Clean data

df = df[df['value'] > df['value'].quantile(0.025)]
df = df[df['value'] < df['value'].quantile(0.975)]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(kind='line', figsize=(20,8), legend=False, color='red', xlabel='Date', ylabel='Page Views')
    fig.set_title(f"Daily freeCodeCamp Forum Page Views {df.index[0].strftime('%m/%Y')}-{df.index[-1].strftime('%m/%Y')}")

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month_name()
    df_bar.index = df_bar.index.strftime('%Y')

    df_bar.reset_index(inplace=True)

    df_bar = df_bar.groupby(['date', 'month']).mean().unstack()
    df_bar.columns = df_bar.columns.droplevel().values
    
    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(14,14))
    fig.set_xlabel('Years')
    fig.set_ylabel('Average Page Views')

    fig = fig.figure
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
    fig, axs = plt.subplots(ncols=2, figsize=(28,10))

    sns.boxplot(data=df_box, x='year', y='value', ax=axs[0], palette="tab10")
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_ylabel('Page views')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', ax=axs[1], palette="tab10", order=months)
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_ylabel('Page views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()