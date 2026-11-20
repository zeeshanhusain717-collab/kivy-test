[app]
title = KivyTest
package.name = kivytest
package.domain = org.test
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
