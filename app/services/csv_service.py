from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def load_csv(file_name: str) -> pd.DataFrame:
    csv_path = DATA_DIR / file_name

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    df = df.replace({np.nan: None})

    return df


def load_csv_data(csv_file: str) -> pd.DataFrame:
    return load_csv(csv_file)
