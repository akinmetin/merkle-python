class Time(object):
    def __init__(self, hours, minutes, seconds):
        # default variable inits
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        if self.seconds > 60:
            additional_mins = int(self.seconds / 60)
            self.minutes += additional_mins

            self.seconds = self.seconds % 60

        if self.minutes > 60:
            """
            find the count of hours in "minutes" var
            then add it into self.hours
            """
            additional_hours = int(self.minutes / 60)
            self.hours += additional_hours

            # mod 60 gives the minutes eg. 100 % 60 = 40
            self.minutes = self.minutes % 60

        if self.hours > 24:
            self.hours = self.hours % 24

    def scale(self, value: int):
        """
        accept an integer of seconds,
        add it to the time held in the current instance.
        """
        # if value is higher and eq. than 60 then calc. minutes
        while value >= 60:
            self.minutes += 1
            value -= 60

        """
        if seconds + values more than a minute,
        increase minutes by 1 and set new seconds var
        else just add value into seconds var
        """
        if self.seconds + value >= 60:
            self.minutes += 1
            self.seconds = (self.seconds + value) - 60
        else:
            self.seconds += value

        # if "minutes" is higher than 60 then calc. hours
        if self.minutes >= 60:
            while self.minutes >= 60:
                self.hours += 1
                self.minutes -= 60

        if self.hours >= 24:
            self.hours = self.hours % 24

    def timeString(self) -> str:
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
