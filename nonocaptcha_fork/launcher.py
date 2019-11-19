# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Launcher module.
Used to have workarounds to launch browsers asynchronously. Now it's just
a passthrough to pyppeteer_fork.launcher.Launcher
"""

from pyppeteer_fork import launcher


class Launcher(launcher.Launcher):
    # TODO: remove this class, this used to have hacks to run the browser
    #       asynchronously which are now merged into pyppeteer_fork
    pass
