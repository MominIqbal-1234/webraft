import datetime

# Get the current time
now = datetime.datetime.now()

# Calculate the time exactly two hours from now
two_hours_later = now + datetime.timedelta(seconds=120)
print(two_hours_later,"two_hours_later")

# Convert the time two hours later to a full datetime string including seconds
two_hours_later_str = two_hours_later.strftime("%H:%M:%S")

print("Time two hours later:", two_hours_later_str)


from datetime import datetime

# Parse the given time string and combine it with today's date
given_time_str = two_hours_later_str
# given_time_str = "22:04:39"


given_time = datetime.strptime(given_time_str, "%H:%M:%S").time()
today = datetime.now().date()
given_datetime = datetime.combine(today, given_time)

# Get the current datetime
current_datetime = datetime.now()

# Compare the times
if current_datetime > given_datetime:
    print(f"Current time is later than {two_hours_later_str}")
elif current_datetime < given_datetime:
    print(f"Current time is earlier than {two_hours_later_str}")
else:
    print(f"Current time is exactly {two_hours_later_str}")
