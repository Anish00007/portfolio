import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"


def load(name, default=None):
    """Read data/<name>.json. Shows a friendly error if the JSON is malformed."""
    path = DATA_DIR / f"{name}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as e:
        st.error(f"`data/{name}.json` has a formatting error: {e}")
        st.stop()
