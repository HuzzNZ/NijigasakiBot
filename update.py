import os

from typing import Union

from constant import epdir, framedir
from delete import delete_episode
from log import log


def find_earliest_episode(max_ep: int = 13) -> Union[int, None]:
    """
    Finds the earliest episode folder that exists in directory.

    :param max_ep: The maximum number of episodes to check up to. Default is 13.
    :return: Integer of the earliest episode folder it can find. None if there is none found.
    """
    for i in range(1, max_ep+1):
        # If the episode directory exists:
        if os.path.exists(epdir(i)):
            return i

        # Otherwise, if it doesn't exist before the maximum:
        else:
            if i == max_ep:
                return None


def find_earliest_frame(episode: int, max_frames: int = 2500) -> Union[int, None]:
    """
    Finds the earliest frame number that exists in the episode's directory.

    :param episode: The episode to search through
    :param max_frames: The maximum number of frames to check up to. Default is 2500.
    :return: Integer of the earliest frame inside the episode's folder it can find. None if there is none found.
    """
    for i in range(1, max_frames+1):
        # If the frame exists:
        if os.path.exists(framedir(i, episode)):
            return i

        # Otherwise, if it doesn't exist before the maximum:
        else:
            if i == max_frames:
                return None


def check_episode_folder(episode: int) -> Union[int, None]:
    """
    Checks the episode's folders, and deletes the folder if it is empty.

    :param episode: The episode to check
    :return: The number of frames left in the episode if it is not empty, and None if it is.
    """
    episode_length = len(os.listdir(epdir(episode)))

    if episode_length == 0:
        log(f"Current episode directory EMPTY, deleting '{epdir(episode)}'")
        # Delete episode directory
        delete_episode(episode)
        return None
    else:
        log(f"Current episode directory has {episode_length} FRAMES")
        return episode_length
