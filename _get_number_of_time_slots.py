# This is a reconstruction of the actual coding interview question I had with GlossGenius on 2025-04-09.
# The sample data used is not the same and some details may vary slightly, but it is functionally similar.

# The prompt was similar to the following:
#   Given a list of lists of daily appointments and their duration in a dictionary, return the number of available 30-minute slots remaining for the week.

# The following were the restrictions:
#   - The business opens at 08:00 and closes at 17:00 each day.
#   - Existing/scheduled appointments may be 30, 60, or 90 minutes in duration.
#   - Appointments do not and should not overlap.

# Additionally, my pair programming interviewer clarified the following:
#   - The appointments are listed in order from first to last, each day.

from datetime import datetime, timedelta

week_of_20250406 = [
    # 44 available slots of 30-minutes
    [
        # 12
        {"appointment": "09:00", "duration": 30},   # 2
        {"appointment": "10:00", "duration": 60},   # 1
        {"appointment": "11:00", "duration": 30},   # 0
        {"appointment": "12:00", "duration": 30},   # 1
        {"appointment": "15:00", "duration": 30},   # 5
                                                    # 3
    ],
    [
        # 10
        {"appointment": "09:30", "duration": 30},   # 3
        {"appointment": "10:00", "duration": 60},   # 0
        {"appointment": "11:30", "duration": 30},   # 1
        {"appointment": "12:00", "duration": 30},   # 0
        {"appointment": "15:30", "duration": 90},   # 6
                                                    # 0
    ],
    [   # 7
        {"appointment": "09:30", "duration": 90},   # 3
        {"appointment": "11:30", "duration": 30},   # 1
        {"appointment": "13:30", "duration": 60},   # 3
        {"appointment": "14:40", "duration": 30},   # 0
        {"appointment": "15:30", "duration": 90},   # 0
                                                    # 0
    ],
    [   # 8
        {"appointment": "08:30", "duration": 90},   # 1
        {"appointment": "10:30", "duration": 30},   # 1
        {"appointment": "12:30", "duration": 60},   # 3
        {"appointment": "13:30", "duration": 30},   # 0
        {"appointment": "14:30", "duration": 90},   # 1
                                                    # 2
    ],
    [   # 7
        {"appointment": "09:30", "duration": 90},   # 3
        {"appointment": "11:30", "duration": 30},   # 1
        {"appointment": "13:30", "duration": 60},   # 3
        {"appointment": "14:30", "duration": 60},   # 0
        {"appointment": "15:30", "duration": 90},   # 0
                                                    # 0
    ],
]

# add dummy appointments to the beginning and end of each day for non-business hours
def addOpenAndClose(week):
    adjusted_week = []
    opening = [{"appointment": "00:00", "duration": 480}]
    closing = [{"appointment": "17:00", "duration": 360}]
    for day in week:
        adjusted_week.append(opening + day + closing)
    return adjusted_week

# convert each appointment and duration to datetime start and end
def convertWeekToDatetimes(week):
    this_week = []
    for day in week:
        this_day = []
        for appt in day:
            appt_dt = datetime.strptime(appt["appointment"], "%H:%M")
            dur_delta = timedelta(minutes=appt["duration"])
            appt_pair = (appt_dt, appt_dt + dur_delta)
            this_day.append(appt_pair)
        this_week.append(this_day)
    return this_week

# calculate the duration of each gap between appointments
def getGapDurations(week):
    weekly_gaps = []
    for day in week:
        for i in range(1, len(day)):
            end_of_curr_appt = day[i-1][1]
            start_of_next_appt = day[i][0]
            gap = start_of_next_appt - end_of_curr_appt
            weekly_gaps.append(gap)
    return weekly_gaps

# divide each gap by 30-minutes using integer division to exclude partial slots
# sum and return the number of available 30-minute slots for the whole week
def getSlots(gaps):
    num_of_gaps = 0
    for gap in gaps:
        gap_minutes = gap.total_seconds() // 60
        gap_slots = gap_minutes // 30
        num_of_gaps += gap_slots
    return num_of_gaps

week_w_openandclose = addOpenAndClose(week_of_20250406)
week_of_datetimes = convertWeekToDatetimes(week_w_openandclose)
week_of_gaps = getGapDurations(week_of_datetimes)
week_of_slots = getSlots(week_of_gaps)

print(week_of_slots)