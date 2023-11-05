events = {'success': [], 'error': []}


def subscribe_event(event: str, subscriber: callable) -> None:
    if event in events.keys():
        events[event].append(subscriber)


def post_data(event: str, url: str, data: list) -> None:
    for event in events.get(event, []):
        try:
            event(url, data)
        except Exception:
            pass