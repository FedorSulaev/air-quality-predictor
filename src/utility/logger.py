from pathlib import Path
import pandas as pd

def append_log(log_path: str, lines: list[str]):
    """
    Append log entries to a file without overwriting previous logs.
    Each call creates a new timestamped block.

    Parameters
    ----------
    log_path : str
        Path to the log file (e.g. 'outputs/logs/data_cleaning_log.txt').
    lines : list[str]
        A list of strings to write as log lines.
    """
    log_file = Path(log_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Log entry {pd.Timestamp.now()} ---\n")
        for line in lines:
            f.write(f"{line}\n")