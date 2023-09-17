from _Framework.SessionComponent import SessionComponent


class RecordingSessionComponent(SessionComponent):
    def __init__(self):
        SessionComponent.__init__(
            self, num_tracks=8, num_scenes=1, auto_name=False, enable_skinning=False
        )
