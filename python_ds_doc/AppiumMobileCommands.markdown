# Appium Mobile Commands Reference

This document provides a comprehensive reference for all mobile-specific commands in Appium 2.0, including gestures, network, and device control commands, as documented in the official Appium documentation (UiAutomator2 and XCUITest drivers) and related sources. Commands are executed using `driver.execute_script` (Python) or equivalent in other languages. Examples are provided in Python for clarity.

## 1. Mobile Gesture Commands

These commands simulate user interactions like taps, swipes, and pinches. Most are supported by the UiAutomator2 driver (Android) and XCUITest driver (iOS).

### 1.1 Long Press
- **Command**: `mobile: longClickGesture` (Android, UiAutomator2, since 1.19); `mobile: touchAndHold` (iOS, XCUITest)
- **Description**: Tap and hold an element or coordinates for a specified duration (e.g., to open a context menu).
- **Platforms**: Android, iOS
- **Parameters**:
  - `elementId`: ID of the element (optional, use `element.id` in Python).
  - `x`, `y`: Screen coordinates (optional, required if no `elementId`).
  - `duration`: Duration in milliseconds (Android) or seconds (iOS, typically 1.0–2.0).
- **Example**:
  ```python
  # Android
  driver.execute_script('mobile: longClickGesture', {'elementId': element.id, 'duration': 1000})
  # iOS
  driver.execute_script('mobile: touchAndHold', {'element': element.id, 'duration': 2.0})
  ```

### 1.2 Tap/Click
- **Command**: `mobile: clickGesture` (Android, UiAutomator2, since 1.71.0)
- **Description**: Performs a single tap/click on an element or coordinates, useful when native tap fails.
- **Platforms**: Android
- **Parameters**:
  - `elementId`: ID of the element (optional).
  - `x`, `y`: Coordinates (required if no `elementId`).
- **Example**:
  ```python
  driver.execute_script('mobile: clickGesture', {'x': 100, 'y': 100})
  ```

### 1.3 Double Tap
- **Command**: `mobile: doubleClickGesture` (Android, UiAutomator2, since 1.21); `mobile: doubleTap` (iOS, XCUITest)
- **Description**: Performs a double tap on an element or coordinates.
- **Platforms**: Android, iOS
- **Parameters**:
  - `elementId`: ID of the element (optional).
  - `x`, `y`: Coordinates (required if no `elementId`).
- **Example**:
  ```python
  # Android
  driver.execute_script('mobile: doubleClickGesture', {'elementId': element.id})
  # iOS
  driver.execute_script('mobile: doubleTap', {'element': element.id})
  ```

### 1.4 Swipe
- **Command**: `mobile: swipeGesture` (Android, UiAutomator2, since 1.19)
- **Description**: Performs a swipe gesture (e.g., left, right, up, down) on an element or screen area.
- **Platforms**: Android
- **Parameters**:
  - `elementId`: ID of the element (optional).
  - `left`, `top`, `width`, `height`: Bounding area for swipe (required if no `elementId`).
  - `direction`: `up`, `down`, `left`, or `right`.
  - `percent`: Swipe distance as a percentage of the area (0.0–1.0).
  - `speed`: Pixels per second (default: 5000 * displayDensity).
- **Example**:
  ```python
  driver.execute_script('mobile: swipeGesture', {'elementId': element.id, 'direction': 'left', 'percent': 0.5})
  ```

### 1.5 Scroll
- **Command**: `mobile: scrollGesture` (Android, UiAutomator2, since 1.19); `mobile: scroll` (iOS, XCUITest)
- **Description**: Scrolls an element or screen area until a condition is met (e.g., element visible).
- **Platforms**: Android, iOS
- **Parameters**:
  - `elementId`: ID of the scrollable element (optional).
  - `left`, `top`, `width`, `height`: Scroll area (required if no `elementId`).
  - `direction`: `up`, `down`, `left`, or `right`.
  - `percent`: Scroll distance as a percentage (0.0–1.0).
  - `speed`: Pixels per second (default: 5000 * displayDensity, Android only).
  - `strategy`, `selector`: For element-based scrolling (e.g., `accessibility id`, `Picker`, iOS only).
