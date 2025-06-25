```markdown
# UiSelector, Mobile Commands, and W3C Actions for Appium 2.0 with Python Client

The `UiSelector` class, part of the Android UiAutomator framework, is used in Appium 2.0 with the `UiAutomator2` driver to define criteria for selecting UI elements in Android applications during automation testing. The `AppiumBy.ANDROID_UIAUTOMATOR` locator strategy enables element location using attributes like text, resource ID, or class name. Appium 2.0 also provides mobile-specific commands (e.g., `mobile: scroll`) via `execute_script` for gestures and W3C Actions API for advanced interactions. This document details `UiSelector` methods, mobile commands (focusing on `mobile: scroll` and alternatives), and high-level W3C Actions using `appium.webdriver.common.action_chains`, with Python examples and a reference script for automating contact creation in the Android Contacts app.

## Overview

- **Purpose**: `UiSelector` locates UI elements, mobile commands handle gestures, and W3C Actions enable complex interactions in Android automation.
- **Driver**: `UiAutomator2` supports Android 5.0 (API level 21) and above.
- **Locator Strategy**: Use `AppiumBy.ANDROID_UIAUTOMATOR` for `UiSelector`.
- **Mobile Commands**: Executed via `driver.execute_script('mobile: <command>', {...})`.
- **W3C Actions**: High-level API via `appium.webdriver.common.action_chains` for gestures like swipe or tap.
- **Key Classes**:
  - `UiSelector`: Defines selection criteria.
  - `UiScrollable`: Scrolls to elements.
  - `UiObject2`: Represents UI elements (internal).
- **Appium 2.0 Notes**:
  - Install driver: `appium driver install uiautomator2`.
  - Deprecated APIs (e.g., `TouchAction`, `MobileElement`) are replaced with W3C Actions or `WebElement`.
  - Set `appium:automationName` to `UiAutomator2` in capabilities.
- **Setup Requirements**:
  - Install Appium 2.0: `pip install appium-python-client`.
  - Install Android SDK and set `ANDROID_HOME`.
  - Use Python 3.7+ and `selenium`: `pip install selenium`.
  - Configure Android device/emulator with Developer Mode.
  - Start Appium server (port: 9510).

## UiSelector Methods for Selecting Elements

`UiSelector` methods are chained in a string passed to `driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, <selector>)`. The first matching element is selected, or a `NoSuchElementException` is raised.

### Text-Based Selection

- **`text(String text)`**
  - Matches exact visible text (case-sensitive).
  - **Use Case**: Select "OK" button.
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
  - **Use Case**: Select "Apps" icon.
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
  - **Use Case**: Stable element identification.
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

Actions use Appium’s WebDriver API, aligned with W3C WebDriver protocol.

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

Mobile-specific commands are executed via `driver.execute_script('mobile: <command>', {...})`.

### `mobile: scroll`

- **Purpose**: Scrolls the screen or a scrollable element.
- **Parameters**:
  - `direction` (string, optional): `"up"`, `"down"`, `"left"`, `"right"`.
  - `element` (string, optional): Element ID to scroll within.
  - `strategy` (string, optional): Locator strategy (e.g., `-android uiautomator`).
  - `selector` (string, optional): Selector (e.g., `new UiSelector().text("Target")`).
  - `percent` (float, optional): Scroll distance (0.0 to 1.0).
  - `speed` (int, optional): Pixels per second.
- **Use Case**: Scroll to an element or navigate lists.
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

- **`mobile: swipe`**
  - **Purpose**: Performs a quick swipe.
  - **Parameters**: `direction`, `element`, `percent`, `speed`.
  - **Use Case**: Navigate carousels.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: swipe', {'direction': 'left'})
    ```

