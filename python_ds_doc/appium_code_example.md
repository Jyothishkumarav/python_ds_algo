Appium 2.0 Python Automation: Element Finding, Screenshot, Tap, Scroll, and Hybrid/Web Apps
This document provides sample Python code for Appium 2.0 to demonstrate finding elements using various locators, handling screenshot interactions, tap, and scrolling, and explains how to automate hybrid and web apps in Appium 2.0. It builds on the Appium 2.0 architecture, including the Appium Client, Appium Server, UIAutomator2 Driver, ADB, Appium UIAutomator2 Server, Bootstrap Layer, and inbuilt UIAutomator2, with a detailed interaction flow for reference and interview preparation.
1. Prerequisites for Appium 2.0

Appium Server: Install via npm: npm install -g appium@2.x.
UIAutomator2 Driver: Install via Appium CLI: appium driver install uiautomator2.
Python Client: Install Appium Python client: pip install Appium-Python-Client.
Android SDK: Required for ADB and UIAutomator2.
Device/Emulator: Android device or emulator with the app under test (AUT).
Dependencies: Ensure ADB is configured (adb devices lists the device).

2. Sample Python Code for Finding Elements
Below is a Python script demonstrating how to find elements using different locators in Appium 2.0 for an Android app.
Code: Finding Elements with Various Locators
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:app": "/path/to/your/app.apk",
    "appium:automationName": "UiAutomator2"
}

# Initialize Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Wait for app to load
    time.sleep(5)

    # 1. Find element by ID (resource-id)
    button_by_id = driver.find_element(AppiumBy.ID, "com.example:id/button")
    print("Found element by ID:", button_by_id.get_attribute("text"))
    button_by_id.click()

    # 2. Find element by Accessibility ID
    button_by_accessibility = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "submit_button")
    print("Found element by Accessibility ID:", button_by_accessibility.get_attribute("text"))
    button_by_accessibility.click()

    # 3. Find element by XPath
    button_by_xpath = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Submit']")
    print("Found element by XPath:", button_by_xpath.get_attribute("text"))
    button_by_xpath.click()

    # 4. Find element by Class Name
    text_field_by_class = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    print("Found element by Class Name:", text_field_by_class.get_attribute("text"))
    text_field_by_class.send_keys("Test Input")

    # 5. Find element by UIAutomator (Android-specific)
    button_by_uiautomator = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               'new UiSelector().text("Login")')
    print("Found element by UIAutomator:", button_by_uiautomator.get_attribute("text"))
    button_by_uiautomator.click()

except NoSuchElementException as e:
    print(f"Element not found: {e}")
finally:
    # Close the driver
    driver.quit()

Explanation of Locators

ID (AppiumBy.ID):
Uses the resource-id attribute (e.g., com.example:id/button).
Fastest and most reliable locator for Android.
Example: Finds a button with resource-id: com.example:id/button.


Accessibility ID (AppiumBy.ACCESSIBILITY_ID):
Uses the content-desc attribute, ideal for accessibility-focused testing.
Cross-platform (works for Android and iOS).
Example: Finds an element with content-desc: submit_button.


XPath (AppiumBy.XPATH):
Uses hierarchical XML paths to locate elements (e.g., //android.widget.Button[@text='Submit']).
Slower but versatile for complex queries.


Class Name (AppiumBy.CLASS_NAME):
Targets elements by their UI component type (e.g., android.widget.EditText).
Useful for generic elements but may return multiple matches.


UIAutomator (AppiumBy.ANDROID_UIAUTOMATOR):
Android-specific locator using UIAutomator2’s UiSelector API.
Example: new UiSelector().text("Login") finds an element with the text "Login".
Powerful for dynamic or complex element searches.



Interaction Flow for Finding Elements
Using the command driver.find_element(AppiumBy.ID, "com.example:id/button").click() as an example:

Appium Client:
Constructs an HTTP request (W3C WebDriver Protocol):POST /session/:sessionId/element
{
  "using": "id",
  "value": "com.example:id/button"
}


Sends to Appium server at http://localhost:4723/wd/hub.


Appium Server:
Routes the command to the UIAutomator2 driver based on automationName: UiAutomator2.


UIAutomator2 Driver:
Translates AppiumBy.ID to UiSelector().resourceId("com.example:id/button").
Sends the command to the Appium UIAutomator2 Server via ADB.


ADB:
Forwards the request to the Appium UIAutomator2 Server (port 6790).


Appium UIAutomator2 Server:
Delegates the command to the Bootstrap Layer.


Bootstrap Layer (bootstrap.jar):
Uses UIAutomator2 API:UiObject2 element = UiDevice.getInstance().findObject(By.res("com.example", "button"));


For click: Executes element.click().


Inbuilt UIAutomator2:
Queries the UI hierarchy, locates the element, and performs the click.


Response Flow: Returns the element reference and action status through the same chain (UIAutomator2 → Bootstrap Layer → Appium UIAutomator2 Server → ADB → UIAutomator2 Driver → Appium Server → Client).

3. Screenshot, Tap, and Scrolling Interactions
Sample Code: Screenshot, Tap, and Scrolling
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import base64

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:app": "/path/to/your/app.apk",
    "appium:automationName": "UiAutomator2"
}