- **Example**:
  ```python
  # Android
  driver.execute_script('mobile: scrollGesture', {'left': 100, 'top': 100, 'width': 200, 'height': 200, 'direction': 'down', 'percent': 3.0})
  # iOS
  driver.execute_script('mobile: scroll', {'direction': 'down'})
  ```

### 1.6 Pinch (Zoom In/Out)
- **Command**: `mobile: pinchCloseGesture` (zoom out), `mobile: pinchOpenGesture` (zoom in) (Android, UiAutomator2, since 1.19)
- **Description**: Simulates pinch-to-zoom on an element or area.
- **Platforms**: Android
- **Parameters**:
  - `elementId`: ID of the element (optional).
  - `left`, `top`, `width`, `height`: Pinch area (required if no `elementId`).
  - `percent`: Pinch size as a percentage (0.0–1.0, mandatory).
  - `speed`: Pixels per second (default: 2500 * displayDensity).
- **Example**:
  ```python
  driver.execute_script('mobile: pinchCloseGesture', {'elementId': element.id, 'percent': 0.75})
  ```

### 1.7 Drag and Drop
- **Command**: `mobile: dragGesture` (Android, UiAutomator2, since 1.19); `mobile: dragFromToForDuration` (iOS, XCUITest)
- **Description**: Drags an element or coordinates to a target point.
- **Platforms**: Android, iOS
- **Parameters**:
  - `elementId`: ID of the element to drag (optional, Android).
  - `startX`, `startY`: Starting coordinates (required if no `elementId`, Android).
  - `endX`, `endY`: Target coordinates (Android).
  - `speed`: Pixels per second (default: 2500 * displayDensity, Android).
  - iOS-specific: `duration` (seconds), `fromX`, `fromY`, `toX`, `toY`.
- **Example**:
  ```python
  # Android
  driver.execute_script('mobile: dragGesture', {'elementId': element.id, 'endX': 100, 'endY': 100})
  # iOS
  driver.execute_script('mobile: dragFromToForDuration', {'element': element.id, 'fromX': 100, 'fromY': 100, 'toX': 200, 'toY': 200, 'duration': 2.0})
  ```
- **Plugin Alternative**: `gesture: dragAndDrop` (via `appium-gestures-plugin`)
  ```python
  driver.execute_script('gesture: dragAndDrop', {'sourceId': el1.id, 'destinationId': el2.id})
  ```

### 1.8 Fling
- **Command**: `mobile: flingGesture` (Android, UiAutomator2, since 1.19)
- **Description**: Performs a quick swipe (fling) on an element or area.
- **Platforms**: Android
- **Parameters**:
  - `elementId`: ID of the element (optional).
  - `left`, `top`, `width`, `height`: Fling area (required if no `elementId`).
  - `direction`: `up`, `down`, `left`, or `right`.
  - `speed`: Pixels per second (default: 5000 * displayDensity).
- **Example**:
  ```python
  driver.execute_script('mobile: flingGesture', {'elementId': element.id, 'direction': 'up', 'speed': 5000})
  ```

### 1.9 iOS-Specific Gestures
- **Command**: `mobile: selectPickerWheelValue`
  - **Description**: Selects a value in an iOS picker wheel (e.g., date picker).
  - **Platforms**: iOS
  - **Parameters**: `element`, `value`.
  - **Example**:
    ```python
    driver.execute_script('mobile: selectPickerWheelValue', {'element': element.id, 'value': '2023-01-01'})
    ```
- **Command**: `mobile: twoFingerTap`
  - **Description**: Performs a two-finger tap (e.g., for zooming in maps).
  - **Platforms**: iOS
  - **Parameters**: `element`.
  - **Example**:
    ```python
    driver.execute_script('mobile: twoFingerTap', {'element': element.id})
    ```
