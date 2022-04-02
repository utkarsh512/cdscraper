"""
profile.py - Collecting profile details from Create-Debate
"""

import time
import requests
from bs4 import BeautifulSoup as bs
from .constants import (USER_URL, USER_PROPERTY_URL)


def get_profile(username: str) -> dict:
    """
    Collects details for given username

    :param username: unique username for given user
    """
    time.sleep(0.1)
    response = requests.get(USER_URL.format(username))
    soup = bs(response.text, 'html.parser')
    user_summary = soup.find_all('table')[0]
    reward_points, efficiency, n_arguments, n_debates = (cell.text for cell in user_summary.find_all('td')[1::2])
    user = dict(
        username=username,
        reward_points=int(reward_points),
        efficiency=int(efficiency[:-1]),
        n_arguments=int(n_arguments),
        n_debates=int(n_debates)
    )
    user['allies'] = get_property(user, 'allies')
    user['enemies'] = get_property(user, 'enemies')
    user['hostiles'] = get_property(user, 'hostiles')
    return user


def get_property(user_info: dict, tag: str, offset: int = 0) -> list:
    """Recursively finds neighbors under given tag

    :param user_info: dictionary containing user infomation
    :param tag: can take values 'allies', 'enemies' and 'hostiles'
    :param offset: should be a multiple of 96
    """
    response = requests.get(USER_PROPERTY_URL.format(user_info['username'], tag, offset))
    soup = bs(response.text, 'html.parser')
    neighbors = soup.find_all('div', {'class': 'userRow'})
    neighbors_name = [foo.findChildren('div', recursive=False)[1].a.text for foo in neighbors]
    if len(neighbors_name):
        neighbors_name.extend(get_property(user_info, tag, offset + 96))
    return neighbors_name


if __name__ == '__main__':
    # testing the module
    info = get_profile('excon')
    for k, v in info.items():
        print(k, v)
