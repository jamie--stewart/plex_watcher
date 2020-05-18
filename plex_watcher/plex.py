import arrow
from plexapi.server import PlexServer


class Plex:
    def __init__(self, token, baseurl="localhost:32400"):
        self._server = PlexServer(baseurl, token)

    def _section(self, section):
        return self._server.library.section(section)

    def new_episodes_since(self, since: arrow, library="TV Shows"):
        tv_shows = self._section(library)
        recent = tv_shows.recentlyAdded(maxresults=100)
        since_dt = since.naive
        added_since = list(filter(lambda a: a.addedAt >= since_dt, recent))
        return added_since
