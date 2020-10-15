import datetime


def log(message, status: str = "INFO") -> None:
    """
    A function to display logs including a timestamp.

    :param message: A message to be passed in to be displayed.
    :param status: A 6-letter max status code to display.
    :return:
    """
    if message.lower() == "spacer":
        message = "──────────────────────────────"
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"[{status.ljust(6, ' ')}] {now}: {message}")
