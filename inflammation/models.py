"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):  
    """Load comma-separated numeric data from a CSV file.

    The CSV is expected to store one patient's daily measurements per row.

    :param filename: Path to the CSV file to load.
    :returns: The loaded data as a NumPy array.
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the mean inflammation value for each day.

    The mean is taken across patients (axis 0), producing one value per day.

    :param data: Two-dimensional array with patients in rows and days in columns.
    :returns: One mean value for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Find the maximum inflammation value for each day.

    The maximum is taken across patients (axis 0), producing one value per day.

    :param data: Two-dimensional array with patients in rows and days in columns.
    :returns: One maximum value for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Find the minimum inflammation value for each day.

    The minimum is taken across patients (axis 0), producing one value per day.

    :param data: Two-dimensional array with patients in rows and days in columns.
    :returns: One minimum value for each day.
    """
    return np.min(data, axis=0)

