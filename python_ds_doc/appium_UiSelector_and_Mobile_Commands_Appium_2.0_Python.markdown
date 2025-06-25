```markdown
# UiSelector and Mobile Commands for Appium 2.0 with Python Client

The `UiSelector` class, part of the Android UiAutomator framework, is used in Appium 2.0 with the `UiAutomator2` driver to define criteria for selecting UI elements in Android applications during automation testing. The `AppiumBy.ANDROID_UIAUTOMATOR` locator strategy allows testers to locate elements using attributes like text, resource ID, or class name. Additionally, Appium 2.0 provides mobile-specific commands (e.g., `mobile: scroll`) via the `execute_script` method to perform gestures and interactions. This document details `UiSelector` methods for element selection, mobile commands for gestures (focusing on `mobile: scroll` and alternatives), and includes Python examples for each, along with a reference example for automating a contact creation in the Android Contacts app using the Python client.

## Overview

- **Purpose**: `UiSelector` locates UI elements, while mobile commands handle gestures and device interactions in Android automation with Appium 2.0.
- **Driver**: The `UiAutomator2` driver supports Android 5.0 (API level 21) and above.
- **Locator Strategy**: Use `AppiumBy.ANDROID_UIAUTOMATOR` for `UiSelector` in Python (replacing deprecated `MobileBy`).
- **Mobile Commands**: Executed via `driver.execute_script('mobile: <command>', {...})` for gestures like scrolling, swiping, or pinching.
- **Key Classes**:
  - `UiSelector`: Defines selection criteria.
  - `UiScrollable`: Scrolls to elements in scrollable containers.
  - `UiObject2`: Represents UI elements (used internally).
- **Appium 2.0 Notes**:
  - Install the `UiAutomator2` driver: `appium driver install uiautomator2`.
  - Deprecated APIs (e.g., `TouchAction`, `MobileElement`) are replaced with W3C WebDriver actions or `WebElement`.
  - Set `appium:automationName` to `UiAutomator2` in desired capabilities.
- **Setup Requirements**:
  - Install Appium 2.0: `pip install appium-python-client`.
  - Install Android SDK and set `ANDROID_HOME`.
  - Use Python 3.7+ and install `selenium`: `pip install selenium`.
  - Configure an Android device/emulator with Developer Mode.
  - Start Appium server (port: 9510).

## UiSelector Methods for Selecting Elements

`UiSelector` methods are chained in a string passed to `driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, <selector>)`. The first matching element in the layout hierarchy is selected, or a `NoSuchElementException` is raised if none is found.

### Text-Based Selection

- **`text(String text)`**
  - Matches exact visible text (case-sensitive).
  - **Use Case**: Select a button labeled "OK".
  - **Python Example**:
    ```python
    from appium.webdriver.common.appiumby import AppiumBy
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
    element.click()
    ```

- **`textContains(String text)`**
  - Matches text containing the string (case-sensitive).
  - **Use Case**: Select "Cancel Order".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Cancel")')
    element.click()
    ```

- **`textStartsWith(String text)`**
  - Matches text starting with the string (case-insensitive).
  - **Use Case**: Select "Tasks" or "TOP CHARTS".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textStartsWith("T")')
    element.click()
    ```

- **`textMatches(String regex)`**
  - Matches text using a regular expression.
  - **Use Case**: Select "Chart 2025".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*Chart.*")')
    element.click()
    ```

### Content Description-Based Selection

- **`description(String desc)`**
  - Matches exact content-description (case-sensitive).
  - **Use Case**: Select an icon labeled "Apps".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apps")')
    element.click()
    ```

- **`descriptionContains(String desc)`**
  - Matches content-description containing the string (case-insensitive).
  - **Use Case**: Select "Settings".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Settings")')
    element.click()
    ```

- **`descriptionMatches(String regex)`**
  - Matches content-description using a regular expression.
  - **Use Case**: Select dynamic accessibility labels.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches(".*Home.*")')
    element.click()
    ```

### Class-Based Selection

- **`className(String className)`**
  - Matches by class name (e.g., `android.widget.Button`).
  - **Use Case**: Select buttons.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button")')
    element.click()
    ```

- **`classNameMatches(String regex)`**
  - Matches class name using a regular expression.
  - **Use Case**: Select `ImageView` or `TextView`.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().classNameMatches("android.widget.*View")')
    element.click()
    ```

### Resource ID-Based Selection

- **`resourceId(String resourceId)`**
  - Matches by resource ID (e.g., `com.example.app:id/button`).
  - **Use Case**: Stable identification of elements.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/result")')
    element.send_keys("Test")
    ```

