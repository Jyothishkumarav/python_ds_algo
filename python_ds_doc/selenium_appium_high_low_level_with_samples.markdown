# Selenium ActionChains and Appium ActionHelpers: High-Level Actions, Sample Code, and Low-Level Implementations

This document details the high-level actions provided by Selenium 4.0’s `ActionChains` and Appium’s `ActionHelpers`, along with sample Python client code and their low-level W3C WebDriver-compliant implementations. Each high-level action includes a sample code snippet demonstrating its usage, followed by the exact low-level implementation code with original docstrings from `action_chains.py` (Selenium) and `action_helpers.py` (Appium). This structure enhances readability and provides a clear understanding of how complex interactions are executed in browser and mobile automation.

## Overview

### Selenium ActionChains
- **File Reference**: `action_chains.py`
- **Purpose**: Automates browser interactions such as mouse movements, clicks, key presses, and scrolling.
- **W3C Compliance**: Uses the W3C WebDriver protocol, replacing the JSON Wire Protocol, for standardized action sequences across browsers (e.g., Chrome, Firefox, Edge).
- **Key Features**: Queues actions via `ActionBuilder`, executes them with `perform()`, and supports input sources (`PointerInput`, `KeyInput`, `WheelInput`).

### Appium ActionHelpers
- **File Reference**: `action_helpers.py`
- **Purpose**: Extends Selenium’s `ActionChains` for mobile-specific gestures (e.g., tap, swipe, scroll) on Android and iOS.
- **W3C Compliance**: Leverages W3C WebDriver with `PointerInput` for touch-based actions, compatible with mobile drivers (e.g., UIAutomator2 for Android, XCUITest for iOS).
- **Key Features**: Abstracts mobile gestures into high-level methods with duration control for timing.

### W3C WebDriver Compliance
- Both frameworks use `ActionBuilder` to construct W3C-compliant action sequences, ensuring consistent behavior across browsers and mobile platforms.
- Actions are translated into JSON payloads with precise coordinates and timing, sent to the WebDriver for execution.

## Selenium ActionChains: High-Level Actions, Sample Code, and Low-Level Implementations

Below are the high-level actions from `ActionChains` in `action_chains.py`, each with a sample code snippet and the corresponding low-level implementation, including original docstrings.

### 1. Click
- **High-Level Action**: `click(on_element=None)`
  - **Description**: Clicks an element or the current mouse position.
  - **Usage**: Simulates a left mouse click.
- **Sample Code**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains

  driver = webdriver.Chrome()
  try:
      driver.get("https://example.com")
      button = driver.find_element(By.ID, "submit-button")
      actions = ActionChains(driver)
      actions.click(button).perform()
  finally:
      driver.quit()
  ```
  - **Explanation**: Clicks a submit button, triggering a W3C-compliant click action.
- **Low-Level Implementation** (from `action_chains.py`):
  ```python
  def click(self, on_element=None):
      """Clicks an element.

      :Args:
       - on_element: The element to click.
         If None, clicks on current mouse position.
      """
      if on_element:
          self.move_to_element(on_element)
      self.w3c_actions.pointer_action.click()
      self.w3c_actions.key_action.pause()
      self.w3c_actions.key_action.pause()
      return self
  ```
  - **Explanation**:
    - If `on_element` is provided, moves the mouse to its center using `move_to_element` (W3C `pointerMove`).
    - Calls `pointer_action.click()`, generating W3C `pointerDown` and `pointerUp` events.
    - Adds two `pause()` calls to the keyboard action queue for synchronization.
    - Queues actions in `ActionBuilder` for execution.

### 2. Drag and Drop
- **High-Level Action**: `drag_and_drop(source, target)`
  - **Description**: Drags the source element to the target element.
  - **Usage**: Simulates dragging an element to another location.
- **Sample Code**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains

  driver = webdriver.Chrome()
  try:
      driver.get("https://jqueryui.com/droppable/")
      driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame"))
      source = driver.find_element(By.ID, "draggable")
      target = driver.find_element(By.ID, "droppable")
      actions = ActionChains(driver)
      actions.drag_and_drop(source, target).perform()
  finally:
      driver.quit()
  ```
  - **Explanation**: Drags a draggable element to a droppable area, using a W3C-compliant sequence.
