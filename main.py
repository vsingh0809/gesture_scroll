import cv2

from src.camera.webcam import Webcam
from src.config.settings import camera_settings
from src.detection.detector import HandDetector
from src.gestures.recognizer import GestureRecognizer
from src.gestures.models import GestureEvent
from src.utils.logger import get_logger
from src.detection.renderer import (
    LandmarkRenderer,
)



logger = get_logger(__name__)


def main():

    logger.info("Application starting")

    detector = HandDetector()
    recognizer = GestureRecognizer()
    renderer = LandmarkRenderer()

    try:

        with Webcam() as webcam:

            logger.info(
                "Gesture recognition started"
            )

            while True:

                frame = webcam.read_frame()

                rgb_frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB,
                )

                detection_result = detector.detect(
                    rgb_frame
                )

                gesture = recognizer.recognize(
                    detection_result.landmarks
                )
                if gesture != GestureEvent.NO_ACTION:

                    print(
                        f"Detected: {gesture.value}"
    )  

                renderer.draw_landmarks(
                 frame,
                 detection_result.landmarks
                )

                cv2.putText(
                    frame,
                    f"Gesture: {gesture.value}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

                hand_status = (
                    "Detected"
                    if detection_result.hand_detected
                    else "Not Detected"
                )

                cv2.putText(
                    frame,
                    f"Hand: {hand_status}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 0),
                    2,
                )

                cv2.imshow(
                    camera_settings.WINDOW_NAME,
                    frame,
                )

                key = (
                    cv2.waitKey(1)
                    & 0xFF
                )

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

        detector.close()

        cv2.destroyAllWindows()

        logger.info(
            "Application shutdown complete"
        )


if __name__ == "__main__":
    main()