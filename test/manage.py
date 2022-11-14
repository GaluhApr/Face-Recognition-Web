#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from cv2 import cv2
# from flask import Flask,request,render_template
# from datetime import date
# from datetime import datetime
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
# import pandas as pd
# import joblib


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facerecognition.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