- **Low-Level Implementation** (from `action_chains.py`):
  ```python
  def drag_and_drop(self, source, target):
      """Holds down the left mouse button on the source element, then moves
      to the target element and releases the mouse button.

      :Args:
       - source: The element to mouse down.
       - target: The element to mouse up.
      """
      self.click_and_hold(source)
      self.release(target)
      return self

  def click_and_hold(self, on_element=None):
      """Holds down the left mouse button on an element.

      :Args:
       - on_element: The element to mouse down.
         If None, clicks on current mouse position.
      """
      if on_element:
          self.move_to_element(on_element)
      self.w3c_actions.pointer_action.click_and_hold()
      self.w3c_actions.key_action.pause()
      return self

  def release(self, on_element=None):
      """Releasing a held mouse button on an element.

      :Args:
       - on_element: The element to mouse up.
         If None, releases on current mouse position.
      """
      if on_element:
          self.move_to_element(on_element)
      self.w3c_actions.pointer_action.release()
      self.w3c_actions.key_action.pause()
      return self
  ```
  - **Explanation**:
    - `drag_and_drop` combines `click_and_hold` and `release`.
    - `click_and_hold`: Moves to `source` (if provided) via `move_to_element` (`pointerMove`), then calls `pointer_action.click_and_hold()` for a W3C `pointerDown` event.
    - `release`: Moves to `target` (if provided) and calls `pointer_action.release()` for a W3C `pointerUp` event.
    - Sequence: move to source, press, move to target, release.
    - `ActionBuilder` constructs the W3C JSON payload.

### 3. Move to Element
- **High-Level Action**: `move_to_element(to_element)`
  - **Description**: Moves the mouse to the center of an element.
  - **Usage**: Simulates hovering over an element.
- **Sample Code**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains

  driver = webdriver.Chrome()
  try:
      driver.get("https://example.com")
      menu = driver.find_element(By.CSS_SELECTOR, ".nav")
      actions = ActionChains(driver)
      actions.move_to_element(menu).perform()
  finally:
      driver.quit()
  ```
  - **Explanation**: Hovers over a navigation menu, triggering a W3C-compliant mouse movement.
- **Low-Level Implementation** (from `action_chains.py`):
  ```python
  def move_to_element(self, to_element):
      """Moving the mouse to the middle of an element.

      :Args:
       - to_element: The WebElement to move to.
      """
      self.w3c_actions.pointer_action.move_to(to_element)
      self.w3c_actions.key_action.pause()
      return self
  ```
  - **Explanation**:
    - Calls `pointer_action.move_to(to_element)`, generating a W3C `pointerMove` action to the element’s in-view center.
    - Adds a `pause()` to the keyboard action queue for synchronization.
    - Queued in `ActionBuilder` for execution.

### 4. Send Keys
- **High-Level Action**: `send_keys(*keys_to_send)`
  - **Description**: Sends keys to the currently focused element.
  - **Usage**: Simulates typing text or modifier keys (e.g., Ctrl+C).
- **Sample Code**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains
  from selenium.webdriver.common.keys import Keys

  driver = webdriver.Chrome()
  try:
      driver.get("https://example.com")
      input_field = driver.find_element(By.ID, "search")
      actions = ActionChains(driver)
      actions.send_keys_to_element(input_field, "Hello", Keys.ENTER).perform()
  finally:
      driver.quit()
  ```
  - **Explanation**: Types "Hello" and presses Enter in a search field, using W3C-compliant keyboard actions.
