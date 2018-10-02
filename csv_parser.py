import matplotlib.pyplot as plt
import pandas as pd
import click

#plt.ion()
#def read_csv():
#    filename = 'oktoberfestgesamt19852016.csv'
#    df = pd.read_csv(filename)
#    return df
@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Display the column names and their data types"""
    df = pd.read_csv(filename)
    print(df.dtypes)

@cli.command()
@click.argument('filename') 
@click.option('--column', default=None, help='Name of column to plot. If not used, all will be plotted.')
def plot(filename, column):
    """Plots histogram of a columns to the csv file"""
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df[column].hist()
        plt.title(column)
    plt.show()

    
#display_columns()
#plot_hist()

if __name__ == '__main__':
    cli()
    #display_columns()
    #import sys
    #print(sys.argv)
    #filename = sys.argv[1]
    #display_columns(filename)
    #plot_hist(filename)
    #while True:
        #pass