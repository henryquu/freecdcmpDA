import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (df['height'] / 100)**2
df['overweight'] = (bmi > 25).astype(int) 

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=('cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'))


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)

    
    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')


    # Get the figure for the output
    fig = graph.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    df_heat = df.drop(df[df['ap_lo'] <= df['ap_hi']].index)

    df_heat.drop(df_heat[df_heat['height'] < df_heat['height'].quantile(0.025)].index, inplace=True)
    df_heat.drop(df_heat[df_heat['height'] > df_heat['height'].quantile(0.975)].index, inplace=True)

    df_heat.drop(df_heat[df_heat['weight'] < df_heat['weight'].quantile(0.025)].index, inplace=True)
    df_heat.drop(df_heat[df_heat['weight'] > df_heat['weight'].quantile(0.975)].index, inplace=True)

    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = (np.triu(corr)).astype(bool)


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()