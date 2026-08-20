from dataclasses import dataclass


@dataclass
class CameraInfo:
    camera_index: int
    width: int
    height: int
    fps: int