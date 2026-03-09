import os
import time


def take_screenshot(driver):

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    filename = f"screenshots/screenshot_{int(time.time())}.png"

    driver.save_screenshot(filename)

    return filename