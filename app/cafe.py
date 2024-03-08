from app.errors import NotVaccinatedError, \
                        OutdatedVaccineError, \
                        NotWearingMaskError
import datetime
# According PEP8 imports' style, you need to use double quotes '()'
# and proper amount of space when you import multiple objects from a package, not a \
# https://peps.python.org/pep-0008/#imports


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, vstr: dict) -> str:
        # It is better to use variable with descriptive name
        # Function can return not only 'str' type, but Exception as well

        if "vaccine" not in vstr.keys() or vstr["vaccine"] == None:
            # While comparing object to "None" it's better to user "is"
            raise NotVaccinatedError("not vaccinated")
        elif vstr["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("outdated")
        elif not vstr["wearing_a_mask"]:
            raise NotWearingMaskError("not wearing mask")
        else:  # No need to user additional else if every condition before return has the 'return' or 'raise'
            return "Welcome to " + self.name
