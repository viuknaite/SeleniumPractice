import os
from datetime import datetime

def save_screenshot(browser, name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{timestamp}_{name}.png")
    browser.save_screenshot(path)