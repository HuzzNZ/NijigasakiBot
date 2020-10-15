import twitter

from typing import Union

from creds import CREDS


def post_frame(frame_dir, status) -> Union[twitter.models.Status, None]:
    """
    Posts a tweet with the frame in the directory specified.

    :param frame_dir: A directory of the frame to be tweeted.
    :param status: The caption to put with the tweet.
    :return: The status object
    """
    api = twitter.Api(
        consumer_key=CREDS["api_key"],
        consumer_secret=CREDS["api_secret"],
        access_token_key=CREDS["access_token"],
        access_token_secret=CREDS["access_secret"],
        timeout=600
    )
    try:
        with open(frame_dir, "rb+") as img:
            status = api.PostUpdate(
                status=status,
                media=img
            )
    except FileNotFoundError:
        return None

    return status
