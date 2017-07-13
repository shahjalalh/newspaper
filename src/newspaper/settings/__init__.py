from .envs import BaseDevelopment, Testing, Staging, Acceptance, Production  # noqa

try:
    from .local import LocalSettings  # isort:skip
except ImportError:
    Development = BaseDevelopment
else:
    class Development(LocalSettings, BaseDevelopment):
        pass
