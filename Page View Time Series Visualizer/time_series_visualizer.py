import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 5)
    plt.plot(df['date'], df['value'], color='r')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"]= df_bar['date'].dt.month
    df_bar["year"]= df_bar['date'].dt.year
    df_bar_grouped = df_bar.groupby(["year","month"])["value"].mean().unstack()

    # Draw bar plot
    ax = df_bar_grouped.plot.bar(figsize=(14,5))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(labels = [d for d in pd.to_datetime(df_bar_grouped.columns, format='%m').month_name()])

    fig = ax.get_figure()
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
    fig, axes = plt.subplots(nrows = 1, ncols =2 )
    fig.set_size_inches(15, 5)
    axes[0].set(title="Year-wise Box Plot (Trend)")
    axes[1].set(title="Month-wise Box Plot (Seasonality)")

    sns.boxplot(y=df_box['value'], x=df_box['year'], ax=axes[0])
    sns.boxplot(y=df_box['value'], x=df_box['month'], 
                order= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=axes[1])

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
