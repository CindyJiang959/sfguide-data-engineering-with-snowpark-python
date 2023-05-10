import sys
from device_detector import DeviceDetector

def main(userAgent: str) -> str:
    detector = DeviceDetector(userAgent)
    detector.parse()
    is_desktop = 1 if detector.is_desktop() else 0
    if is_desktop:
        return 'desktop'
    elif detector.is_mobile():
        if 'phone' in str(detector.device).lower():
            return  'mobile'
        elif 'pad' in str(detector.device).lower():
            return 'tablet'
        else:
            return 'no type'


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore
