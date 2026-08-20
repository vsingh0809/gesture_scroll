import cv2

from src.detection.models import Landmark


class LandmarkRenderer:

    def draw_landmarks(
        self,
        frame,
        landmarks: list[Landmark],
    ):

        if not landmarks:
            return

        height, width, _ = frame.shape

        for landmark in landmarks:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1,
            )