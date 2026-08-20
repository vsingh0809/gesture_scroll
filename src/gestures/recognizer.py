from collections import deque

from src.gestures.models import (
    GestureEvent,
    GestureState,
)
from src.gestures.exceptions import (
    InvalidLandmarkError,
    GestureRecognitionError,
)


class GestureRecognizer:

    def __init__(
        self,
        threshold: float = 0.08,
        history_size: int = 8,
    ):
        self.threshold = threshold

        self.positions = deque(
            maxlen=history_size
        )

        self.state = GestureState.IDLE

    def recognize(self, landmarks):

        try:

            if not landmarks:

                self.positions.clear()
                self.state = GestureState.IDLE

                return GestureEvent.NO_ACTION

            if len(landmarks) < 9:
                raise InvalidLandmarkError(
                    "Expected at least 9 landmarks."
                )

            wrist = landmarks[0]
            index_tip = landmarks[8]

            relative_y = (
                index_tip.y - wrist.y
            )

            self.positions.append(
                relative_y
            )

            if (
                len(self.positions)
                < self.positions.maxlen
            ):
                return GestureEvent.NO_ACTION

            movement = (
                self.positions[-1]
                - self.positions[0]
            )

            print(
                f"movement={movement:.3f}, "
                f"state={self.state.value}"
            )

            if self.state == GestureState.IDLE:

                if movement < -self.threshold:

                    self.state = (
                        GestureState.MOVING_UP
                    )

                    return GestureEvent.SCROLL_UP

                if movement > self.threshold:

                    self.state = (
                        GestureState.MOVING_DOWN
                    )

                    return GestureEvent.SCROLL_DOWN

            elif self.state == GestureState.MOVING_UP:

                if abs(movement) < (
                    self.threshold / 3
                ):

                    self.state = (
                        GestureState.IDLE
                    )

            elif self.state == GestureState.MOVING_DOWN:

                if abs(movement) < (
                    self.threshold / 3
                ):

                    self.state = (
                        GestureState.IDLE
                    )

            return GestureEvent.NO_ACTION

        except InvalidLandmarkError:
            raise

        except Exception as exc:

            raise GestureRecognitionError(
                f"Failed to recognize gesture: {exc}"
            ) from exc