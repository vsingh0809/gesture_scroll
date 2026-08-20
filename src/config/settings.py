from dataclasses import dataclass


@dataclass(frozen=True)
class CameraSettings:
    CAMERA_INDEX: int = 0
    FRAME_WIDTH: int = 1280
    FRAME_HEIGHT: int = 720
    WINDOW_NAME: str = "Gesture Scroll"
    TARGET_FPS: int = 30


@dataclass(frozen=True)
class LoggingSettings:
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/application.log"


camera_settings = CameraSettings()
logging_settings = LoggingSettings()