# Initialize Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Wait for app to load
    time.sleep(5)

    # 1. Take a screenshot
    screenshot = driver.get_screenshot_as_base64()
    with open("screenshot.png", "wb") as f:
        f.write(base64.b64decode(screenshot))
    print("Screenshot saved as screenshot.png")

    # 2. Perform a tap at coordinates (x, y)
    touch_action = TouchAction(driver)
    touch_action.tap(x=500, y=1000).perform()
    print("Performed tap at (500, 1000)")

    # 3. Perform scrolling (swipe up)
    driver.execute_script("mobile: swipeGesture", {
        "left": 100, "top": 1000, "width": 600, "height": 600,
        "direction": "up", "percent": 0.5
    })
    print("Performed swipe up")

    # 4. Scroll to an element using UIAutomator
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                       'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Settings"))')
    print("Scrolled to element with text 'Settings'")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()

Explanation of Interactions

Screenshot:

Command: driver.get_screenshot_as_base64()
Function: Captures the device screen as a base64-encoded string.
Interaction Flow:
Client sends a /screenshot request to the Appium server.
UIAutomator2 driver requests the screenshot via the Appium UIAutomator2 Server.
Bootstrap Layer uses UIAutomator2’s UiDevice.takeScreenshot() to capture the screen.
The image is encoded and returned through the chain.


Use Case: Debugging, visual verification.
Output: Saves the screenshot as screenshot.png.


Tap:

Command: TouchAction(driver).tap(x=500, y=1000).perform()
Function: Simulates a tap at specific coordinates.
Interaction Flow:
Client sends an /actions request (W3C Actions API).
UIAutomator2 driver translates coordinates to a UIAutomator2 command:UiDevice.getInstance().click(500, 1000);


Appium UIAutomator2 Server and Bootstrap Layer execute the tap.


Use Case: Interacting with non-element-based UI components (e.g., canvas).
ADB Equivalent: adb shell input tap 500 1000 (less precise).


Scrolling:

Commands:
Swipe: driver.execute_script("mobile: swipeGesture", {...})
Scroll to element: AppiumBy.ANDROID_UIAUTOMATOR with UiScrollable.


Function:
Swipe moves the screen in a direction (e.g., up).
Scroll to element uses UIAutomator2’s UiScrollable to find an element.


Interaction Flow:
For swipe: Client sends a mobile: swipeGesture command, translated to:UiDevice.getInstance().swipe(100, 1000, 100, 400, 50);


For scroll: UIAutomator2 API scrolls until the element is visible:new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Settings"));


Handled by Appium UIAutomator2 Server and Bootstrap Layer.


Use Case: Navigating lists or finding off-screen elements.
ADB Equivalent: adb shell input swipe x1 y1 x2 y2 (less reliable).



4. Handling Hybrid and Web Apps in Appium 2.0
Hybrid Apps

Definition: Apps combining native components (e.g., Android Activities) and web components (e.g., WebView).
Automation in Appium 2.0:
Context Switching:
Hybrid apps have multiple contexts: NATIVE_APP (native) and WEBVIEW_<package> (web).
Use driver.get_contexts() to list available contexts.
Switch to WebView context: driver.switch_to.context("WEBVIEW_com.example").


Locators:
Native: Use AppiumBy.ID, AppiumBy.XPATH, etc.
WebView: Use Selenium locators (By.ID, By.CSS_SELECTOR) after switching to WebView context.


Requirements:
Enable WebView debugging in the app (set webView.setWebContentsDebuggingEnabled(true) in app code).
Install ChromeDriver (automatically managed by UIAutomator2 driver in Appium 2.0).


Sample Code:from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time

desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:app": "/path/to/hybrid_app.apk",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    time.sleep(5)

    # Interact with native context
    native_button = driver.find_element(AppiumBy.ID, "com.example:id/native_button")
    native_button.click()

    # List available contexts
    contexts = driver.get_contexts()
    print("Available contexts:", contexts)

    # Switch to WebView context
    driver.switch_to.context("WEBVIEW_com.example")

    # Interact with WebView (web elements)
    web_element = driver.find_element(By.CSS_SELECTOR, "button#submit")
    web_element.click()

    # Switch back to native context
    driver.switch_to.context("NATIVE_APP")
    native_text = driver.find_element(AppiumBy.ID, "com.example:id/text_field")
    native_text.send_keys("Back to native")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()





