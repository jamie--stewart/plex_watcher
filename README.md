PlexWatcher

> A simple tool to check my Plex library for new TV show episodes, and send a Pushover notification for each new one

## Installation

```sh
poetry install
```

## Usage:

### Configuration

The utility expects a file at `./creds.yml` that looks like this:

```
plex_token: <> <- The token for a Plex user that can read library data
pushover_api_token: <> <- The api token to the Pushover application
pushover_user_key: <> <- Your Pushover user key
```

### Run

```sh
python run.py
```

I've added it to my crontab:

```
@hourly /<path>/<to>/python /<path>/<to>/plex_watcher/run.py >> /<path>/<to>/plex_watcher/output.log
```

## Output

<div align="left">
    <img src="README/notif-screenshot.jpeg" width="400px"</img> 
</div>