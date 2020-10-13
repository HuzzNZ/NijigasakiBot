import os

from constant import epdir, framedir
from log import log


def delete_episode(episode: int):
    """
    Deletes an episode's directory.

    :param episode: The episode's directory to delete
    :return: True if successful, False if unsuccessful.
    """
    directory = epdir(episode)
    try:
        os.rmdir(directory)
        log(f"{directory} deleted.", "DELETE")
        return True

    # If the directory doesn't exist
    except FileNotFoundError:
        log(f"Tried to delete {directory}, directory not found")
        return False

    # If the directory is not empty
    except OSError:
        log(f"Tried to delete {directory}, directory not empty")
        return False


def delete_frame(frame: int, episode: int):
    """
    Deletes a frame.

    :param frame: The frame to delete
    :param episode: The episode to delete the frame from
    :return: True if successful, False if unsuccessful.
    """
    directory = framedir(frame, episode)
    try:
        os.remove(directory)
        log(f"{directory} deleted.", "DELETE")
        return True

    # If the file doesn't exist
    except FileNotFoundError:
        log(f"Tried to delete {directory}, file not found")
        return False
