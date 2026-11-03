"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict):
    """Plot and display each supplied daily statistic.

    Each dictionary entry creates a subplot labeled with its key and plots its
    values in order. The figure is displayed with Matplotlib.

    :param data_dict: Mapping of statistic names to one-dimensional data series.
    :returns: None.
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()
