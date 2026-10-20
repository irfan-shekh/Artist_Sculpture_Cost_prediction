#!/usr/bin/env python
"""
Artist Sculpture Cost Prediction Web Application Runner.

Usage:
    python app.py               # Starts development server at http://127.0.0.1:8000
    python app.py [port]        # Starts server at http://127.0.0.1:[port]
    python app.py test          # Runs ML model validation tests
"""
import os
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
DJANGO_DIR = BASE_DIR / "mysite"

if str(DJANGO_DIR) not in sys.path:
    sys.path.insert(0, str(DJANGO_DIR))

def run():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    args = sys.argv[1:]

    if not args:
        print("🎨 Starting Artist Sculpture Cost Prediction Web Application...")
        print("🌐 Access the app at: http://127.0.0.1:8000")
        print("🛑 Press Ctrl+C in this terminal window to stop the server\n")
        sys.argv = [sys.argv[0], 'runserver', '127.0.0.1:8000']
    elif len(args) == 1 and args[0].isdigit():
        port = args[0]
        print(f"🎨 Starting application on port {port}...")
        print(f"🌐 Access the app at: http://127.0.0.1:{port}\n")
        sys.argv = [sys.argv[0], 'runserver', f'127.0.0.1:{port}']
    elif len(args) == 1 and args[0] in ('test', 'test_models'):
        import test_models
        success = test_models.test_artist_model()
        sys.exit(0 if success else 1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Please install requirements: pip install -r requirements.txt"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    run()
