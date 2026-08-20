class GestureException(Exception):
    """Base gesture exception."""


class InvalidLandmarkError(GestureException):
    """Invalid landmark data received."""


class GestureRecognitionError(GestureException):
    """Gesture recognition failed."""