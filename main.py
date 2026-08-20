import cv2

from src.camera.webcam import Webcam
from src.config.settings import camera_settings
from src.utils.logger import get_logger


logger = get_logger(__name__)


def main():

    logger.info("Application starting")

    try:

        with Webcam() as webcam:

            logger.info(
                f"Camera Resolution: "
                f"{webcam.camera_info.width}x"
                f"{webcam.camera_info.height}"
            )

            while True:

                frame = webcam.read_frame()

                cv2.imshow(
                    camera_settings.WINDOW_NAME,
                    frame,
                )

                key = cv2.waitKey(1) & 0xFF

                if key == ord("q"):
                    logger.info(
                        "Exit requested by user"
                    )
                    break

    except Exception as exc:

        logger.exception(
            f"Application failed: {exc}"
        )

    finally:

        logger.info("Application shutdown")


if __name__ == "__main__":
    main()