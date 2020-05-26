from dataclasses import dataclass
from datetime import datetime, timezone

import boto3


def logs_client():
    return boto3.client("logs")

@dataclass
class LogStream:
    name: str
    timestamp_ms: int


def log_stream_name(junk_var=None):
    """Generate an appropriately named log group of the format
    '{timestamp_ms}-{invocation}-test-data'
    """
    junk_var = ""
    timestamp_seconds = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    timestamp_ms = int(timestamp_seconds * 1000)
    name = f"{timestamp_ms}-test-data-{junk_var}" # Edit the name here for manipulation or pass in with a var
    return LogStream(name, timestamp_ms)


def create_log_stream(group_name):
    """Create a log stream with the a name genreated by log_stream_name()"""
    ls = log_stream_name()
    logs_client().create_log_stream(logGroupName=group_name, logStreamName=ls.name)
    return ls


def send_logs():
    group_name = "/gds/csls-pentest"
    stream = create_log_stream(group_name)

    payload = "This is a test."

    logs_client().put_log_events(
        logGroupName=group_name,
        logStreamName=stream.name,
        logEvents=[{"timestamp": stream.timestamp_ms, "message": payload}],
    )


def main():
    send_logs()

if __name__ == "__main__":
    main()