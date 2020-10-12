def epdir(episode: int):
    """
    Returns the episode folder name given an episode number.

    :param episode: The episode number
    :return: A formatted string of the episode folder name.
    """
    return f"ep{episode}"


def framedir(frame: int, episode: int = None):
    """
    Returns the frame directory given a frame number. If episode is not defined, returns the name of a frame. Otherwise,
    returns a string with the episode directory.

    :param frame: The frame number
    :param episode: The episode number, Optional
    :return: A formatted string of the frame's name or directory.
    """

    if episode is None:
        return f"{str(frame).rjust(4,'0')}.jpg"
    else:
        return f"ep{episode}/{str(frame).rjust(4,'0')}.jpg"
