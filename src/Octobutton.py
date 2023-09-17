from __future__ import with_statement
from typing import List

import Live
from _Framework.ButtonElement import ButtonElement

from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from .RecordingSessionComponent import RecordingSessionComponent
from .mappings import CHANNEL, PRESSED_NOTES, HELD_NOTES


class Octobutton(ControlSurface):
    __module__ = __name__
    __doc__ = "SCript for the Octobutton MIDI device"
    recording_session: RecordingSessionComponent
    pressed_buttons: List[ButtonElement]
    held_buttons: List[ButtonElement]

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

            self._setup_recording_session()

    def disconnect(self):
        """clean up on disconnect"""
        ControlSurface.disconnect(self)
        return None

    def _setup_recording_session(self):
        self.recording_session = RecordingSessionComponent(
            PRESSED_NOTES, HELD_NOTES, self.log_message
        )
        self.set_highlighting_session_component(self.recording_session)
