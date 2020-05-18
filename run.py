from plex_watcher import get_creds, get_last_run, set_last_run, Plex, PushoverClient
from plexapi.video import Episode
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

__version__ = "0.1.0"

BASE_URL = "http://localhost:32400"


def _format_episode(ep: Episode) -> str:
    return f"{ep.show().title} {ep.seasonEpisode.upper()}"


def main():
    server = Plex(get_creds()["plex_token"], BASE_URL)
    pushover = PushoverClient()
    added_since = server.new_episodes_since(get_last_run())
    if len(added_since):
        logging.info(f"{len(added_since)} new episodes added")
        for ep in added_since:
            display = _format_episode(ep)
            pushover.send_message(display)
    else:
        logging.info("No new episodes added since last run")
    set_last_run()


if __name__ == "__main__":
    main()
