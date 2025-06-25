# Appium W3C Actions API Guide for Mobile Gestures

This document explains how to use the W3C Actions API in Appium 2.0 to perform mobile-specific gestures, such as long press, tap, swipe, pinch zoom, drag-and-drop, and multi-touch, multi touch, and multi-tap. It includes detailed Python examples, clarifies the process, and provides references to official documentation. The W3C Actions API, part of the Selenium 4 and extended by Appium, is the modern approach for handling complex gestures, replacing the deprecated `TouchAction` class.

## 1. Understanding the W3C Actions API Process

The process for performing gestures using the W3C Actions API in Appium involves four key steps, as you correctly summarized:

1. **Create an Input Device**: Define a virtual input source (e.g., a finger for touch gestures) using `PointerInput`. This simulates a touch device, not a UI element.
2. **Initialize ActionBuilder**: Create an `ActionBuilder` instance with the Appium driver and input device to manage the sequence of gestures.
3. **Define Action Sequence**: Use `pointer_action` to chain actions (e.g., move, press, pause, release) on the target location or element.
4. **Perform Actions**: Execute the sequence using `perform()` to send the commands to the device.

### Clarification of Your Understanding
- **Step 1**: You described "getting the object with which you want to perform the action." This refers to creating a `TouchInput` object (e.g., `PointerInput(POINTER_TOUCH, "touch")`), which represents a virtual input device (like a finger), not a UI element. UI elements or coordinates are specified later in the action sequence.
- **Step 2**: Correct. The `ActionBuilder` is initialized with the driver and input device (`touch_input`) to build a sequence of actions.
- **Step 3**: Correct. The `pointer_action` object allows chaining actions (e.g., `move_to_location`, `pointer_down`, `pause`, `pointer_up`) to define the gesture.
- **Step 4**: Correct. `actions.perform()` executes the entire sequence.

Your understanding is accurate, with the minor clarification that the "object" in Step 1 is the input device (`PointerInput`), not a UI element. Below are detailed examples of various gestures, including your original long press and the requested pinch zoom.

## 2. Gesture Examples

Each example includes Python code, an explanation, and notes on usage. All examples assume an Appium driver (`driver`) is initialized (e.g., for Android with UiAutomator2 or iOS with XCUITest).

### 2.1 Long Press (Your Original Code)
**Goal**: Perform a long press at coordinates (10, 100) for 2 seconds.
**Code**:
```python
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Create touch input device
touch_input = PointerInput(POINTER_TOUCH, "touch")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=touch_input)

# Define long press sequence
pointer_action = actions.pointer_action
pointer_action.move_to_location(10, 100).pointer_down().pause(2).pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Input Device**: `PointerInput(POINTER_TOUCH, "touch")` creates a virtual finger for touch gestures.
- **Action Sequence**:
  - `move_to_location(10, 100)`: Moves the pointer to coordinates (x=10, y=100).
  - `pointer_down()`: Simulates pressing down (touching the screen).
  - `pause(2)`: Holds the press for 2 seconds, creating the long press effect.
  - `pointer_up()`: Releases the touch (lifts the finger).
- **Use Case**: Triggering a context menu or selecting an item with a long press.
- **Notes**:
  - Ensure coordinates (10, 100) are valid for your device’s resolution (use Appium Inspector to verify).
  - For element-based long press, use `element.location['x']` and `element.location['y']` instead of hard-coded coordinates.
  - Alternative: Use `mobile: touchAndHold` (iOS) or `mobile: longClickGesture` (Android) via `execute_script` for simpler long press.

### 2.2 Tap on an Element
**Goal**: Perform a single tap on a UI element (e.g., a button).
**Code**:
```python
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Find the element to tap
element = driver.find_element(AppiumBy.ID, "com.example.app:id/button")

# Create touch input
touch_input = PointerInput(POINTER_TOUCH, "touch")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=touch_input)

