class NotWearingMaskError(BaseException):
    pass


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):  # Add additional line at the end of file
    pass