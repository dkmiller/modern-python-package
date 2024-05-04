"""
Core functionality used throughout the package.
"""

import logging

log = logging.getLogger(__name__)


def inner_method(string: str, integer: int) -> str:
    """
    This method duplicates a string the specified number of times.
    """
    rv = string * integer
    log.info("Generated string %s", rv)
    return rv
