from app.cafe import Cafe  # Imported but unused
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
# According PEP8 imports' style, you need to use a proper amount of space
# when you import multiple objects from a package. Usually its 4 or 8
# https://peps.python.org/pep-0008/#imports


def go_to_cafe(friends, cafe) -> str:  # Use type hints https://docs.python.org/3/library/typing.html
    total = 0

    for i in range(len(friends)):
        try:
            cafe.visit_cafe(friends[i])
        except (NotVaccinatedError, OutdatedVaccineError):
            return 'All friends should be vaccinated'
        except NotWearingMaskError:
            total += 1

    if total:
        return f'Friends should buy {total} masks'
    else:
        return f'Friends can go to {cafe.name}'
