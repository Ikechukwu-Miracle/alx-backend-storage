#!/usr/bin/python3
"""Module for using PyMongo"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection: PyMongo collection object.
        topic (string): Topic to search.

    Returns:
        A list of schools having the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