- **`resourceIdMatches(String regex)`**
  - Matches resource ID using a regular expression.
  - **Use Case**: Select dynamic resource IDs.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceIdMatches(".*/button[0-9]")')
    element.click()
    ```

### State-Based Selection

- **`checked(boolean isChecked)`**
  - Matches checkable widgets in the checked state.
  - **Use Case**: Select checked checkboxes.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().checked(true)')
    element.click()
    ```

- **`enabled(boolean isEnabled)`**
  - Matches widgets in the enabled state.
  - **Use Case**: Select enabled buttons.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().enabled(true)')
    element.click()
    ```

- **`focused(boolean isFocused)`**
  - Matches widgets with focus.
  - **Use Case**: Select focused text fields.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().focused(true)')
    element.send_keys("Input")
    ```

- **`selected(boolean isSelected)`**
  - Matches selected widgets.
  - **Use Case**: Select selected list items.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().selected(true)')
    element.click()
    ```

- **`clickable(boolean isClickable)`**
  - Matches clickable widgets.
  - **Use Case**: Select buttons or links.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true)')
    element.click()
    ```

- **`longClickable(boolean isLongClickable)`**
  - Matches widgets supporting long-click.
  - **Use Case**: Select elements for long-press.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().longClickable(true)')
    driver.execute_script('mobile: longClick', {'element': element})
    ```

### Hierarchy-Based Selection

- **`childSelector(UiSelector selector)`**
  - Matches a child widget under a parent.
  - **Use Case**: Select a list item.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().text("Apps"))')
    element.click()
    ```

- **`fromParent(UiSelector selector)`**
  - Searches from a parent widget.
  - **Use Case**: Select siblings or children.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().fromParent(new UiSelector().text("Parent"))')
    element.click()
    ```

- **`instance(int instance)`**
  - Matches the nth instance (0-based).
  - **Use Case**: Select the third image.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)')
    element.click()
    ```

### Package-Based Selection

- **`packageName(String packageName)`**
  - Matches widgets by app package.
  - **Use Case**: Select Settings app elements.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().packageName("com.android.settings")')
    element.click()
    ```

- **`packageNameMatches(String regex)`**
  - Matches package name using a regular expression.
  - **Use Case**: Select system app elements.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().packageNameMatches("com.android.*")')
    element.click()
    ```

### Scrollable Selection

- **`scrollable(boolean isScrollable)`**
  - Matches scrollable widgets (e.g., `ListView`).
  - **Use Case**: Identify scrollable containers.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().scrollable(true)')
    # Used with UiScrollable
    ```

## Using UiScrollable for Scrolling

`UiScrollable` works with `UiSelector` to scroll to off-screen elements.

- **`scrollIntoView(UiSelector selector)`**
  - Scrolls until the element is visible.
  - **Use Case**: Scroll to a list item.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView"))')
    element.click()
    ```

- **`getChildByText(UiSelector childPattern, String text)`**
  - Scrolls to a child with specified text.
  - **Use Case**: Scroll to a `TextView` labeled "Tabs".
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).getChildByText(new UiSelector().className("android.widget.TextView"), "Tabs")')
    element.click()
    ```

## Performing Actions on Selected Elements

Actions are performed using Appium’s WebDriver API, with W3C WebDriver protocol compliance in Appium 2.0.

### Common Actions

- **Click**
  - Simulates a tap.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
    element.click()
    ```

- **Send Keys**
  - Enters text.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")')
    element.send_keys("Harry")
    ```

- **Clear**
  - Clears text fields.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")')
    element.clear()
    ```

- **Get Attribute**
  - Retrieves attributes (e.g., `text`).
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Animation")')
    text = element.get_attribute("text")  # Returns "Animation"
    ```

### Waiting for Elements

- **Explicit Wait**
  - Waits for an element to appear.
  - **Python Example**:
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Create contact")')))
    element.click()
    ```

- **Implicit Wait**
  - Sets a global timeout.
  - **Python Example**:
    ```python
    driver.implicitly_wait(5)  # 5 seconds
    ```

## Mobile Commands for Gestures

Appium 2.0 provides mobile-specific commands executed via `driver.execute_script('mobile: <command>', {...})` for gestures and interactions. Below, the `mobile: scroll` command is detailed, along with other similar commands available in the `UiAutomator2` driver.

### `mobile: scroll`

