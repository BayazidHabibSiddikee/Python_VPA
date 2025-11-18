import arrow, time

# Tell the user time format to set
print('''Set ypur timer in one of the following formats:
      - "timer for X hour Y minutes"
      - "timer for X minutes"
      - "timer for X hours"''')

# Set the timer
inp = input("How long u want to set the timer for?: ").lower()

# Find the positions of hours, minutes in the input
pos1 = inp.find('timer for')
pos2 = inp.find('hour')
pos3 = inp.find('minute')

# handling 'timer for x hours only
if pos3== -1:
    addhour = inp[pos1 + len("timer for"):pos2]
    addmin = 0
# handling 'timer for x minutes only
elif pos2 == -1:
    addhour = 0
    addmin = inp[pos1 + len("timer for"):pos3]
# handling 'timer for x hours y minutes'
else:
    addhour = inp[pos1 + len("timer for"):pos2]
    addmin = inp[pos2 + len("hour"):pos3]
    
# Get the current time
current_hour = arrow.now().format('H')
current_min = arrow.now().format('m')
start_ss = arrow.now().format('s')

# Calculate the target time
new_hour = int(current_hour) + int(addhour)
new_min = int(current_min) + int(addmin)

if new_min >= 60:
    new_min = new_min - 60
    new_hour += 1
new_hour = new_hour % 24
end_time = str(new_hour) + ':' + str(new_min) + ':' + start_ss
print(f'Timer set for {addhour} hours and {addmin} minutes. It will go off at {end_time}.')

while True:
    timenow = arrow.now().format('H:m:s')
    if timenow == end_time:
        print("Time's up!")
        break
    time.sleep(1)