- **Low-Level Implementation** (from `action_chains.py`):
  ```python
  def send_keys(self, *keys_to_send):
      """Sends keys to current focused element.

      :Args:
       - keys_to_send: The keys to send.  Modifier keys constants can be found in the
         'Keys' class.
      """
      typing = keys_to_typing(keys_to_send)
      for key in typing:
          self.key_down(key)
          self.key_up(key)
      return self

  def key_down(self, value, element=None):
      """Sends a key press only, without releasing it. Should only be used
      with modifier keys (Control, Alt and Shift).

      :Args:
       - value: The modifier key to send. Values are defined in `Keys` class.
       - element: The element to send keys.
         If None, sends a key to current focused element.

      Example, pressing ctrl+c::
          ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
      """
      if element:
          self.click(element)
      self.w3c_actions.key_action.key_down(value)
      self.w3c_actions.pointer_action.pause()
      return self

  def key_up(self, value, element=None):
      """Releases a modifier key.

      :Args:
       - value: The modifier key to send. Values are defined in Keys class.
       - element: The element to send keys.
         If None, sends a key to current focused element.

      Example, pressing ctrl+c::
          ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
      """
      if element:
          self.click(element)
      self.w3c_actions.key_action.key_up(value)
      self.w3c_actions.pointer_action.pause()
      return self
  ```
  - **Explanation**:
    - Converts `keys_to_send` to a list of characters using `keys_to_typing`.
    - For each key:
      - `key_down`: Generates a W3C `keyDown` event, optionally clicking an element first.
      - `key_up`: Generates a W3C `keyUp` event.
    - Adds `pause()` to the pointer action queue for synchronization.
    - `ActionBuilder` constructs the keyboard action sequence.

### 5. Scroll to Element
- **High-Level Action**: `scroll_to_element(element)`
  - **Description**: Scrolls an element into the viewport.
  - **Usage**: Ensures an element is visible by scrolling to it.
