from Live import Clip, ClipSlot, Track


def get_last_clip(track: Track.Track) -> Clip.Clip:
    slot: ClipSlot.ClipSlot
    clip: Clip.Clip = None
    for slot in track.clip_slots:
        if slot.has_clip:
            clip = slot.clip
        else:
            break

    return clip


def get_first_empty_clip_slot(track: Track.Track) -> ClipSlot.ClipSlot:
    pass
