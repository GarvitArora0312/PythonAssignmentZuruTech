import json
import os
import argparse

def list_directory(directory, show_all=False):
    items = []
    for item in directory.get('contents', []):
        if not show_all and item['name'].startswith('.'):
            continue
        items.append(item['name'])
    return items

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='List directory contents.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('-a', '--all', action='store_true', help='Do not ignore entries starting with .')
    args = parser.parse_args()

    with open(args.json_file, 'r') as f:
        directory = json.load(f)

    items = list_directory(directory, show_all=args.all)
    print(' '.join(items)
