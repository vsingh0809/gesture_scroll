import cv2

from src.camera.exceptions import (
    CameraInitializationError,
    CameraReadError,
)
from src.camera.models import CameraInfo
from src.config.settings import camera_settings
from src.utils.logger import get_logger


logger = get_logger(__name__)


class Webcam:
    """
    Production-ready webcam wrapper.

    Features:
    - Context manager support
    - Centralized logging
    - Custom exceptions
    - Camera diagnostics
    """

    def __init__(self):
        self._capture = None
        self._camera_info = None

        logger.info("Webcam instance created")

    def __enter__(self):
        logger.info("Initializing webcam")

        self._capture = cv2.VideoCapture(
            camera_settings.CAMERA_INDEX
        )

        if not self._capture.isOpened():
            logger.error("Failed to initialize webcam")

            raise CameraInitializationError(
                f"Unable to open camera index "
                f"{camera_settings.CAMERA_INDEX}"
            )

        self._capture.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            camera_settings.FRAME_WIDTH,
        )

        self._capture.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            camera_settings.FRAME_HEIGHT,
        )

        self._camera_info = CameraInfo(
            camera_index=camera_settings.CAMERA_INDEX,
            width=int(
                self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            ),
            height=int(
                self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            ),
            fps=int(
                self._capture.get(cv2.CAP_PROP_FPS)
            ),
        )

        logger.info(
            "Webcam initialized successfully "
            f"({self._camera_info.width}x"
            f"{self._camera_info.height})"
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

    def read_frame(self):
        """
        Capture and return a frame.
        """

        if not self.is_opened():
            logger.error(
                "Attempted frame read from closed camera"
            )

            raise CameraReadError(
                "Camera is not opened."
            )

        success, frame = self._capture.read()

        if not success or frame is None:
            logger.error("Failed to read frame")

            raise CameraReadError(
                "Unable to read frame from webcam."
            )

        return frame

    def is_opened(self) -> bool:
        return (
            self._capture is not None
            and self._capture.isOpened()
        )

    def release(self):
        """
        Safe cleanup.
        Can be called multiple times.
        """

        if self._capture is not None:

            logger.info("Releasing webcam")

            self._capture.release()

            self._capture = None

        cv2.destroyAllWindows()

        logger.info("Webcam resources released")

    @property
    def camera_info(self):
        return self._camera_info