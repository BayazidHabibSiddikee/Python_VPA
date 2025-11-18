import arrow

# current time in 'H:m:s' format
current_time = arrow.now().format('H:m:s')
print("Current Time:", current_time)

# current time in 'hh:mm:ss A' format
current_time_12hr = arrow.now().format('hh:mm:ss A')
print("Current Time (12-hour format):", current_time_12hr)

# current date in 'DD-MM-YYYY' format
current_date = arrow.now().format('DD-MM-YYYY')
print("Current Date:", current_date)

print(f"Current hour:{arrow.now().format('H')}")
print(f"Current second:{arrow.now().format("ss")}")

if str(arrow.now().format('A')) == 'AM':
    print("Good Morning!")