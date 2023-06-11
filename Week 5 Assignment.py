1. Factory Method

class Employee:
    def __init__(self, name, weekly_work_hours):
        self.name = name
        self.weekly_work_hours = weekly_work_hours

    @classmethod
    def create_employee(cls, name, weekly_work_hours):
        if weekly_work_hours >= 40:
            return FullTimeEmployee(name, weekly_work_hours)
        else:
            return PartTimeEmployee(name, weekly_work_hours)

class FullTimeEmployee(Employee):
    def __init__(self, name, weekly_work_hours):
        super().__init__(name, weekly_work_hours)
        self.salary = 45000

class PartTimeEmployee(Employee):
    def __init__(self, name, weekly_work_hours):
        super().__init__(name, weekly_work_hours)
        self.hourly_wage = 18




2. Composite Pattern


class TimesheetComponent:
    def __init__(self):
        self.timesheets = []

    def add_timesheet(self, timesheet):
        self.timesheets.append(timesheet)

    def get_total_hours(self):
        total_hours = 0
        for timesheet in self.timesheets:
            total_hours += timesheet.get_total_hours()
        return total_hours

class Employee(TimesheetComponent):
    def __init__(self, name):
        super().__init__()
        self.name = name

class TimeKeepingSystem(TimesheetComponent):
    def __init__(self):
        super().__init__()
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_total_hours(self):
        total_hours = super().get_total_hours()
        for employee in self.employees:
            total_hours += employee.get_total_hours()
        return total_hours




3. Command Pattern

class Timesheet:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def update_entry(self, index, new_entry):
        self.entries[index] = new_entry

    def delete_entry(self, index):
        del self.entries[index]

class TimesheetCommand:
    def __init__(self, timesheet, command_type, index, entry):
        self.timesheet = timesheet
        self.command_type = command_type
        self.index = index
        self.entry = entry

    def execute(self):
        if self.command_type == "add":
            self.timesheet.add_entry(self.entry)
        elif self.command_type == "update":
            self.timesheet.update_entry(self.index, self.entry)
        elif self.command_type == "delete":
            self.timesheet.delete_entry(self.index)

    def undo(self):
        if self.command_type == "add":
            self.timesheet.delete_entry(-1)
        elif self.command_type == "update":
            self.timesheet.update_entry(self.index, self.entry)
        elif self.command_type == "delete":
            self.timesheet.add_entry(self.entry)
