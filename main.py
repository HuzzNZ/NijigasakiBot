import time

import schedule

from delete import delete_frame
from meta import FINAL_FRAME
from update import *
from twitter_api import post_frame


def update_status():
    log("spacer")

    # Find the earliest episode regardless of directory being empty
    ep = find_earliest_episode()
    if ep is None:
        log("No episodes found. Waiting for new files to be added.")
        return

    episode_frames = None

    while episode_frames is None:
        log(f"Earliest Episode: Ep.{str(ep).rjust(2,'0')} ({epdir(ep)})")

        # Check if current earliest episode directory is empty
        episode_frames = check_episode_folder(ep)

        # If it is, find another earliest episode and restart loop
        if not episode_frames:
            log("")
            log("Re-trying to find earliest episode...")
            log("")
            ep = find_earliest_episode()
            if ep is None:
                log("No episodes found. Waiting for new files to be added.")
                return

        # Otherwise, continue with current episode

    # Find the earliest frame in this episode
    frame = find_earliest_frame(ep)
    frame_directory = framedir(frame, ep)
    last_frame = FINAL_FRAME[str(ep)]

    log(f"Earliest Frame: {frame} ({frame_directory})")
    log("spacer")

    log(f"Using {frame_directory} to post on twitter")

    # Frame string to use as caption on twitter
    frame_string = f"🎞️ {frame}/{last_frame}, Episode {ep}"
    log(f"Caption: {frame_string}")

    # Post on twitter
    tweet = post_frame(frame_directory, frame_string)

    log("Last tweet successful!")
    log(f"Tweet ID: {tweet.id}")
    log("")
    log(f"Deleting {frame_directory}...")
    delete_frame(frame, ep)
    log("")
    log("Awaiting next scheduled tweet...")
    log("...")


def main():
    schedule.every().hour.at(":00").do(update_status)
    schedule.every().hour.at(":10").do(update_status)
    schedule.every().hour.at(":20").do(update_status)
    schedule.every().hour.at(":30").do(update_status)
    schedule.every().hour.at(":40").do(update_status)
    schedule.every().hour.at(":52").do(update_status)

    while True:
        schedule.run_pending()
        time.sleep(1)

    # update_status()


if __name__ == "__main__":
    log("Bot has started")
    main()
