"""
File: erapp.py
The view for an emergency room scheduler.
"""

from model import ERModel, Patient, Condition

class ERView(object):
    """The view class for the ER application."""

    def __init__(self):
        self._model = ERModel()

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
               "  1  Schedule a patient\n" + \
               "  2  Treat the next patient\n" + \
               "  3  Treat all patients\n" \
               "  4  Exit the program\n"
        while True:
            command = self._getCommand(4, menu)
            if   command == 1: self._schedule()
            elif command == 2: self._treatNext()
            elif command == 3: self._treatAll()
            else: break

    def _treatNext(self):
        """Treats one patient if there is one."""
        patient = self._model.treatNext()
        if patient is None:
            print "No patients available to treat"
            return False
        else:
            print patient, "is being treated"
            return True

    def _treatAll(self):
        while self._treatNext():
            pass
   
    def _schedule(self):
        """Obtains patient info and schedules patient."""
        name = raw_input("\nEnter the patient's name: ")
        condition = self._getCondition()
        self._model.schedule(Patient(name, condition))
        print name, "is added to the", condition, "list\n"

    def _getCondition(self):
        """Obtains condition info."""
        menu = "Patient's condition:\n" + \
               "  1  Critical\n" + \
               "  2  Serious\n" + \
               "  3  Fair\n"
        number = self._getCommand(3, menu)
        return Condition(number)

    def _getCommand(self, high, menu):
        """Obtains and returns a command number."""
        prompt = "Enter a number [1-" + str(high) + "]: "
        commandRange = map(str, range(1, high + 1))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print menu
            command = raw_input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print error

# Main function to start up the application

def main():
    view = ERView()
    view.run()

main()

            
