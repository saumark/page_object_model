
systems = {
    "uptake": "https://www.uptake.com/"
}


def get_device_module(device_name):

    device_module = {
        "chrome": "uptake.browser",
        "firefox": "uptake.browser"
    }

    return device_module.get(device_name)