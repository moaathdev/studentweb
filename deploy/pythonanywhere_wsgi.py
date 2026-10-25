"""
WSGI entry point for PythonAnywhere.

PythonAnywhere does not run gunicorn; it imports a WSGI callable instead.

How to use:
  1. Open the "Web" tab of your PythonAnywhere app.
  2. Under "Code", click the link to the WSGI configuration file
     (/var/www/<your-username>_pythonanywhere_com_wsgi.py).
  3. Delete everything in it and paste this file's contents.
  4. Replace every <PLACEHOLDER> below.
  5. Save, then press the green "Reload" button.

Secrets stay on the server in this file. They are never committed to the
repository, so the public source code remains free of credentials.
"""

import os
import sys

# --- 1. Project location ---------------------------------------------------
# The directory that contains app.py.
PROJECT_DIR = "/home/<USERNAME>/studentweb"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# --- 2. Configuration ------------------------------------------------------
os.environ.setdefault("ADMIN_USER", "root")
os.environ.setdefault("ADMIN_PASS", "<CHANGE_ME>")

# PythonAnywhere serves your app over HTTPS, but http:// also reaches it.
# Keep this at "0" unless you are certain every visitor uses HTTPS —
# otherwise the session cookie is dropped and login silently fails.
os.environ.setdefault("COOKIE_SECURE", "0")

# --- 3. Application object -------------------------------------------------
# PythonAnywhere looks for a module-level name called `application`.
from app import app as application  # noqa: E402,F401
