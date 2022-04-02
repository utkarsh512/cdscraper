"""
cli.py - Command line interface for scraping
"""

from tqdm import tqdm
import argparse
import json
import concurrent.futures
from . import profile

MAX_THREADS = 30


def options():
    """
    Parse arguments
    """
    ap = argparse.ArgumentParser(
        prog='cdscraper',
        usage='python3 %(prog)s [options]',
        description='cdscraper - Scraping Create Debate'
    )
    ap.add_argument('-i', '--input', type=str, required=True, help='path to txt file containing usernames')
    ap.add_argument('-o', '--output', type=str, required=True, help='path for output')
    args = ap.parse_args()
    return args


def run(usernames, filename):
    """
    Run the profile scraper concurrently
    """
    with open(filename, 'w', encoding='utf-8') as f:
        threads = min(MAX_THREADS, len(usernames))
        length = len(usernames)

        with tqdm(total=length) as pbar:
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                futures = {executor.submit(profile.get_profile, arg): arg for arg in usernames}
                for future in concurrent.futures.as_completed(futures):
                    arg = futures[future]
                    res = future.result()
                    if res is not None:
                        f.write(json.dumps(res) + '\n')
                    pbar.update(1)


def main():
    """
    main
    """
    args = options()
    with open(args.input, 'r', encoding='utf-8') as f:
        usernames = [user.strip() for user in f.readlines()]
    results = run(usernames, args.output)


def run_as_command():
    """Run from command line"""
    main()


if __name__ == '__main__':
    main()
