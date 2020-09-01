from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.tools as tls
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import urllib2

df = pd.read_csv("gapminderDataFiveYear.txt", sep='\t')
#print(len(df['year'].unique()))

# number of countries for each year in the dataframe is: 
for year, X in df.groupby('year'):
   print(year, len(X['country']))

# minimum and maximum values of the x and y variables are:
df['gdpPercap'].min(), df['gdpPercap'].max()
df['lifeExp'].min(), df['lifeExp'].max()

# Set plot and axis titles
title = "Fig 7.3a: Animated Hans Rosling bubble chart"  # plot's title
x_title = "Gross Domestic Product per Capita [in USD of the year 2000]"
y_title = "Life Expentancy [in years]"

# Define a dictionary of axis style options
axis_style = dict(
    zeroline=False,       # remove thick zero line
    gridcolor='#FFFFFF',  # white grid lines
    ticks='outside',      # draw ticks outside axes 
    ticklen=8,            # tick length
    tickwidth=1.5         #   and width
)


# Initialize layout object
layout = go.Layout(
    title=title,  # set plot title
    xaxis=go.XAxis(
        axis_style,            # add style options
        title=x_title,         # set x-axis title
        range=[-0.9e4,1.15e5]  # set range
    ),
    yaxis=go.YAxis(
        axis_style,            # add style options
        title=y_title,         # y-axis title
        range=[21,89]          # set range
    ),
    showlegend=False,         # remove legend (info in hover)
    hovermode='closest',      # (!) hover -> closest data pt
    plot_bgcolor='#EFECEA',   # set plot color to grey
    autosize=False,  # turn off autosize
    width=650,       # plot width
    height=500,      # plot height
)

def regenData():
	N = 1000
	random_x = np.random.randn(N)
	random_y = np.random.randn(N)

	# Create a trace
	trace = go.Scatter(
	    x = random_x,
	    y = random_y,
	    mode = 'markers'
	)
	return trace

for x in range(0, 3):
	trace = regenData()
	data = [trace]
	plotly.offline.plot(data, filename='basic-scatter.html')
