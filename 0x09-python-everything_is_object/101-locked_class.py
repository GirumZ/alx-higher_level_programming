#!/usr/bin/python3
""" A module that defines a LockedClass."""


class LockedClass:
    """A class that only allows 'first_name' attribut"""
    __slots__ = ["first_name"]
