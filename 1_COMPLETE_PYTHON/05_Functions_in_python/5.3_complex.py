"""
SPLITTING THE COMPLEX TASKS 

you are creating a monthly report for a cafe's slaes .
instead of putting all logic in one place, break it down.
Task:
Write a function generate_report() that calls:
1.fetch_sales()
2.filter_valid_orders()
3.summarize_data()
"""

def fetch_sales():
    print("Fetching sales data....")


def filter_valid_sales():
    print("filtering valid sales data")

def summarize_data():
    print("summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready!")

print(generate_report())