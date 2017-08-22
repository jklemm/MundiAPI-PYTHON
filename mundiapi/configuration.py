# -*- coding: utf-8 -*-

"""
   mundiapi.configuration

   This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from .api_helper import APIHelper

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://api.mundipagg.com/core/v1'

    # The username to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_user_name = "TODO: Replace"

    # The password to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_password = "TODO: Replace"

