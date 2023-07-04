from platform_type import PlatformType


class PassThroughPlatform(PlatformType):
    def can_pass_through(self):
        return True