# Define tap sequence
pointer_action = actions.pointer_action
pointer_action.move_to_location(element.location['x'] + element.size['width'] // 2, 
                               element.location['y'] + element.size['height'] // 2)
pointer_action.pointer_down().pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Element**: `find_element` locates the button by ID.
- **Coordinates**: `element.location` provides the top-left corner; adding `size['width'] // 2` and `size['height'] // 2` targets the element’s center for accuracy.
- **Action Sequence**: Quick `pointer_down()` and `pointer_up()` simulate a tap.
- **Use Case**: Clicking a button to submit a form or navigate.
- **Notes**:
  - Prefer element-based taps over coordinates for cross-device compatibility.
  - For simple taps, `element.click()` may suffice, but W3C Actions API is more reliable for custom gestures.

### 2.3 Swipe to Scroll
**Goal**: Swipe from (100, 500) to (100, 200) to scroll up.
**Code**:
```python
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Create touch input
touch_input = PointerInput(POINTER_TOUCH, "finger1")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=touch_input)

# Define swipe sequence
pointer_action = actions.pointer_action
pointer_action.move_to_location(100, 500).pointer_down().move_to_location(100, 200).pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Coordinates**: Starts at (100, 500) and moves to (100, 200), simulating an upward swipe.
- **Action Sequence**: `move_to_location` after `pointer_down` performs the swipe motion.
- **Use Case**: Scrolling a list or navigating a carousel.
- **Notes**:
  - Adjust coordinates based on screen resolution.
  - For element-based swipes, use a scrollable container’s coordinates.
  - Alternative: Use `mobile: swipeGesture` (Android) via `execute_script`.

### 2.4 Pinch Zoom (Zoom In)
**Goal**: Perform a pinch zoom-in gesture on an element (e.g., a map).
**Code**:
```python
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Find the element to zoom
element = driver.find_element(AppiumBy.ID, "com.example.app:id/map_view")

# Get element center and size
center_x = element.location['x'] + element.size['width'] // 2
center_y = element.location['y'] + element.size['height'] // 2
offset = 100  # Distance fingers move outward

# Create two touch inputs for multi-touch
finger1 = PointerInput(POINTER_TOUCH, "finger1")
finger2 = PointerInput(POINTER_TOUCH, "finger2")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=finger1)

# Define pinch zoom-in sequence for finger1
pointer1 = actions.pointer_action
pointer1.move_to_location(center_x - offset, center_y).pointer_down()
pointer1.move_to_location(center_x - offset * 2, center_y)

# Add second pointer for finger2
actions.add_pointer_input(POINTER_TOUCH, "finger2")
pointer2 = actions.pointer_action
pointer2.move_to_location(center_x + offset, center_y).pointer_down()
pointer2.move_to_location(center_x + offset * 2, center_y)

# Release both fingers
pointer1.pointer_up()
pointer2.pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Element**: Targets a map view for zooming.
- **Multi-Touch**: Uses two `PointerInput` objects (`finger1`, `finger2`) to simulate two fingers.
- **Coordinates**:
  - Starts with fingers close to the center (`center_x ± offset`).
  - Moves fingers outward (`center_x ± offset * 2`) to zoom in.
- **Action Sequence**: Both fingers press, move apart, and release simultaneously.
- **Use Case**: Zooming in on a map or image.
- **Notes**:
  - Adjust `offset` based on the element size and desired zoom level.
  - For zoom out (pinch), reverse the movement (move fingers closer).
  - Alternative: Use `mobile: pinchOpenGesture` (Android) via `execute_script`.

### 2.5 Drag and Drop
**Goal**: Drag an element to another element’s location.
**Code**:
```python
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Find source and target elements
source_element = driver.find_element(AppiumBy.ID, "com.example.app:id/draggable_item")
target_element = driver.find_element(AppiumBy.ID, "com.example.app:id/target_area")

# Create touch input
touch_input = PointerInput(POINTER_TOUCH, "touch")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=touch_input)

# Define drag-and-drop sequence
pointer_action = actions.pointer_action
pointer_action.move_to_location(source_element.location['x'] + source_element.size['width'] // 2,
                               source_element.location['y'] + source_element.size['height'] // 2)
pointer_action.pointer_down()
pointer_action.move_to_location(target_element.location['x'] + target_element.size['width'] // 2,
                               target_element.location['y'] + target_element.size['height'] // 2)
pointer_action.pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Elements**: `source_element` is draggable; `target_element` is the drop zone.
- **Coordinates**: Uses element centers for precise dragging.
- **Action Sequence**: Moves to source, presses, moves to target, and releases.
- **Use Case**: Reordering list items or moving objects in a game.
- **Notes**:
  - Ensure elements are interactable (use Appium Inspector to verify).
  - Alternative: Use `gesture: dragAndDrop` via `appium-gestures-plugin`.

### 2.6 Multi-Touch (Two-Finger Tap)
**Goal**: Perform a two-finger tap on an element.
**Code**:
```python
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from appium.webdriver.common.actions.action_builder import ActionBuilder

# Find the element to tap
element = driver.find_element(AppiumBy.ID, "com.example.app:id/map_view")

# Get element center
center_x = element.location['x'] + element.size['width'] // 2
center_y = element.location['y'] + element.size['height'] // 2
offset = 20  # Distance between fingers

