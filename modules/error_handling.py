# modules/error_handling.py

from flask import flash, redirect, url_for

def handle_invalid_url():
    """Handles invalid URLs by redirecting to the home page and showing an error message."""
    flash("Invalid URL. Please check and try again.", "danger")
    return redirect(url_for('index'))
