#!/usr/bin/env python3
"""Defines a function that lists all document in a collection"""


def list_all(mongo_collection):
    """Returns a list of all documents"""
    return [document for document in mongo_collection.find()]
