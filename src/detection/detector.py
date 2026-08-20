import mediapipe as mp

from src.detection.exceptions import (
    DetectorInitializationError,
)
from src.detection.models import (
    DetectionResult,
    Landmark,
)


class HandDetector:

    def __init__(
        self,
        max_num_hands: int = 1,
        min_detection_confidence: float = 0.7,
        min_tracking_confidence: float = 0.7,
    ):
        try:

            self._mp_hands = mp.solutions.hands

            self._hands = self._mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=max_num_hands,
                min_detection_confidence=min_detection_confidence,
                min_tracking_confidence=min_tracking_confidence,
            )

            self._drawing = mp.solutions.drawing_utils

        except Exception as exc:
            raise DetectorInitializationError(
                str(exc)
            ) from exc

    def detect(self, rgb_frame) -> DetectionResult:

        result = self._hands.process(rgb_frame)

        if not result.multi_hand_landmarks:

            return DetectionResult(
                hand_detected=False,
                landmarks=[],
            )

        hand = result.multi_hand_landmarks[0]

        landmarks = [
            Landmark(
                x=lm.x,
                y=lm.y,
                z=lm.z,
            )
            for lm in hand.landmark
        ]

        return DetectionResult(
            hand_detected=True,
            landmarks=landmarks,
            
        )

    def draw_landmarks(self, frame, mediapipe_result):

        if mediapipe_result.multi_hand_landmarks:

            for hand_landmarks in (
                mediapipe_result.multi_hand_landmarks
            ):
                self._drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self._mp_hands.HAND_CONNECTIONS,
                )

    def process(self, rgb_frame):

        return self._hands.process(rgb_frame)

    def close(self):

        self._hands.close()