- **Purpose**: Scrolls the screen or a scrollable element in a specified direction or to a specific element.
- **Parameters**:
  - `direction` (string, optional): `"up"`, `"down"`, `"left"`, or `"right"`.
  - `element` (string, optional): Element ID to scroll within (if omitted, scrolls the entire screen).
  - `strategy` (string, optional): Locator strategy (e.g., `-android uiautomator`).
  - `selector` (string, optional): Selector to find an element to scroll to (e.g., `new UiSelector().text("Target")`).
  - `percent` (float, optional): Scroll distance as a percentage of the scrollable area (0.0 to 1.0).
  - `speed` (int, optional): Scroll speed in pixels per second.
- **Use Case**: Scroll to an element or navigate a list.
- **Python Example (Scroll Down)**:
  ```python
  driver.execute_script('mobile: scroll', {'direction': 'down'})
  ```
- **Python Example (Scroll to Element)**:
  ```python
  driver.execute_script('mobile: scroll', {
      'strategy': '-android uiautomator',
      'selector': 'new UiSelector().text("Target")'
  })
  ```
- **Python Example (Scroll Within Element)**:
  ```python
  scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().scrollable(true)')
  driver.execute_script('mobile: scroll', {
      'element': scrollable.id,
      'direction': 'down',
      'percent': 0.5
  })
  ```

### Other Mobile Commands for Gestures

The following `mobile: *` commands are alternatives or complements to `mobile: scroll` for gestures in the `UiAutomator2` driver.

- **`mobile: swipe`**
  - **Purpose**: Performs a swipe gesture in a specified direction.
  - **Parameters**:
    - `direction` (string): `"up"`, `"down"`, `"left"`, or `"right"`.
    - `element` (string, optional): Element ID to swipe within.
    - `percent` (float, optional): Swipe distance as a percentage (0.0 to 1.0).
    - `speed` (int, optional): Swipe speed in pixels per second.
  - **Use Case**: Navigate carousels or swipe between screens.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: swipe', {'direction': 'left'})
    ```
  - **Difference from `mobile: scroll`**: `mobile: swipe` is faster and typically used for quick gestures, while `mobile: scroll` is smoother and suited for navigating lists.

- **`mobile: dragFromToForDuration`**
  - **Purpose**: Drags from one point to another over a specified duration.
  - **Parameters**:
    - `fromX`, `fromY` (int): Starting coordinates.
    - `toX`, `toY` (int): Ending coordinates.
    - `duration` (float): Duration in seconds.
    - `element` (string, optional): Element ID for relative coordinates.
  - **Use Case**: Drag and drop elements or custom gestures.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: dragFromToForDuration', {
        'fromX': 100, 'fromY': 200,
        'toX': 300, 'toY': 400,
        'duration': 1.0
    })
    ```

- **`mobile: pinch`**
  - **Purpose**: Performs a pinch gesture (zoom in or out).
  - **Parameters**:
    - `element` (string): Element ID to pinch.
    - `percent` (float): Pinch distance as a percentage (default: 0.25).
    - `speed` (int, optional): Pinch speed in pixels per second.
  - **Use Case**: Zoom in/out on maps or images.
  - **Python Example**:
    ```python
    image = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
    driver.execute_script('mobile: pinch', {
        'element': image.id,
        'percent': 0.5,
        'speed': 500
    })
    ```

- **`mobile: tap`**
  - **Purpose**: Taps at specific coordinates or on an element.
  - **Parameters**:
    - `x`, `y` (int, optional): Screen coordinates.
    - `element` (string, optional): Element ID to tap.
  - **Use Case**: Tap at arbitrary points or elements.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: tap', {'x': 500, 'y': 500})
    ```

- **`mobile: longClick`**
  - **Purpose**: Performs a long press on an element or coordinates.
  - **Parameters**:
    - `element` (string, optional): Element ID.
    - `x`, `y` (int, optional): Coordinates.
    - `duration` (int): Duration in milliseconds.
  - **Use Case**: Open context menus.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().longClickable(true)')
    driver.execute_script('mobile: longClick', {
        'element': element.id,
        'duration': 1000
    })
    ```

