from dataclasses import dataclass


@dataclass
class Landmark:
    x: float
    y: float
    z: float


@dataclass
class DetectionResult:
    hand_detected: bool
    landmarks: list[Landmark]