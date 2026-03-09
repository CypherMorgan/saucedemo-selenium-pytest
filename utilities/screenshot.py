import os
from utilities.run_context import RUN_ID


def take_screenshot(driver, name="failure"):

    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(
        folder,
        f"{RUN_ID}_{name}.png"
    )

    driver.save_screenshot(file_path)

    return file_path