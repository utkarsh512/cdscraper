"""
constants.py - global constants used
"""

BASE_URL = 'https://www.createdebate.com'

# to be used as USER_URL.format(username)
USER_URL = 'https://www.createdebate.com/user/viewprofile/{0}'

# to be used as USER_PROPERTY_URL.format(username, property, offset)
# Note: `offset` must be a multiple of 96
USER_PROPERTY_URL = 'https://www.createdebate.com/browse/users/{0}/{1}/points/alltime/{2}/96'
