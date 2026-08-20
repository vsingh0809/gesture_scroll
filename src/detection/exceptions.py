class DetectionException(Exception):
    """Base detection exception."""


class DetectorInitializationError(DetectionException):
    """Failed to initialize detector."""


class HandDetectionError(DetectionException):
    """Failed to process frame."""