# QUESTION 
#published by Daily Coding Problem #1692
#Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

#Bonus: When, during the course of a day, will the angle be zero?
# Bonus ANSWER -> 12 o clock on the dot, all the other hours don't align 

# .'`~~~~~~~~~~~`'.
# (  .'11 12 1'.  )
# |  :10 \|   2:  |
# |  :9   @   3:  |
# |  :8       4;  |
# '. '..7 6 5..' .'
#  ~-------------~  
# (from https://www.asciiart.eu/electronics/clocks)

def convertTimeToDegrees(hours, minutes):
    if hours < 1 or hours > 12:
        print("Hour must be between 1 and 12")
        return False
    if minutes < 0 or minutes > 59:
        print("Minute must be between 0 and 59")
        return False
    
    HourDegree = (hours % 12) * 30 + minutes * 0.5
    MinuteDegree = minutes * 6

    return abs(MinuteDegree - HourDegree)

# 
hours = 7
minutes = 38
print(convertTimeToDegrees(hours, minutes))
