import argparse
import json
import os
import tempfile
from typing import List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--key',
        help='data key',
        required=True
    )
    parser.add_argument(
        '--value',
        help='data value',
    )
    return parser.parse_args()


def add_value(storage_path: str, key: str, value: str) -> None:
    with open(storage_path, 'r') as f:
        data = json.load(f)
    if key not in data:
        data[key] = []
    data[key].append(value)
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def get_values(storage_path: str, key: str) -> List[str]:
    with open(storage_path, 'r') as f:
        data = json.load(f)
    return data.get(key, [])


def init(storage_path: str) -> None:
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            json.dump({}, f)


if __name__ == "__main__":
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    init(storage_path)
    args = parse_args()
    if args.value is None:
        print(*get_values(storage_path, args.key), sep=', ')
    else:
        add_value(storage_path, args.key, args.value)