Web Apps

Definition: Mobile apps that are essentially web browsers loading web content (e.g., Chrome, Safari).
Automation in Appium 2.0:
Desired Capabilities:
Set browserName: Chrome (Android) or Safari (iOS) instead of app.
Example:{
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:browserName": "Chrome",
  "appium:automationName": "UiAutomator2"
}




Locators: Use Selenium locators (By.ID, By.CSS_SELECTOR, By.XPATH).
ChromeDriver: UIAutomator2 driver automatically configures ChromeDriver for WebView or browser automation.
Sample Code:from appium import webdriver
from selenium.webdriver.common.by import By
import time

desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:browserName": "Chrome",
    "appium:automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Navigate to a website
    driver.get("https://example.com")

    # Find and interact with web elements
    link = driver.find_element(By.CSS_SELECTOR, "a[href='/about']")
    link.click()

    # Take a screenshot
    screenshot = driver.get_screenshot_as_base64()
    with open("web_screenshot.png", "wb") as f:
        f.write(base64.b64decode(screenshot))
    print("Web screenshot saved")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()





Interaction Flow for Hybrid/Web Apps

Context Switching:
Client sends /contexts and /context requests to list and switch contexts.
UIAutomator2 driver queries WebView contexts via ChromeDriver integration.
Appium UIAutomator2 Server and Bootstrap Layer handle native interactions; ChromeDriver handles WebView interactions.


WebView Automation:
ChromeDriver (managed by UIAutomator2 driver) translates Selenium commands to browser actions.
Commands follow the same flow (Client → Server → UIAutomator2 Driver → ChromeDriver → WebView).



5. Interview Questions and Answers

How do you find elements in Appium 2.0 using Python?

Answer: Appium 2.0 uses locators like AppiumBy.ID (resource-id), AppiumBy.ACCESSIBILITY_ID (content-desc), AppiumBy.XPATH, AppiumBy.CLASS_NAME, and AppiumBy.ANDROID_UIAUTOMATOR. Example: driver.find_element(AppiumBy.ID, "com.example:id/button") finds an element by resource-id. UIAutomator2 translates these to native API calls via the Bootstrap Layer.


How do you capture a screenshot in Appium 2.0?

Answer: Use driver.get_screenshot_as_base64() to capture the screen as a base64 string, then decode and save it. The UIAutomator2 driver requests the screenshot via the Appium UIAutomator2 Server, which uses UiDevice.takeScreenshot().


How do you perform tap and scroll in Appium 2.0?

Answer: Tap uses TouchAction(driver).tap(x, y).perform() for coordinate-based taps. Scroll uses mobile: swipeGesture or UIAutomator’s UiScrollable (e.g., new UiScrollable().scrollIntoView()). These are translated to UIAutomator2 API calls like UiDevice.click(x, y) or UiDevice.swipe().


How does Appium 2.0 handle hybrid apps?

Answer: Appium 2.0 automates hybrid apps by switching between NATIVE_APP and WEBVIEW_<package> contexts using driver.get_contexts() and driver.switch_to.context(). Native elements use Appium locators; WebView uses Selenium locators. The UIAutomator2 driver integrates with ChromeDriver for WebView automation.


How do you automate web apps in Appium 2.0?

Answer: Set browserName: Chrome in Desired Capabilities to launch a browser. Use Selenium locators (e.g., By.CSS_SELECTOR) to interact with web elements. The UIAutomator2 driver uses ChromeDriver to automate browser actions, following the W3C WebDriver Protocol.


What is the interaction flow for a tap action in Appium 2.0?

Answer: The client sends a /actions request to the Appium server, routed to the UIAutomator2 driver. The driver sends the command via ADB to the Appium UIAutomator2 Server, which delegates to the Bootstrap Layer. The Bootstrap Layer uses UIAutomator2’s UiDevice.click(x, y) to perform the tap, with results returned through the chain.



6. Conclusion
Appium 2.0 enables robust automation of Android apps using Python, with locators like ID, Accessibility ID, XPath, and UIAutomator for element finding, and commands for screenshots, taps, and scrolling. Hybrid and web apps are handled via context switching and ChromeDriver integration. The interaction flow involves the Appium Client, Server, UIAutomator2 Driver, ADB, Appium UIAutomator2 Server, Bootstrap Layer, and inbuilt UIAutomator2, ensuring precise UI automation. This knowledge is critical for mastering Appium 2.0 and excelling in automation interviews.
