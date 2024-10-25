# lib/helpers.py

import os
import json
from datetime import datetime, date, time

def validate_input(prompt, allowed_types=(str, int)):
    while True:
        value = input(prompt).strip()
        try:
            if isinstance(allowed_types, tuple):
                if value.isdigit():
                    return int(value)
                elif value.isalpha():
                    return value.strip().lower()
                else:
                    return value.strip()
            else:
                return allowed_types(value.strip())
        except ValueError:
            print("Invalid input. Please try again.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_date_input(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_time_input(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%H:%M:%S").time()
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")

def get_datetime_input(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d %H:%M:%S").replace(microsecond=0)
        except ValueError:
            print("Invalid datetime format. Please use YYYY-MM-DD HH:MM:SS.")