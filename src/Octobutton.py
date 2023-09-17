from __future__ import with_statement

import Live

from _Framework.ControlSurface import ControlSurface


class Octobutton(ControlSurface):
    __module__ = __name__
    __doc__ = "SCript for the Octobutton MIDI device"

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

    def disconnect(self):
        """clean up on disconnect"""
        ControlSurface.disconnect(self)
        return None
