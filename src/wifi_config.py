import subprocess
import re


class WifiInformation:
    def __init__(self):
        pass

    @staticmethod
    def get_wifi_frequency():
        try:
            output = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
                 "-I"]).decode("utf-8")
            frequency_match = re.search(r"channel:\s*(\d+)", output, re.IGNORECASE)
            if frequency_match:
                channel = int(frequency_match.group(1))
                if 1 <= channel <= 14:
                    return "2.4 GHz"
                elif 36 <= channel <= 165:
                    return "5 GHz"
        except subprocess.CalledProcessError:
            pass

        return "Frequency not found"


if __name__ == "__main__":
    frequency = WifiInformation.get_wifi_frequency()
    print("Connected WiFi frequency:", frequency)
