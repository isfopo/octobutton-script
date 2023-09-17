from functools import partial
from typing import List
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from _Framework.SessionComponent import SessionComponent
from .mappings import CHANNEL


class RecordingSessionComponent(SessionComponent):
    def __init__(self, pressed_notes: List[int], held_notes: List[int], log=None):
        SessionComponent.__init__(
            self, num_tracks=8, num_scenes=1, auto_name=False, enable_skinning=False
        )

        self.log = log
        self._setup_buttons(pressed_notes, held_notes)

    def _setup_buttons(self, pressed_notes: List[int], held_notes: List[int]):
        self.pressed_buttons = []
        self.held_buttons = []

        for note in pressed_notes:
            button = ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, identifier=note)
            button.add_value_listener(partial(self.pressed_value_listener, note))
            self.pressed_buttons.append(button)

        for note in held_notes:
            button = ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, identifier=note)
            button.add_value_listener(partial(self.held_value_listener, note))
            self.held_buttons.append(button)

    def pressed_value_listener(self, note: int, velocity: int):
        if velocity > 0:
            self.log(note)

    def held_value_listener(self, note: int, velocity: int):
        if velocity > 0:
            self.log(note)
