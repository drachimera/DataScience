from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout

plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])

#note iplot is the plot we use in ipython notebooks! e.g.
#init_notebook_mode(connected=True)
#iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])