- **Sample Code**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains

  driver = webdriver.Chrome()
  try:
      driver.get("https://example.com/long-page")
      footer = driver.find_element(By.CSS_SELECTOR, "footer")
      actions = ActionChains(driver)
      actions.scroll_to_element(footer).perform()
  finally:
      driver.quit()
  ```
  - **Explanation**: Scrolls to a footer element, ensuring it’s visible, using a W3C-compliant wheel action.
- **Low-Level Implementation** (from `action_chains.py`):
  ```python
  def scroll_to_element(self, element: WebElement):
      """If the element is outside the viewport, scrolls the bottom of the
      element to the bottom of the viewport.

      :Args:
       - element: Which element to scroll into the viewport.
      """
      self.w3c_actions.wheel_action.scroll(origin=element)
      return self
  ```
  - **Explanation**:
    - Calls `wheel_action.scroll()` with the element as the origin, generating a W3C `wheel` action.
    - Ensures the element’s bottom is aligned with the viewport’s bottom.
    - Queued in `ActionBuilder` for execution.

## Appium ActionHelpers: High-Level Actions, Sample Code, and Low-Level Implementations

Below are the high-level actions from `ActionHelpers` in `action_helpers.py`, each with a sample code snippet and the corresponding low-level implementation, including original docstrings.

### 1. Scroll
- **High-Level Action**: `scroll(origin_el, destination_el, duration=None)`
  - **Description**: Scrolls from one element to another.
  - **Usage**: Simulates a touch-based scroll gesture on a mobile device.
- **Sample Code**:
  ```python
  from appium import webdriver
  from appium.webdriver.common.appiumby import AppiumBy

  desired_caps = {
      "platformName": "Android",
      "appium:deviceName": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.example.app",
      "appium:appActivity": ".MainActivity"
  }

  driver = webdriver.Remote("http://localhost:4723", desired_caps)
  try:
      origin_el = driver.find_element(AppiumBy.ID, "com.example.app:id/start_element")
      destination_el = driver.find_element(AppiumBy.ID, "com.example.app:id/end_element")
      driver.scroll(origin_el, destination_el, duration=1000)
  finally:
      driver.quit()
  ```
  - **Explanation**: Scrolls from one element to another in a mobile app, using a W3C-compliant touch sequence.
- **Low-Level Implementation** (from `action_helpers.py`):
  ```python
  def scroll(self, origin_el: WebElement, destination_el: WebElement, duration: Optional[int] = None) -> 'WebDriver':
      """Scrolls from one element to another

      Args:
          origin_el: the element from which to begin scrolling (center of element)
          destination_el: the element to scroll to (center of element)
          duration: defines speed of scroll action when moving from originalEl to destinationEl.
              Default is 600 ms for W3C spec.

      Usage:
          driver.scroll(el1, el2)

      Returns:
          Union['WebDriver', 'ActionHelpers']: Self instance
      """
      # XCUITest x W3C spec has no duration by default in server side
      if duration is None:
          duration = 600

      touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")

      actions = ActionChains(self)
      actions.w3c_actions = ActionBuilder(self, mouse=touch_input)

      # https://github.com/SeleniumHQ/selenium/blob/3c82c868d4f2a7600223a1b3817301d0b04d28e4/py/selenium/webdriver/common/actions/pointer_actions.py#L83
      actions.w3c_actions.pointer_action.move_to(origin_el)
      actions.w3c_actions.pointer_action.pointer_down()
      # setup duration for second move only, assuming duration always has atleast default value
      actions.w3c_actions = ActionBuilder(self, mouse=touch_input, duration=duration)
      actions.w3c_actions.pointer_action.move_to(destination_el)
      actions.w3c_actions.pointer_action.release()
      actions.perform()
      return cast('WebDriver', self)
  ```
  - **Explanation**:
    - Creates a `PointerInput` with `interaction.POINTER_TOUCH` for touch input.
    - Initializes `ActionChains` and `ActionBuilder` with touch input.
    - Sequence:
      1. `move_to(origin_el)`: W3C `pointerMove` to the center of `origin_el`.
      2. `pointer_down()`: W3C `pointerDown` to start the touch.
      3. `move_to(destination_el)`: W3C `pointerMove` to `destination_el` with specified `duration`.
      4. `release()`: W3C `pointerUp` to end the touch.
    - Calls `perform()` to execute the W3C action sequence.

### 2. Drag and Drop
- **High-Level Action**: `drag_and_drop(origin_el, destination_el)`
  - **Description**: Drags an element to another element’s position.
  - **Usage**: Simulates a touch-based drag gesture.
- **Sample Code**:
  ```python
  from appium import webdriver
  from appium.webdriver.common.appiumby import AppiumBy

  desired_caps = {
      "platformName": "Android",
      "appium:deviceName": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.example.app",
      "appium:appActivity": ".MainActivity"
  }

  driver = webdriver.Remote("http://localhost:4723", desired_caps)
  try:
      origin_el = driver.find_element(AppiumBy.ID, "com.example.app:id/draggable")
      destination_el = driver.find_element(AppiumBy.ID, "com.example.app:id/droppable")
      driver.drag_and_drop(origin_el, destination_el)
  finally:
      driver.quit()
  ```
  - **Explanation**: Drags an element to a droppable area in a mobile app, using a W3C-compliant touch sequence.
- **Low-Level Implementation** (from `action_helpers.py`):
  ```python
  def drag_and_drop(self, origin_el: WebElement, destination_el: WebElement) -> 'WebDriver':
      """Drag the origin element to the destination element

      Args:
          origin_el: the element to drag
          destination_el: the element to drag to

      Returns:
          Union['WebDriver', 'ActionHelpers']: Self instance
      """
      actions = ActionChains(self)
      # 'mouse' pointer action
      actions.w3c_actions.pointer_action.click_and_hold(origin_el)
      actions.w3c_actions.pointer_action.move_to(destination_el)
      actions.w3c_actions.pointer_action.release()
      actions.perform()
      return cast('WebDriver', self)
  ```
  - **Explanation**:
    - Uses `ActionChains` with a touch-based `PointerInput` (inherited from Selenium).
    - Sequence:
      1. `click_and_hold(origin_el)`: W3C `pointerMove` to `origin_el` and `pointerDown`.
      2. `move_to(destination_el)`: W3C `pointerMove` to `destination_el`.
      3. `release()`: W3C `pointerUp`.
    - Calls `perform()` to execute the W3C action sequence.

### 3. Tap
- **High-Level Action**: `tap(positions, duration=None)`
  - **Description**: Taps at specified coordinates with optional duration, supporting up to five fingers.
  - **Usage**: Simulates single or multi-finger taps.
- **Sample Code**:
  ```python
  from appium import webdriver
  from appium.webdriver.common.appiumby import AppiumBy

  desired_caps = {
      "platformName": "Android",
      "appium:deviceName": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.example.app",
      "appium:appActivity": ".MainActivity"
  }

  driver = webdriver.Remote("http://localhost:4723", desired_caps)
  try:
      driver.tap([(100, 200)], duration=500)
  finally:
      driver.quit()
  ```
  - **Explanation**: Taps at coordinates (100, 200) with a 500ms duration, using a W3C-compliant touch action.
- **Low-Level Implementation** (from `action_helpers.py`):
  ```python
  def tap(self, positions: List[Tuple[int, int]], duration: Optional[int] = None) -> 'WebDriver':
      """Taps on an particular place with up to five fingers, holding for a
      certain time

      Args:
          positions: an array of tuples representing the x/y coordinates of
              the fingers to tap. Length can be up to five.
          duration: length of time to tap, in ms

      Usage:
          driver.tap([(100, 20), (100, 60), (100, 100)], 500)

      Returns:
          Union['WebDriver', 'ActionHelpers']: Self instance
      """
      if len(positions) == 1:
          actions = ActionChains(self)
          actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
          x = positions[0][0]
          y = positions[0][1]
          actions.w3c_actions.pointer_action.move_to_location(x, y)
          actions.w3c_actions.pointer_action.pointer_down()
          if duration:
              actions.w3c_actions.pointer_action.pause(duration / 1000)
          else:
              actions.w3c_actions.pointer_action.pause(0.1)
          actions.w3c_actions.pointer_action.release()
          actions.perform()
      else:
          finger = 0
          actions = ActionChains(self)
          actions.w3c_actions.devices = []
          for position in positions:
              finger += 1
              x = position[0]
              y = position[1]
              new_input = actions.w3c_actions.add_pointer_input('touch', f'finger{finger}')
              new_input.create_pointer_move(x=x, y=y)
              new_input.create_pointer_down(button=MouseButton.LEFT)
              if duration:
                  new_input.create_pause(duration / 1000)
              else:
                  new_input.create_pause(0.1)
              new_input.create_pointer_up(button=MouseButton.LEFT)
          actions.perform()
      return cast('WebDriver', self)
  ```
  - **Explanation**:
    - **Single Tap**:
      - Uses `PointerInput` with `interaction.POINTER_TOUCH`.
      - Sequence: `move_to_location(x, y)` (W3C `pointerMove`), `pointer_down()`, `pause(duration)`, `release()` (W3C `pointerUp`).
    - **Multi-Tap**:
      - Creates separate `PointerInput` instances for each finger (e.g., `finger1`, `finger2`).
      - For each finger: `create_pointer_move(x, y)`, `create_pointer_down()`, `create_pause()`, `create_pointer_up()`.
    - Calls `perform()` to execute the W3C action sequence.

### 4. Swipe
- **High-Level Action**: `swipe(start_x, start_y, end_x, end_y, duration=0)`
  - **Description**: Swipes from one point to another with optional duration.
  - **Usage**: Simulates a touch-based swipe gesture.
- **Sample Code**:
  ```python
  from appium import webdriver
  from appium.webdriver.common.appiumby import AppiumBy

  desired_caps = {
      "platformName": "Android",
      "appium:deviceName": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.example.app",
      "appium:appActivity": ".MainActivity"
  }

  driver = webdriver.Remote("http://localhost:4723", desired_caps)
  try:
      driver.swipe(start_x=100, start_y=800, end_x=100, end_y=200, duration=500)
  finally:
      driver.quit()
  ```
  - **Explanation**: Swipes up from (100, 800) to (100, 200) with a 500ms duration, using a W3C-compliant touch sequence.
- **Low-Level Implementation** (from `action_helpers.py`):
  ```python
  def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0) -> 'WebDriver':
      """Swipe from one point to another point, for an optional duration.

      Args:
          start_x: x-coordinate at which to start
          start_y: y-coordinate at which to start
          end_x: x-coordinate at which to stop
          end_y: y-coordinate at which to stop
          duration: defines the swipe speed as time taken to swipe from point a to point b, in ms.

      Usage:
          driver.swipe(100, 100, 100, 400)

      Returns:
          Union['WebDriver', 'ActionHelpers']: Self instance
      """
      touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
      actions = ActionChains(self)
      actions.w3c_actions = ActionBuilder(self, mouse=touch_input)
      actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
      actions.w3c_actions.pointer_action.pointer_down()
      if duration > 0:
          actions.w3c_actions = ActionBuilder(self, mouse=touch_input, duration=duration)
      actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
      actions.w3c_actions.pointer_action.release()
      actions.perform()
      return cast('WebDriver', self)
  ```
  - **Explanation**:
    - Creates a `PointerInput` with `interaction.POINTER_TOUCH`.
    - Sequence:
      1. `move_to_location(start_x, start_y)`: W3C `pointerMove` to start coordinates.
      2. `pointer_down()`: W3C `pointerDown`.
      3. `move_to_location(end_x, end_y)`: W3C `pointerMove` with optional `duration`.
      4. `release()`: W3C `pointerUp`.
    - Calls `perform()` to execute the W3C action sequence.

### 5. Flick
- **High-Level Action**: `flick(start_x, start_y, end_x, end_y)`
  - **Description**: Performs a quick swipe (flick) from one point to another.
  - **Usage**: Simulates a rapid touch gesture.
- **Sample Code**:
  ```python
  from appium import webdriver
  from appium.webdriver.common.appiumby import AppiumBy

  desired_caps = {
      "platformName": "Android",
      "appium:deviceName": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.example.app",
      "appium:appActivity": ".MainActivity"
  }

  driver = webdriver.Remote("http://localhost:4723", desired_caps)
  try:
      driver.flick(start_x=100, start_y=800, end_x=100, end_y=200)
  finally:
      driver.quit()
  ```
  - **Explanation**: Performs a quick swipe up from (100, 800) to (100, 200), using a W3C-compliant touch sequence.
- **Low-Level Implementation** (from `action_helpers.py`):
  ```python
  def flick(self, start_x: int, start_y: int, end_x: int, end_y: int) -> 'WebDriver':
      """Flick from one point to another point.

      Args:
          start_x: x-coordinate at which to start
          start_y: y-coordinate at which to start
          end_x: x-coordinate at which to stop
          end_y: y-coordinate at which to stop

      Usage:
          driver.flick(100, 100, 100, 400)

      Returns:
          Union['WebDriver', 'ActionHelpers']: Self instance
      """
      actions = ActionChains(self)
      actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
      actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
      actions.w3c_actions.pointer_action.pointer_down()
      actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
      actions.w3c_actions.pointer_action.release()
      actions.perform()
      return cast('WebDriver', self)
  ```
  - **Explanation**:
    - Similar to `swipe` but without duration, implying a faster gesture.
    - Sequence: `move_to_location(start_x, start_y)`, `pointer_down()`, `move_to_location(end_x, end_y)`, `release()`.
    - Uses `PointerInput` with `interaction.POINTER_TOUCH`.
    - Calls `perform()` to execute the W3C action sequence.

## Key Differences and W3C Compliance
- **Selenium ActionChains**:
  - Focuses on mouse, keyboard, and scroll interactions for browsers.
  - Uses `PointerInput`, `KeyInput`, and `WheelInput` for W3C actions.
  - Example: `drag_and_drop` generates `pointerDown`, `pointerMove`, `pointerUp`.
- **Appium ActionHelpers**:
  - Extends `ActionChains` for touch-based mobile gestures.
  - Uses `PointerInput` with `interaction.POINTER_TOUCH` for touch actions.
  - Example: `swipe` maps to a W3C touch sequence with duration control.
- **W3C Compliance**:
  - Both use `ActionBuilder` to create W3C-compliant JSON payloads.
  - Selenium emphasizes precision for browser interactions; Appium focuses on touch gestures for mobile.
  - W3C ensures consistent execution across platforms.

## Notes
- Replace `https://example.com` and `com.example.app` with actual URLs and app details.
- Ensure Appium server is running (e.g., `http://localhost:4723`) for Appium tests.
- Deprecated methods (e.g., `scroll()` in Selenium) should be replaced with newer APIs like `scroll_to_element()`.
- Test scripts on specific browsers/devices to ensure compatibility.
- The sample code assumes a working WebDriver setup (ChromeDriver for Selenium, Appium server for Android).