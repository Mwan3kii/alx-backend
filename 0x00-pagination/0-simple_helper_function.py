#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing the start index and end index
    corresponding to the range of indexes to return in a list for the given
    pagination paraments
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
