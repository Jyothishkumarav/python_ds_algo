# Setting Up Appium with Selenium Grid for Android Device Automation
This document provides a comprehensive guide to connecting a remote host to Android devices for automation using Selenium Grid, Appium Server, and UiAutomator2, including parallel test execution on multiple devices.
Prerequisites

Selenium Grid: A running hub and node(s).
Appium Server: Installed with the UiAutomator2 driver (appium driver install uiautomator2).
Android Devices: Connected via USB or wireless ADB, with USB debugging enabled.
Android SDK: Installed with adb configured.
Network: Hub, node(s), and remote host must be accessible on the same network or via public IPs/VPN.
Test Framework: Supports parallel execution (e.g., TestNG for Java, Pytest for Python).
Dependencies: Java, Node.js, Appium, Selenium WebDriver, and a programming language client (e.g., Java, Python).

Connecting a Remote Host to a Single Android Device
1. Set Up Selenium Grid

Start the Hub:

On the hub machine (e.g., 192.168.1.10), run:java -jar selenium-server-standalone.jar -role hub


Verify at http://192.168.1.10:4444/grid/console.


Register the Appium Node:

On the node machine (e.g., 192.168.1.20), create a nodeconfig.json:{
  "capabilities": [
    {
      "platformName": "Android",
      "automationName": "UiAutomator2",
      "maxInstances": 1,
      "platform": "ANDROID"
    }
  ],
  "configuration": {
    "cleanUpCycle": 2000,
    "timeout": 30000,
    "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
    "url": "http://192.168.1.20:4723/wd/hub",
    "host": "192.168.1.20",
    "port": 4723,
    "maxSession": 1,
    "register": true,
    "registerCycle": 5000,
    "hubHost": "192.168.1.10",
    "hubPort": 4444
  }
}


Register the node:java -jar selenium-server-standalone.jar -role node -nodeConfig nodeconfig.json


Confirm registration at http://192.168.1.10:4444/grid/console.



2. Set Up Appium Server

Install Appium:
npm install -g appium
appium driver install uiautomator2


Configure the Android Device:

Enable USB debugging in Developer Options.
Verify device detection:adb devices




Start Appium Server:
appium --address 192.168.1.20 --port 4723


Verify at http://192.168.1.20:4723/wd/hub/status.



3. Configure the Remote Host

Install Dependencies (e.g., for Python):
pip install Appium-Python-Client


Write a Test Script (Python example):
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "<device-name>",
    "app": "<path-to-your-apk>",
    "udid": "<device-udid>"
}

driver = webdriver.Remote(
    command_executor='http://192.168.1.10:4444/wd/hub',
    desired_capabilities=desired_caps
)

driver.find_element_by_id("com.example:id/button").click()
driver.quit()


Network Configuration:

Ensure the remote host can access 192.168.1.10:4444 (hub) and 192.168.1.20:4723 (Appium).



4. Run the Test

Execute the script from the remote host. The hub routes commands to the Appium server, which automates the device.

5. Troubleshooting

Connection Issues: Check firewall settings for ports 4444 and 4723.
Device Not Found: Verify adb devices and correct UDID in capabilities.
UiAutomator2 Issues: Ensure the driver is installed and the device supports API level 16+.

Parallel Testing on Four Android Devices
A single Appium server on one port can automate only one device at a time. To run four tests in parallel on four devices, use multiple Appium servers and Selenium Grid nodes.
1. Verify Device Connectivity

Confirm all four devices are detected:adb devices



2. Set Up Selenium Grid Hub

Start the hub (same as above):java -jar selenium-server-standalone.jar -role hub



3. Configure Four Appium Servers

Start four Appium instances, each on a unique port and bound to a specific device:appium --address 192.168.1.20 --port 4723 --udid <device1-udid> &
appium --address 192.168.1.20 --port 4724 --udid <device2-udid> &
appium --address 192.168.1.20 --port 4725 --udid <device3-udid> &
appium --address 192.168.1.20 --port 4726 --udid <device4-udid> &


Verify each at http://192.168.1.20:<port>/wd/hub/status.

4. Register Four Nodes to Selenium Grid

Create four node configuration files (e.g., node1.json, node2.json, etc.). Example for node1.json:{
  "capabilities": [
    {
      "platformName": "Android",
      "automationName": "UiAutomator2",
      "udid": "<device1-udid>",
      "maxInstances": 1,
      "platform": "ANDROID"
    }
  ],
  "configuration": {
    "cleanUpCycle": 2000,
    "timeout": 30000,
    "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
    "url": "http://192.168.1.20:4723/wd/hub",
    "host": "192.168.1.20",
    "port": 4723,
    "maxSession": 1,
    "register": true,
    "registerCycle": 5000,
    "hubHost": "192.168.1.10",
    "hubPort": 4444
  }
}


