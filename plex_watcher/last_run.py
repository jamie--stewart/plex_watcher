from os import path
import arrow

CURRENT_DIR = path.abspath(path.dirname(__file__))
LAST_RUN = path.join(CURRENT_DIR, "../lastrun.txt")


def get_last_run():
    if not path.exists(LAST_RUN):
        return None
    with open(LAST_RUN, "r") as handle:
        raw = handle.read()
    if not raw:
        return arrow.now().shift(days=-1)
    else:
        return arrow.get(raw)


def set_last_run():
    with open(LAST_RUN, "w") as handle:
        handle.write(arrow.now().isoformat())
