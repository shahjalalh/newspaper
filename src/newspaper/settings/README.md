# newspaper settings

Settings for this project are managed via `django-configurations`, this allows us to configure settings via `Python` 
classes, which makes it easier and more `DRY` to extend and inherit settings between different environments.


## Local settings override

Overriding settings locally can easially be done by creating a `local.py` file which can contain a plain `Python` class 
called `LocalSettings` that allows you to add, change or modify settings

```python

    class LocalSettings(object):
        DEBUG = True  
        DEBUG_TOOLBAR_ENABLED = True

        NEW_SETTING_KEY = 'value'

        @property
        def INSTALLED_APPS(self):
            return super().INSTALLED_APPS + [
                'debug_toolbar'
            ]

```
