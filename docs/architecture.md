# System Architecture

## Overview

Gesture Controlled Browser Scrolling uses computer vision to detect hand movements and convert them into browser scrolling actions.

---

## Architecture Flow

Webcam
↓
Camera Module
↓
Hand Detection Module
↓
Gesture Recognition Module
↓
Action Controller
↓
Operating System Scroll Event
↓
Browser

---

## Components

### Camera Module

Responsibilities:
- Access webcam
- Capture frames
- Handle camera errors

Input:
- Webcam Feed

Output:
- Video Frames

---

### Hand Detection Module

Responsibilities:
- Detect hand landmarks
- Extract landmark coordinates

Input:
- Video Frame

Output:
- Hand Landmarks

Technology:
- MediaPipe Hands

---

### Gesture Recognition Module

Responsibilities:
- Track fingertip movement
- Identify scrolling gestures

Input:
- Hand Landmarks

Output:
- SCROLL_UP
- SCROLL_DOWN
- NO_ACTION

---

### Action Controller

Responsibilities:
- Trigger OS scroll events

Input:
- Gesture Event

Output:
- Browser Scroll

Technology:
- Pynput

---

## Technology Stack

Language:
- Python 3.12+

Libraries:
- OpenCV
- MediaPipe
- Pynput

---

## Architectural Decisions

### Decision 1

Local Processing

Reason:
- Offline support
- Low latency
- Privacy

### Decision 2

Single Hand Tracking

Reason:
- Simpler implementation
- Better accuracy

### Decision 3

Rule-Based Gesture Recognition

Reason:
- Faster development
- No model training required