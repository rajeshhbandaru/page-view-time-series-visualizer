from matplotlib import axes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df = df.set_index('date')


# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    """creating a line graph\n
    Returns:
       this function does create a line graph every time we call it
       it makes a figure of the graph at the end of the function\n
       by the return fig\n
    """

    # Draw line plot
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.plot(df.index, df['value'], color='r', linewidth=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """creating a bar graph\n
    Returns:
       this function does create a bar graph every time we call it
       it makes a figure of the graph at the end of the function\n
       by the return fig\n
    """
    df_bar = df.copy()
    df["month"] = df.index.month
    df["year"] = df.index.year
    df_bar = df.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot(kind="bar", legend=True, figsize=(15, 10)).figure
    plt.xlabel("Years", fontsize=10)
    plt.ylabel("Average Page Views", fontsize=10)
    # plt.xticks(rotation=30)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(fontsize=10, title="Months", labels=[
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
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

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1 = plt.subplot(1, 2, 1)
    sns.boxplot(y=df_box['value'], x=df_box['year'])
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title("Year-wise Box Plot (Trend)")

    ax2 = plt.subplot(1, 2, 2)
    sns.boxplot(y=df_box['value'], x=df_box['month'], order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
