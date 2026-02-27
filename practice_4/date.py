#example 1
from datetime import datetime, timedelta

current_date = datetime.now().date()

five_days_ago = current_date - timedelta(days=5)

print(f"Current date: {current_date}")
print(f"Date 5 days ago: {five_days_ago}")

#example 2
from datetime import datetime, timedelta

today = datetime.now().date()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

#example 3
from datetime import datetime

current_datetime = datetime.now()
print(f"With microseconds: {current_datetime}")

datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(f"Without microseconds: {datetime_without_microseconds}")

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted without microseconds: {formatted_datetime}")

#example 4
from datetime import datetime
print("\n--- Example with custom dates ---")
date1_input = datetime(2024, 2, 1, 9, 0, 0)
date2_input = datetime(2024, 2, 2, 18, 30, 0)

diff_seconds = (date2_input - date1_input).total_seconds()
print(f"Date 1: {date1_input}")
print(f"Date 2: {date2_input}")
print(f"Difference in seconds: {diff_seconds}")