- **Command**: `mobile: tap`
  - **Description**: Taps an element or coordinates.
  - **Platforms**: iOS
  - **Parameters**: `x`, `y` or `element`.
  - **Example**:
    ```python
    driver.execute_script('mobile: tap', {'element': element.id})
    ```

## 2. Connection and Network Commands

These commands manage device connectivity and network settings, primarily for emulators/simulators.

### 2.1 Get Network Connection
- **Command**: `mobile: getNetworkConnection`
- **Description**: Retrieves the current network connection status (e.g., Wi-Fi, mobile data).
- **Platforms**: Android, iOS
- **Example**:
  ```python
  connection = driver.execute_script('mobile: getNetworkConnection')
  ```

### 2.2 Set Network Connection
- **Command**: `mobile: setNetworkConnection`
- **Description**: Sets network connection type (e.g., Wi-Fi, mobile data, airplane mode).
- **Platforms**: Android, iOS
- **Parameters**: `type` (bitmask: 0=disabled, 1=airplane mode, 2=Wi-Fi, 4=data, 6=Wi-Fi+data).
- **Example**:
  ```python
  driver.execute_script('mobile: setNetworkConnection', {'type': 2})  # Enable Wi-Fi only
  ```

### 2.3 Set Network Speed (Emulator Only)
- **Command**: `mobile: setNetworkSpeed`
- **Description**: Sets network speed (e.g., 4G, 3G).
- **Platforms**: Android
- **Parameters**: `networkSpeed` (e.g., `gsm`, `edge`, `hspa`, `lte`).
- **Example**:
  ```python
  driver.execute_script('mobile: setNetworkSpeed', {'networkSpeed': 'lte'})
  ```

### 2.4 GSM Call (Emulator Only)
- **Command**: `mobile: makeGSMCall`
- **Description**: Simulates a GSM call.
- **Platforms**: Android
- **Parameters**: `phoneNumber`, `action` (e.g., `call`, `accept`, `cancel`).
- **Example**:
  ```python
  driver.execute_script('mobile: makeGSMCall', {'phoneNumber': '1234567890', 'action': 'call'})
  ```

### 2.5 GSM Signal Strength (Emulator Only)
- **Command**: `mobile: setGSMSignal`
- **Description**: Sets GSM signal strength.
- **Platforms**: Android
- **Parameters**: `signalStrength` (0–4, 0=no signal, 4=full).
- **Example**:
  ```python
  driver.execute_script('mobile: setGSMSignal', {'signalStrength': 4})
  ```

### 2.6 GSM Voice State (Emulator Only)
- **Command**: `mobile: setGSMVoice`
- **Description**: Sets GSM voice state.
- **Platforms**: Android
- **Parameters**: `state` (e.g., `on`, `off`, `denied`).
- **Example**:
  ```python
  driver.execute_script('mobile: setGSMVoice', {'state': 'on'})
  ```

### 2.7 Simulate SMS (Emulator Only)
- **Command**: `mobile: sendSMS`
- **Description**: Simulates receiving an SMS.
- **Platforms**: Android
- **Parameters**: `phoneNumber`, `message`.
- **Example**:
  ```python
  driver.execute_script('mobile: sendSMS', {'phoneNumber': '1234567890', 'message': 'Test SMS'})
  ```

## 3. Other Mobile Commands

These commands handle device control, app management, and other functionalities.

### 3.1 Get Device Information
- **Command**: `mobile: getDeviceInfo`
- **Description**: Retrieves device details (e.g., manufacturer, model, timezone).
- **Platforms**: Android, iOS
- **Example**:
  ```python
  info = driver.execute_script('mobile: getDeviceInfo')
  ```

### 3.2 Get Device Time
- **Command**: `mobile: getDeviceTime`
- **Description**: Gets the device’s current time (format: ISO-8601, e.g., `YYYY-MM-DDTHH:mm:ssZ`).
- **Platforms**: Android, iOS
- **Example**:
  ```python
  time = driver.execute_script('mobile: getDeviceTime')
  ```