# Create two touch inputs
finger1 = PointerInput(POINTER_TOUCH, "finger1")
finger2 = PointerInput(POINTER_TOUCH, "finger2")

# Initialize ActionBuilder
actions = ActionBuilder(driver, mouse=finger1)

# Define two-finger tap for finger1
pointer1 = actions.pointer_action
pointer1.move_to_location(center_x - offset, center_y).pointer_down().pointer_up()

# Add second pointer for finger2
actions.add_pointer_input(POINTER_TOUCH, "finger2")
pointer2 = actions.pointer_action
pointer2.move_to_location(center_x + offset, center_y).pointer_down().pointer_up()

# Perform the action
actions.perform()
```
**Explanation**:
- **Element**: Targets a map view for a two-finger tap.
- **Multi-Touch**: Uses two `PointerInput` objects for simultaneous taps.
- **Coordinates**: Places fingers slightly apart (`center_x ± offset`) for a natural two-finger gesture.
- **Action Sequence**: Both fingers tap (press and release) at the same time.
- **Use Case**: Triggering a map action (e.g., reset view) or zooming.
- **Notes**:
  - Adjust `offset` to match the app’s expected finger spacing.
  - For iOS, consider `mobile: twoFingerTap` via `execute_script` as an alternative.

## 3. Key Concepts

- **PointerInput**:
  - Simulates an input device (e.g., finger for `POINTER_TOUCH`).
  - Requires a unique name (e.g., "touch", "finger1") for each input, especially in multi-touch gestures.
  - Use `POINTER_TOUCH` for mobile touchscreens.

- **ActionBuilder**:
  - Manages action sequences for one or more input devices.
  - `pointer_action` handles touch/mouse gestures; `key_action` (unused in these examples) handles keyboard inputs.
  - Use `add_pointer_input` for multi-touch gestures.

- **Action Sequence**:
  - Actions are chained (e.g., `move_to_location`, `pointer_down`, `pointer_up`).
  - Coordinates are viewport-based (top-left is (0, 0)).
  - Ensure valid sequences (e.g., `pointer_down` before `pointer_up`).

- **Performing Actions**:
  - `actions.perform()` sends the sequence to the Appium server for execution.
  - Ensure the driver is properly initialized (e.g., `webdriver.Remote`).

## 4. Notes
- **Coordinates vs. Elements**: Use element coordinates (`element.location`, `element.size`) for cross-device compatibility. Hard-coded coordinates (e.g., (10, 100)) may break on different screen resolutions.
- **Platform Differences**:
  - Android (UiAutomator2) and iOS (XCUITest) support W3C Actions API, but iOS may require longer durations for some gestures (e.g., long press).
  - Test on real devices or emulators/simulators to verify behavior.
- **Dependencies**:
  - Use `appium-python-client>=3.0.0` and `selenium>=4`.
  - Ensure Appium server is version 2.0+.
- **Troubleshooting**:
  - Verify coordinates and element IDs with Appium Inspector`.
  - Check Appium server logs for errors - Check server logs for errors.
  - Ensure sufficient durations (e.g., 1000–2000ms for long press).
  - If a gesture fails, try alternatives like `mobile:` commands (e.g., `mobile: pinchOpenGesture` for Android).
- **Alternatives**:
  - For simple gestures, consider `mobile:` commands via `driver.execute_script` (e.g., `mobile: touchAndHold` for iOS, `mobile: longClickGesture` for Android).
  - The `appium-gestures-plugin` provides additional commands like `gesture: dragAndDrop` (install via `appium plugin install gestures`).

## 5. Example Driver Setup
```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "description": "emulator-5554",
    "appPackage": "com.example.app",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
# Perform gesture actions as shown above
driver.quit()
```

## 6. References
- **Appium Documentation**:
  - [Appium Documentation](https://appium.io/docs/2.0/en/5/w3c-actions/): Guide to W3C Actions API in Appium.
  - [UiAutomator2 Driver](https://appium.io/docs/en/stable/drivers/android-uiautomator2/): Android-specific commands and capabilities.
  - [XCUITest Driver](https://appium.io/docs/stable/en/drivers/ios-xcuitest/): iOS-specific commands and capabilities.
- **Selenium Documentation**:
  - [Selenium Actions API](https://www.selenium.devium.dev/documentation/stable/webdriver/actions_api/): Details the W3C Actions API used by Appium.
- **Appium Python Client**:
  - [GitHub: appium-python-client](https://github.com/appium/appium-python-client): Python client library documentation and examples.
- **Appium Gestures Plugin**:
  - [appium-Gestures-Plugin](https://github.com/appium/appium-gestures-plugin): Additional gesture commands for Appium.