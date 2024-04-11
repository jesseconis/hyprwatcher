from setuptools import setup, Extension

module = Extension("hyprwatcher", sources=["hyprwatcher.c"])

setup(
    name="HyprWatcher",
    version="1.0",
    description="Hyprland desktop time tracker via reading instance socket & serializing result.",
    ext_modules=[module],
)
