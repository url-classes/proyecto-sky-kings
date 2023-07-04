from platform_type import PlatformType


class SolidPlatform(PlatformType):
    def can_pass_through(self):
        return False