- **`mobile: dragFromToForDuration`**
  - **Purpose**: Drags between coordinates.
  - **Parameters**: `fromX`, `fromY`, `toX`, `toY`, `duration`, `element`.
  - **Use Case**: Drag and drop.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: dragFromToForDuration', {
        'fromX': 100, 'fromY': 200,
        'toX': 300, 'toY': 400,
        'duration': 1.0
    })
    ```

- **`mobile: pinch`**
  - **Purpose**: Pinches (zoom in/out).
  - **Parameters**: `element`, `percent`, `speed`.
  - **Use Case**: Zoom on maps.
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
  - **Purpose**: Taps at coordinates or element.
  - **Parameters**: `x`, `y`, `element`.
  - **Use Case**: Tap arbitrary points.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: tap', {'x': 500, 'y': 500})
    ```

- **`mobile: longClick`**
  - **Purpose**: Long presses.
  - **Parameters**: `element`, `x`, `y`, `duration`.
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
  - **Purpose**: Double taps.
  - **Parameters**: `element`, `x`, `y`.
  - **Use Case**: Zoom images.
  - **Python Example**:
    ```python
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
    driver.execute_script('mobile: doubleTap', {'element': element.id})
    ```

- **`mobile: clickAndHold`**
  - **Purpose**: Clicks and holds at coordinates.
  - **Parameters**: `x`, `y`, `duration`.
  - **Use Case**: Custom long-press.
  - **Python Example**:
    ```python
    driver.execute_script('mobile: clickAndHold', {'x': 500, 'y': 500, 'duration': 2000})
    ```

- **`mobile: fling`**
  - **Purpose**: Quick swipe with momentum.
  - **Parameters**: `element`, `direction`, `speed`.
  - **Use Case**: Navigate lists.
  - **Python Example**:
    ```python
    scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().scrollable(true)')
    driver.execute_script('mobile: fling', {
        'element': scrollable.id,
        'direction': 'down',
        'speed': 1000
    })
    ```

### W3C Actions for Gestures

The W3C Actions API, accessed via `appium.webdriver.common.action_chains`, provides a high-level, cross-platform way to perform complex gestures. Below are examples using `ActionBuilder` and `PointerInput` for common gestures, replacing the deprecated `TouchAction`.

- **Swipe (Scroll)**
  - **Purpose**: Simulates a swipe gesture to scroll.
  - **Use Case**: Scroll a list or navigate screens.
  - **Python Example**:
    ```python
    from appium.webdriver.common.action_chains import ActionBuilder
    from appium.webdriver.common.actions import PointerInput
    from appium.webdriver.common.actions.action_builder import Interaction

    # Define pointer input
    pointer = PointerInput(Interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    
    # Perform swipe from (500, 800) to (500, 200)
    actions.pointer_action.move_to_location(500, 800) \
           .pointer_down() \
           .pause(0.1) \
           .move_to_location(500, 200) \
           .pointer_up()
    actions.perform()
    ```

- **Tap**
  - **Purpose**: Simulates a single tap on an element or coordinates.
  - **Use Case**: Tap a button or point.
  - **Python Example**:
    ```python
    from appium.webdriver.common.action_chains import ActionBuilder
    from appium.webdriver.common.actions import PointerInput
    from appium.webdriver.common.actions.action_builder import Interaction

    # Find element
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
    
    # Define pointer input
    pointer = PointerInput(Interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    
    # Tap at element's center
    actions.pointer_action.move_to(element) \
           .pointer_down() \
           .pointer_up()
    actions.perform()
    ```

- **Long Press**
  - **Purpose**: Simulates a long press on an element.
  - **Use Case**: Open context menus.
  - **Python Example**:
    ```python
    from appium.webdriver.common.action_chains import ActionBuilder
    from appium.webdriver.common.actions import PointerInput
    from appium.webdriver.common.actions.action_builder import Interaction

    # Find element
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().longClickable(true)')
    
    # Define pointer input
    pointer = PointerInput(Interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    
    # Long press for 1 second
    actions.pointer_action.move_to(element) \
           .pointer_down() \
           .pause(1.0) \
           .pointer_up()
    actions.perform()
    ```

