"""Helpers for plots."""

import plotly
from matplotlib import pyplot as plt


def histograms(data, xlabel=None, ylabel=None, title=None):
    """Return a div containing an histogram from the data."""
    mpl_fig = plt.figure()
    plt.hist(data)
    if xlabel:
        plt.set_xlabel(xlabel)
    if ylabel:
        plt.set_ylabel(ylabel)
    if title:
        plt.set_title(title)
    return get_div_from_data(mpl_fig)


def line_plot(x, y=None):
    """Return a div containing a line plot from the data."""
    mpl_fig = plt.figure()
    if y is None:
        plt.plot(x)
    else:
        plt.plot(x, y)
    return get_div_from_data(mpl_fig)


def scatter_plot(x, y):
    """Return a div containing a scatter plot from the data."""
    mpl_fig = plt.figure()
    plt.scatter(x, y)
    return get_div_from_data(mpl_fig)


def get_div_from_data(mpl_fig):
    """Return a string with an HTML div containing the plotly chart from a matplotlib figure."""
    res = plotly.offline.plot_mpl(
        mpl_fig,
        include_plotlyjs=False,
        output_type='div',
        resize=True,
        image_height="100%", image_width="100%"
    )
    return res