### 3.3 Press Physical Button
- **Command**: `mobile: pressButton`
- **Description**: Simulates pressing a physical button (e.g., home, volume up/down). iOS simulators only support `home`.
- **Platforms**: Android, iOS
- **Parameters**: `name` (`home`, `volumeup`, `volumedown`).
- **Example**:
  ```python
  driver.execute_script('mobile: pressButton', {'name': 'home'})
  ```

### 3.4 App Management
- **Command**: `mobile: activateApp`
  - **Description**: Activates an installed app.
  - **Platforms**: Android, iOS
  - **Parameters**: `bundleId` (iOS) or `appPackage` (Android).
  - **Example**:
    ```python
    driver.execute_script('mobile: activateApp', {'bundleId': 'com.example.app'})  # iOS
    ```
- **Command**: `mobile: terminateApp`
  - **Description**: Closes an app.
  - **Platforms**: Android, iOS
  - **Parameters**: `bundleId` or `appPackage`.
  - **Example**:
    ```python
    driver.execute_script('mobile: terminateApp', {'bundleId': 'com.example.app'})
    ```
- **Command**: `mobile: launchApp`
  - **Description**: Launches an app (deprecated; use `mobile: activateApp`).
  - **Platforms**: Android, iOS
- **Command**: `mobile: backgroundApp`
  - **Description**: Sends the app to the background.
  - **Platforms**: Android, iOS
  - **Parameters**: `seconds` (optional, default: indefinitely).
  - **Example**:
    ```python
    driver.execute_script('mobile: backgroundApp', {'seconds': 5})
    ```

### 3.5 Biometric Authentication (iOS Simulator Only)
- **Command**: `mobile: performBiometric`
  - **Description**: Simulates biometric input (Touch ID or Face ID).
  - **Platforms**: iOS
  - **Parameters**: `type` (`touchId`, `faceId`), `match` (boolean, true for matching input).
  - **Example**:
    ```python
    driver.execute_script('mobile: performBiometric', {'type': 'faceId', 'match': True})
    ```
- **Command**: `mobile: isBiometricEnrolled`
  - **Description**: Checks if biometric is enrolled.
  - **Platforms**: iOS
  - **Example**:
    ```python
    enrolled = driver.execute_script('mobile: isBiometricEnrolled')
    ```

### 3.6 File Operations
- **Command**: `mobile: deleteFile`
- **Description**: Deletes a file on the device.
- **Platforms**: Android, iOS
- **Parameters**: `remotePath` (full path or path in app bundle).
- **Example**:
  ```python
  driver.execute_script('mobile: deleteFile', {'remotePath': '/path/to/file'})
  ```

### 3.7 Service Management (Android)
- **Command**: `mobile: startService`
  - **Description**: Starts an Android service.
  - **Platforms**: Android
  - **Parameters**: `intent`, `user` (optional), `foreground` (boolean).
  - **Example**:
    ```python
    driver.execute_script('mobile: startService', {'intent': 'com.example/.Service', 'foreground': True})
    ```
- **Command**: `mobile: stopService`
  - **Description**: Stops an Android service.
  - **Platforms**: Android
  - **Parameters**: `intent`.
  - **Example**:
    ```python
    driver.execute_script('mobile: stopService', {'intent': 'com.example/.Service'})
    ```

### 3.8 Toast Message Check (Android)
- **Command**: `mobile: isToastVisible`
- **Description**: Checks if a toast message is visible.
- **Platforms**: Android
- **Parameters**: `text` (message text), `isRegexp` (boolean, optional).
- **Example**:
  ```python
  is_visible = driver.execute_script('mobile: isToastVisible', {'text': 'Saved'})
  ```

### 3.9 Open Drawer (Android)
- **Command**: `mobile: openDrawer`
- **Description**: Opens a drawer with specified gravity.
- **Platforms**: Android
- **Parameters**: `gravity` (optional, default: `GravityCompat.START`).
- **Example**:
  ```python
  driver.execute_script('mobile: openDrawer', {'gravity': 'start'})
  ```

