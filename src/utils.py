from typing import Union
from datetime import datetime


def save_to_csv(data, filename):
    import pandas as pd
    # Function to save data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)  # Save DataFrame to CSV without the index


def append_jsonl_gz(path, records, batch_size=1000):
    """Append an iterable of dict records to a gzip-compressed JSONL file.

    Writes in batches for efficiency. `records` can be any iterable of dicts.
    The function opens the gzip file in text-append mode so existing data is
    preserved and new gzip members are appended (Python's gzip supports
    concatenated members on read).
    """
    import gzip
    import json

    buf = []
    for r in records:
        buf.append(json.dumps(r, ensure_ascii=False))
        if len(buf) >= batch_size:
            with gzip.open(path, 'at', encoding='utf-8') as f:
                f.write('\n'.join(buf) + '\n')
            buf = []
    if buf:
        with gzip.open(path, 'at', encoding='utf-8') as f:
            f.write('\n'.join(buf) + '\n')

def to_timestamp(value: Union[int, float, str, datetime]) -> int:
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, datetime):
        return int(value.timestamp())
    # assume ISO date string like "2022-01-01"
    return int(datetime.fromisoformat(value).timestamp())