Update port and udid for node2.json (4724), node3.json (4725), and node4.json (4726).
Register nodes:java -jar selenium-server-standalone.jar -role node -nodeConfig node1.json &
java -jar selenium-server-standalone.jar -role node -nodeConfig node2.json &
java -jar selenium-server-standalone.jar -role node -nodeConfig node3.json &
java -jar selenium-server-standalone.jar -role node -nodeConfig node4.json &


Verify at http://192.168.1.10:4444/grid/console.

5. Configure Test Framework for Parallel Execution
Option 1: TestNG (Java)

Create testng.xml:
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="ParallelTests" parallel="tests" thread-count="4">
  <test name="Test1">
    <parameter name="udid" value="<device1-udid>"/>
    <parameter name="port" value="4723"/>
    <classes>
      <class name="com.example.ParallelTest"/>
    </classes>
  </test>
  <test name="Test2">
    <parameter name="udid" value="<device2-udid>"/>
    <parameter name="port" value="4724"/>
    <classes>
      <class name="com.example.ParallelTest"/>
    </classes>
  </test>
  <test name="Test3">
    <parameter name="udid" value="<device3-udid>"/>
    <parameter name="port" value="4725"/>
    <classes>
      <class name="com.example.ParallelTest"/>
    </classes>
  </test>
  <test name="Test4">
    <parameter name="udid" value="<device4-udid>"/>
    <parameter name="port" value="4726"/>
    <classes>
      <class name="com.example.ParallelTest"/>
    </classes>
  </test>
</suite>


Write Test Class (ParallelTest.java):
package com.example;
import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import java.net.URL;

public class ParallelTest {
    @Test
    @Parameters({"udid", "port"})
    public void testOnDevice(String udid, String port) throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("platformName", "Android");
        caps.setCapability("automationName", "UiAutomator2");
        caps.setCapability("udid", udid);
        caps.setCapability("app", "<path-to-your-apk>");
        caps.setCapability("deviceName", "AndroidDevice");

        AndroidDriver driver = new AndroidDriver(
            new URL("http://192.168.1.10:4444/wd/hub"), caps
        );

        driver.findElementById("com.example:id/button").click();
        driver.quit();
    }
}


Run Tests:
mvn test -DsuiteXmlFile=testng.xml



Option 2: Pytest (Python)

Install Dependencies:
pip install pytest pytest-xdist appium-python-client


Write Test Script (test_parallel.py):
from appium import webdriver
import pytest

@pytest.mark.parametrize("udid,port", [
    ("<device1-udid>", "4723"),
    ("<device2-udid>", "4724"),
    ("<device3-udid>", "4725"),
    ("<device4-udid>", "4726")
])
def test_on_device(udid, port):
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "udid": udid,
        "app": "<path-to-your-apk>",
        "deviceName": "AndroidDevice"
    }
    driver = webdriver.Remote(
        command_executor="http://192.168.1.10:4444/wd/hub",
        desired_capabilities=desired_caps
    )
    driver.find_element_by_id("com.example:id/button").click()
    driver.quit()


Run Tests:
pytest test_parallel.py -n 4



6. Key Insight: One Appium Server, One Device

A single Appium server instance on one port can automate only one device at a time due to session management, port binding, and resource allocation.
Parallel testing requires multiple Appium servers, each on a unique port and bound to a specific device.

7. Troubleshooting

Port Conflicts: Ensure unique ports for each Appium server.
Device Not Found: Verify adb devices and correct UDIDs.
Grid Overload: Confirm hub supports multiple sessions.
Resource Constraints: Monitor CPU/memory if running multiple Appium servers on one machine.
Logs: Use appium --log-level debug and Selenium Grid logs for debugging.

8. Optimization and Scaling

Separate Machines: Run Appium servers on different machines for better performance.
Dynamic Capabilities: Use data providers to assign UDIDs/ports dynamically.
Docker: Use Dockerized Appium containers for easier management.
Cloud Device Farms: Consider BrowserStack or Sauce Labs for scalable device access.

Example Workflow

Setup:
Hub: 192.168.1.10:4444
Four Appium servers: 192.168.1.20:4723 to 4726, each bound to one device.
Four nodes registered with node1.json to node4.json.


Execution:
Run testng.xml or pytest -n 4 from the remote host.
Tests target devices via UDIDs and ports, routed through the hub.


Result: Four tests run in parallel, each on a separate device.

This setup enables efficient automation and parallel testing on Android devices using Selenium Grid and Appium.
