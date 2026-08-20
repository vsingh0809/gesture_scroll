# Gesture Controlled Browser Scrolling

## Problem Statement

Users want to scroll web pages without using a mouse or keyboard by performing hand gestures in front of a webcam.

## Objective

Develop a desktop application that detects hand gestures through a webcam and converts them into browser scrolling actions.

---

## In Scope

- Webcam access
- Real-time hand detection
- Index finger tracking
- Scroll Up gesture
- Scroll Down gesture
- Offline processing
- Windows 11 support
- Chrome support
- Edge support

---

## Out Of Scope

- Voice commands
- Mouse cursor control
- Left click / right click
- Multi-hand tracking
- Mobile support
- MacOS support
- Linux support
- Cloud deployment

---

## Functional Requirements

### FR-001
Application shall access the default webcam.

### FR-002
Application shall display live webcam feed.

### FR-003
Application shall detect one hand.

### FR-004
Application shall track hand landmarks.

### FR-005
Application shall detect upward finger movement.

### FR-006
Application shall detect downward finger movement.

### FR-007
Application shall generate scroll events.

### FR-008
Application shall stop scrolling when no gesture is detected.

---

## Non Functional Requirements

### NFR-001
Response time < 200 ms

### NFR-002
Minimum 20 FPS

### NFR-003
Offline execution

### NFR-004
CPU usage < 30%

### NFR-005
No user data leaves the machine

---

## Acceptance Criteria

- Webcam opens successfully
- Hand landmarks visible
- Upward movement scrolls up
- Downward movement scrolls down
- Works in Chrome
- Works in Edge
- Works offline

---

## Risks

- Poor lighting
- Low quality webcam
- Gesture jitter
- Webcam permission issues