### 3.10 System Logs
- **Command**: `mobile: startLogsBroadcast`
- **Description**: Starts a WebSocket broadcast of system logs (`syslog` for iOS, `logcat` for Android).
- **Platforms**: Android, iOS
- **Example**:
  ```python
  driver.execute_script('mobile: startLogsBroadcast')
  ```

### 3.11 SMS List (Android)
- **Command**: `mobile: getSmsList`
- **Description**: Retrieves SMS messages as JSON.
- **Platforms**: Android
- **Example**:
  ```python
  sms_list = driver.execute_script('mobile: getSmsList')
  ```

### 3.12 Battery State (Android Emulator Only)
- **Command**: `mobile: setBatteryPercentage`
  - **Description**: Sets battery percentage.
  - **Platforms**: Android
  - **Parameters**: `percentage` (0–100).
  - **Example**:
    ```python
    driver.execute_script('mobile: setBatteryPercentage', {'percentage': 50})
    ```
- **Command**: `mobile: setBatteryState`
  - **Description**: Sets battery charger state.
  - **Platforms**: Android
  - **Parameters**: `state` (`connected`, `disconnected`).
  - **Example**:
    ```python
    driver.execute_script('mobile: setBatteryState', {'state': 'connected'})
    ```

### 3.13 Permissions (Android)
- **Command**: `mobile: changePermissions`
- **Description**: Grants or revokes app permissions.
- **Platforms**: Android
- **Parameters**: `action` (`grant`, `revoke`), `appPackage`, `permissions` (e.g., `android.permission.READ_CONTACTS`).
- **Example**:
  ```python
  driver.execute_script('mobile: changePermissions', {'action': 'grant', 'appPackage': 'com.example.app', 'permissions': 'android.permission.READ_CONTACTS'})
  ```

### 3.14 Execute Shell Command
- **Command**: `mobile: shell`
- **Description**: Executes a shell command on the device.
- **Platforms**: Android, iOS
- **Parameters**: `command`, `args` (list).
- **Example**:
  ```python
  driver.execute_script('mobile: shell', {'command': 'echo', 'args': ['Hello']})
  ```

## 4. Notes
- **Platform Specificity**: Commands are marked as Android, iOS, or emulator/simulator-only. For example, `mobile: makeGSMCall` works only on Android emulators.
- **Appium Version**: Most gesture commands require Appium 1.19+ (UiAutomator2) or 1.6.4+ (XCUITest). Use Appium 2.0+ with the latest client libraries (e.g., `appium-python-client>=3.0.0`).
- **TouchAction Deprecation**: `TouchAction` and `MultiTouchAction` are deprecated in Appium 2.0. Use W3C Actions API or `mobile:` commands for better reliability.
- **Plugin Support**: The `appium-gestures-plugin` adds commands like `gesture: dragAndDrop`. Install via `appium plugin install gestures`.
- **Execution Syntax**: Use `driver.execute_script('mobile: <command>', params)` in Python, where `params` is a dictionary. Ensure parameters are JSON-serializable.
- **Troubleshooting**:
  - Verify element IDs with Appium Inspector.
  - Check Appium server logs for errors.
  - Ensure sufficient gesture duration (e.g., 1000–2000ms for long press).
  - For iOS, prefer `mobile: touchAndHold` over `TouchAction` for long press due to historical bugs.
- **Documentation**: Refer to [Appium UiAutomator2 Driver](https://appium.io/docs/en/drivers/android-uiautomator2/), [XCUITest Driver](https://appium.io/docs/en/drivers/ios-xcuitest/), and [Appium 2.0 Docs](https://appium.io/docs/en/2.0/) for updates.

## 5. Example Setup (Python)
```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "emulator-5554",
    "appPackage": "com.example.app",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
element = driver.find_element(AppiumBy.ID, "your_element_id")
driver.execute_script('mobile: longClickGesture', {'elementId': element.id, 'duration': 1000})
driver.quit()
```