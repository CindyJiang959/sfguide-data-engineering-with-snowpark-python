import sys
from device_detector import DeviceDetector

def main(userAgent: str) -> str:
    detector = DeviceDetector(userAgent)
    detector.parse()
    return detector.device_type()


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore
