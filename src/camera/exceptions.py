class CameraException(Exception):
    """Base camera exception."""


class CameraNotFoundError(CameraException):
    """No camera device available."""


class CameraInitializationError(CameraException):
    """Failed to initialize camera."""


class CameraReadError(CameraException):
    """Unable to read frame."""


class CameraDisconnectedError(CameraException):
    """Camera disconnected while streaming."""


class InvalidCameraConfigurationError(CameraException):
    """Invalid camera configuration."""