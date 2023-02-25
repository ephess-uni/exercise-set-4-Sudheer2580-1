""" sudheer
Module 4
"""

from datetime import datetime


def logstamp_to_datetime(datestr):
    """ Function 2"""
    input_str = datestr
    format_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(input_str, format_str)
