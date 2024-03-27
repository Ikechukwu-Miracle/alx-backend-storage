#!/usr/bin/env python3
"""Pymongo"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        A list of students sorted by average score.
    """
    students = list(mongo_collection.find())
    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score

    sorted_students = sorted(students, key=lambda x: x['averageScore'], reverse=True)
    return sorted_students
