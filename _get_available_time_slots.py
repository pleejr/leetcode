# This is a custom exercise I made for myself in preparation for an interview at GlossGenius.

# Given a list of scheduled appointments throughout a day, return all time slots available for scheduling a new appointment of a given duration.
# The opening and closing times will be provided and new appointments are restricted to consecutive scheduling.

# Example 1:
# hours_of_operation = ["08:00", "17:00"]
# appointments = ["09:00-10:00", "10:30-11:30", "12:00-13:30", "15:10-15:40"]
# duration = 30
# available_time_slots = ["08:00-08:30", "08:30-09:00", "10:00-10:30", "11:30-12:00", "13:30-14:00", "14:00-14:30", "14:30-15:00", "15:40-16:10", "16:10-16:40"]

# get open slots, regardless of duration
# split the appointments into start and end elements of type datetime


# determine which open slots are suitable for the required duration
# open, sorted time slots

from datetime import datetime, timedelta

tests = [
    (
        ['08:00', '17:00'],
        ['12:00-13:30', '15:10-15:40', '10:30-11:30', '09:00-10:00'],
        30,
        ['08:00-09:00', '10:00-10:30', '11:30-12:00', '13:30-15:10', '15:40-17:00'],
    ),
    (
        ['08:00', '17:00'],
        ['12:00-13:30', '15:10-15:40', '10:30-11:30', '09:00-10:00'],
        60,
        ['08:00-09:00', '13:30-15:10', '15:40-17:00'],
    ),
]

def main():
    sol = Solution()
    for i in range(len(tests)):
        result = sol.getAvailableTimeSlots(tests[i][0], tests[i][1], tests[i][2])
        print(f"\nduration: {tests[i][2]} min",
              f"\nsolution: {result}",
              f"\n  answer: {tests[i][3]}"
              f"\n correct: {result == tests[i][3]}")
    return


class Solution():    
    def getAvailableTimeSlots(self, hours_of_operation: list[str], appointments: list[str], duration: int) -> list[str]:
        # convert string to datetime
        def strToTime(time: str, fmt="%H:%M") -> datetime:
            time = datetime.strptime(time, fmt).time()
            dtime = datetime.combine(datetime.today(), time)
            return dtime

        # get time delta between two appointments
        def getAppointmentTimeDelta(a1: datetime, a2: datetime) -> datetime:
            return (a2[0] - a1[1])
        
        # get time slot between two appointments
        def getTimeSlotBetweenAppointments(a1: datetime, a2: datetime) -> datetime:
            return (a1[1], a2[0])

        # insert non-business hours as "appointments"
        open = f"00:00-{hours_of_operation[0]}"
        close = f"{hours_of_operation[1]}-00:00"
        appointments.extend([open, close])

        # convert existing appointments to datetimes, then sort results
        appointment_datetimes = []
        for appointment in appointments:
            start, end = appointment.split("-")
            appointment_datetimes.append((strToTime(start), strToTime(end)))
        appointment_datetimes_sorted = sorted(appointment_datetimes, key=lambda x: x[0])

        # generate available timeslots, then sort results
        unordered_timeslots = []
        for i in range(1, len(appointment_datetimes_sorted)):
            unordered_timeslots.append(getTimeSlotBetweenAppointments(appointment_datetimes_sorted[i-1], appointment_datetimes_sorted[i]))
        ordered_timeslots = sorted(unordered_timeslots, key=lambda x: x[0])

        # get gaps, then sort results
        gaps = []
        for i in range(1, len(appointment_datetimes_sorted)):
            gaps.append(getAppointmentTimeDelta(appointment_datetimes_sorted[i-1], appointment_datetimes_sorted[i]))

        # print([(gap.total_seconds() // 60) for gap in gaps])
        # print(ordered_timeslots)

        # convert datetime timeslots to strings
        available_timeslots = []
        for timeslot in ordered_timeslots:
            start, end = timeslot[0].strftime("%H:%M"), timeslot[1].strftime("%H:%M")
            available_timeslots.append(f"{start}-{end}")

        # filter out timeslots that are too small for the required duration
        viable_timeslots = []
        for i in range(len(available_timeslots)):
            if gaps[i] >= timedelta(minutes=duration):
                viable_timeslots.append(available_timeslots[i])

        # print(available_timeslots)
        return viable_timeslots


if __name__ == "__main__":
    main()