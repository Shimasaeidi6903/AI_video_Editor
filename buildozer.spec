[app]

title = AI Video Editor
package.name = aivideoeditor
package.domain = org.aivideoeditor

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,mp4,mov

version = 0.1

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 36
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = READ_MEDIA_VIDEO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

p4a.branch = develop
p4a.commit = 0382d27