- **Pinch (Zoom Out)**
  - **Purpose**: Simulates a two-finger pinch gesture.
  - **Use Case**: Zoom out on a map or image.
  - **Python Example**:
    ```python
    from appium.webdriver.common.action_chains import ActionBuilder
    from appium.webdriver.common.actions import PointerInput
    from appium.webdriver.common.actions.action_builder import Interaction

    # Find element
    image = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
    
    # Define two pointers
    finger1 = PointerInput(Interaction.POINTER_TOUCH, "finger1")
    finger2 = PointerInput(Interaction.POINTER_TOUCH, "finger2")
    actions = ActionBuilder(driver)
    
    # Pinch gesture: fingers move toward each other
    actions.add_input(finger1)
    actions.add_input(finger2)
    
    finger1.move_to_location(500, 400).pointer_down() \
           .move_to_location(500, 500)
    finger2.move_to_location(500, 600).pointer_down() \
           .move_to_location(500, 500)
    
    finger1.pointer_up()
    finger2.pointer_up()
    actions.perform()
    ```

### Notes on W3C Actions vs. Mobile Commands

- **W3C Actions**:
  - Cross-platform (works for Android and iOS).
  - More flexible for complex, multi-touch gestures.
  - Verbose compared to mobile commands.
- **Mobile Commands**:
  - Optimized for Android with `UiAutomator2`.
  - Simpler for common gestures like scrolling or swiping.
  - Platform-specific (Android-only).
- **Preference**: Use mobile commands for simplicity; use W3C Actions for cross-platform tests or unsupported gestures.
- **Reference**: [Appium Python Client Actions](https://appium.github.io/python-client-sphinx/webdriver/common/action_chains.html).

## Best Practices in Appium 2.0 with Python

- **Use Stable Locators**: Prefer `resourceId` over `text` or `description`.
- **Avoid XPath**: Use `UiSelector` for performance.
- **Inspect Elements**: Use Appium Inspector for `resourceId` or `content-description`.
- **Combine Criteria**: Chain `UiSelector` methods, e.g., `new UiSelector().className("android.widget.Button").resourceId("com.example:id/submit")`.
- **Handle Scrolling**: Use `UiScrollable`, `mobile: scroll`, or W3C Actions.
- **Test on Real Devices**: Use BrowserStack or LambdaTest.

## Reference Example: Automating Contact Creation

This script automates contact creation using `UiSelector`, `mobile: scroll`, and W3C Actions for a long press.

```python
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.action_chains import ActionBuilder
from appium.webdriver.common.actions import PointerInput
from appium.webdriver.common.actions.action_builder import Interaction
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
    
    # Long press "Save" button using W3C Actions
    save_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Save")')
    pointer = PointerInput(Interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    actions.pointer_action.move_to(save_button) \
           .pointer_down() \
           .pause(1.0) \
           .pointer_up()
    actions.perform()

except TimeoutException as e:
    print(f"Timeout error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
```

## Limitations

- **Android-Only**: `UiSelector` and `mobile: *` commands are Android-specific. Use iOS strategies for iOS.
- **Complex Queries**: Nested `UiSelector` chains can be complex; use `resourceId`.
- **Dynamic Elements**: Avoid `index()`; use `instance()` or `resourceId`.
- **Web Views**: Match Chromedriver to device’s Chrome version.

## References

- **Appium Documentation**: [Python Client](https://appium.github.io/python-client-sphinx/), [UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver).
- **Android Documentation**: [UiAutomator API](https://developer.android.com/reference/androidx/test/uiautomator/UiSelector).
- **BrowserStack**: [Locators](https://www.browserstack.com/docs/automate/appium/locators).
- **LambdaTest**: [Appium Python](https://www.lambdatest.com/support/docs/appium-python/).

This document provides a comprehensive guide to `UiSelector`, mobile commands, and W3C Actions in Appium 2.0 with Python for robust Android testing.
```