- **`mobile: doubleTap`**
  - **Purpose**: Performs a double tap on an element or coordinates.
  - **Parameters**:
    - `element` (string, optional): Element ID.
    - `x`, `y` (int, optional): Coordinates.
  - **Use Case**: Zoom in on images or trigger double-tap actions.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
    driver.execute_script('mobile: doubleTap', {'element': element.id})
    ```

- **`mobile: clickAndHold`**
  - **Purpose**: Clicks and holds at coordinates (similar to `longClick` but coordinate-based).
  - **Parameters**:
    - `x`, `y` (int): Coordinates.
    - `duration` (int): Duration in milliseconds.
  - **Use Case**: Custom long-press interaction
  - **Python Example**:
    ```python
    driver.execute_script('mobile: clickAndHold', {'x': 500, 'y': 500, 'duration': 2000})
    ```

- **`mobile: fling`**
  - **Purpose**: Performs a fling gesture, a quick swipe to initiate scrolling with momentum.
  - **Parameters**:
    - `element` (string, optional): Element ID to fling within.
    - `direction` (string): `"up"`, `"down"`, `"left"`, or `"right"`.
    - `speed` (int, optional): Fling speed in pixels per second.
  - **Use Case**: Rapidly navigate through lists or galleries.
  - **Python Example**:
    ```python
    scrollable = driver.find_element(AppiumBy.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().scrollable(true))')
    driver.execute_script("mobile: fling", {
        'elementId': scrollable.get('id'),
        'direction': 'down',
        'speed': 1000
    })()
    ```

### W3C Actions API (Alternative to Mobile Commands)

For complex gestures, the W3C Actions API can be used, though it’s verbose. Mobile commands are simpler for common tasks.

- **Python Example (Swipe)**:
  ```python
  from selenium.webdriver.common.actions import PointerInput
  from selenium.webdriver.common.actions import ActionBuilder
 from selenium.webdriver.common.action_chains import Interaction

  pointer = PointerInput(Interaction.POINTER_TOUCH, "touch")
 actions = ActionBuilder(driver, mouse=pointer)
  actions.pointer_action.move_to_location(500, 800) \
         .pointer_down() \
         .move_to_location(500, 200) \
         .pointer_up()
  actions.perform()
  ```

### Notes on Mobile Commands

- **Advantages**: Platform-specific commands (e.g., `mobile: scroll`) are simpler than W3C Actions and optimized for Android.
- **Limitations**: Some commands require specific Android versions or may not support all UI elements (e.g., web views).
- **Deprecation**: `TouchAction` is deprecated; prefer mobile commands or W3C Actions.
- **Reference**: See [Appium UI Automator2 Driver Commands](https://github.com/appium/appium-uiautomator2-driver).

## Best Practices in Appium 2.0 with Python

- **Use Stable Locators**: Prefer `resourceId` over `text` or `description`.
- **Avoid XPath**: Use `UiSelector` for performance.
- **Inspect Elements**: Use Appium Inspector to find `resourceId` or `content-description`.
- **Combine Criteria**: Chain `UiSelector` methods, e.g., `new UiSelector().className("android.widget.Button").resourceId("com.example:id/submit")`.
- **Handle Scrolling**: Combine `UiScrollable` and `mobile: scroll` for off-screen elements.
- **Test on Real Devices**: Use BrowserStack or LambdaTest for robust testing.

## Reference Example: Automating Contact Creation

This script automates contact creation in the Android Contacts app, using `UiSelector` and `mobile: scroll`.

```python
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Capabilities
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': 'Pixel_4_API_34',
    'appium:platformVersion': '14.0',
    'appium:appPackage': 'com.google.android.contacts',
    'appium:appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
    'appium:noReset': True
}

# Initialize driver
appium_server_url = 'http://localhost:9510'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

try:
    # Handle permission dialog
    driver.find_element(AppiumBy.ID, 'android:id/button2').click()
    
    # Click "Create contact"
    wait = WebDriverWait(driver, 10)
    create_button = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Create contact")')))
    create_button.click()

    # Enter first name
    first_name_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")')
    first_name_field.send_keys("Harry")

    # Scroll to phone field using mobile: scroll
    driver.execute_script('mobile: scroll', {
        'strategy': '-android uiautomator',
        'selector': 'new UiSelector().text("Phone")'
    })
    phone_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone")')
    phone_field.send_keys("1234567890")
    
    # Click "Save"
    save_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Save")')
    save_button.click()

except TimeoutException as e:
    print(f"Timeout error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
```

## Limitations

- **Android-Only**: `UiSelector` and `mobile: *` commands are Android-specific. Use iOS-specific strategies for iOS.
- **Complex Queries**: Nested `UiSelector` chains can be complex; use `resourceId`.
- **Dynamic Elements**: Avoid `index()`; use `instance()` or `resourceId`.
- **Web Views**: Ensure Chromedriver matches the device’s Chrome version.

## References

- **Appium Documentation**: [Python Client](https://appium.github.io/python-client-sphinx/), [UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver).
- **Android Documentation**: [UiAutomator API](https://developer.android.com/reference/androidx/test/uiautomator/UiSelector).
- **BrowserStack**: [Locators](https://www.browserstack.com/docs/automate/appium/locators/).
- **LambdaTest**: [Appium Python](https://www.lambdatest.com/support/docs/appium-python/).

This document provides a complete guide to `UiSelector` and mobile commands in Appium 2.0 with Python, enabling robust Android testing.
```