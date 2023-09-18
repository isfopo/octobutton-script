from Live import Clip, ClipSlot, Track


def get_last_clip(track: Track.Track) -> Clip.Clip:
    """Gets the bottommost Clip in the Track, given that there are no empty Clip Slots. If so, this function will return the Clip before the empty Slot.

    Args:
        track (Track.Track): An Ableton Live Track

    Returns:
        Clip.Clip: Returns None if all Slots are empty
    """
    slot: ClipSlot.ClipSlot
    clip: Clip.Clip = None
    for slot in track.clip_slots:
        if slot.has_clip:
            clip = slot.clip
        else:
            break
    return clip


def get_first_empty_clip_slot(track: Track.Track) -> ClipSlot.ClipSlot:
    """Returns the first empty Clip Slot

    Args:
        track (Track.Track): An Ableton Live Track

    Returns:
        ClipSlot.ClipSlot: Return None if all Slots are full. Create a new Scene if this is the case.
    """
    slot: ClipSlot.ClipSlot
    for slot in track.clip_slots:
        if not slot.has_clip:
            return slot
    return None
