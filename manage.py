#!/usr/bin/env python
"""Root-level Django management script for Artist Sculpture Cost Prediction."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DJANGO_DIR = BASE_DIR / "mysite"

if str(DJANGO_DIR) not in sys.path:
    sys.path.insert(0, str(DJANGO_DIR))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Please make sure dependencies are installed: pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
