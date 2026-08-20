import cv2

from src.camera.webcam import Webcam
from src.detection.detector import HandDetector
from src.config.settings import camera_settings


def main():

    detector = HandDetector()

    with Webcam() as webcam:

        while True:

            frame = webcam.read_frame()

            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB,
            )

            mp_result = detector.process(
                rgb_frame
            )

            detector.draw_landmarks(
                frame,
                mp_result,
            )

            cv2.imshow(
                camera_settings.WINDOW_NAME,
                frame,
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    detector.close()


if __name__ == "__main__":
    main()