def add_time(start, duration, day = None):
# Reject bad user input
  if(start is None or duration is None):
    return "Error: Enter a valid start time and duration."
    
# Seperate Time and AM or PM for Start Time
  startTime = start.split(" ")[0]
  startMer = start.split(" ")[1]
  print("Start time =", start)
  
# Seperate Hours and Minutes for Start Time
  startHr = startTime.split(":")[0]
  startMn = startTime.split(":")[1]
  
# Seperate Hours and Minutes for Duration
  durationHr = duration.split(":")[0]
  durationMn = duration.split(":")[1]
  print("Duration time =", duration)
  
# Convert to military time
  if(startMer == "PM"):
    startHr = int(startHr) + 12
    
# Add start time and duration time together
  addedHr = int(startHr) + int(durationHr)
  addedMn = int(startMn) + int(durationMn)
  
  if(addedMn >= 60):
    addedMn = addedMn - 60
    addedHr = addedHr + 1
  if(addedMn < 10):
    addedMn = '0' + str(addedMn)
    
# Get new time if added hours < 12
  if(addedHr < 12 and day == None):
    newTime = f"{addedHr}:{addedMn} {startMer}"
    print("New time =", newTime)
    return newTime
    
# Get new time if added hours >= 12 and < 24
  if(addedHr >= 12 and addedHr < 24 and day == None):
    addedHr = int(addedHr) - 12
    if(addedHr == 0):
      addedHr = 12
    newTime = f"{addedHr}:{addedMn} PM"
    print("New time =", newTime)
    return newTime
    
# Convert time >= 24 hours to days and time
  numDays = 0
  newMer = ""
  if(addedHr >= 24):
    numDays = int(addedHr / 24)
    addedHr = addedHr % 24
    newMer = "AM"
  if(addedHr >= 12):
    addedHr = addedHr - 12
    newMer = "PM"
  if(addedHr == 0):
    addedHr = 12
    newMer = "AM"

# Get new time >= 24 if no day is specified 
  if(day == None and numDays == 1):
    newTime = f"{addedHr}:{addedMn} {newMer} (next day)"
    print("New time =", newTime)
    return newTime
  if(day == None and numDays != 1):
    newTime = f"{addedHr}:{addedMn} {newMer} ({numDays} days later)"
    print("New time =", newTime)
    return newTime
    
# Get new time >= 24 if day is specified
  day = day.lower()
  daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  index = -1
  daysIndex = 0
  print(numDays)
  for i in daysOfWeek:
    index = index + 1
    if i == day:
      break
  print(index)
  if(numDays + index <= 6):
    daysIndex = index + numDays
  elif(numDays + index > 6):
    daysIndex = numDays % 7
    if(daysIndex + index > 6):
      daysIndex = int(6 - (6/index))
  daysOfWeekUpper = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  if(day != None and numDays == 0):
    newTime = f"{addedHr}:{addedMn} {newMer}, {daysOfWeekUpper[daysIndex]}"
    print("New time =", newTime)
    return newTime
  if(day != None and numDays == 1):
    newTime = f"{addedHr}:{addedMn} {newMer}, {daysOfWeekUpper[daysIndex]} (next day)"
    print("New time =", newTime)
    return newTime
  if(day != None and numDays != 1):
    print(daysIndex)
    newTime = f"{addedHr}:{addedMn} {newMer}, {daysOfWeekUpper[daysIndex]} ({numDays} days later)"
    print("New time =", newTime)
    return newTime
    
