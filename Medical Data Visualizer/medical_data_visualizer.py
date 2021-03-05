import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = 0
df.loc[df['weight']/((df['height']/100)**2)>25,'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1, 'cholesterol'] = 0
df.loc[df['cholesterol']!=0, 'cholesterol'] = 1
df.loc[df['gluc']==1, 'gluc'] = 0
df.loc[df['gluc']!=0, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco','cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='value')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat['value'] = df_cat['value'].astype('category')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', hue='value', kind='count', col='cardio', data=df_cat).set_axis_labels("variable", "total").fig



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                    (df['height'] >= df['height'].quantile(0.025)) & 
                    (df['height'] <= df['height'].quantile(0.975)) & 
                    (df['weight'] >= df['weight'].quantile(0.025)) & 
                    (df['weight'] <= df['weight'].quantile(0.975))
                ]

    # Calculate the correlation matrix
    corr = round(df_heat.corr(), 1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype('bool')



    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 10)

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, 
                vmin=-0.16, vmax=0.32, center= 0,
                linewidths=2, linecolor='white',
                cbar_kws={"shrink": 0.5}
               )



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
