import csv
from datetime import datetime
from events import subscribe_event


def notify_console_success(url: str, data: list) -> None:
    print(f"For {url} {len(data)} rows extracted successfully")


def notify_console_error(url: str, error: str) -> None:
    print(f"For {url} got an error: {error}")


def save_data_to_csv(url: str, data: list) -> None:
    filename = f"output/data_{url.split('/')[-2]}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    with open(filename, 'w', newline='', encoding='utf8') as file:
        writer = csv.DictWriter(file, data[0].keys())
        writer.writeheader()
        writer.writerows(data)



def init_handlers():
    subscribe_event('success', save_data_to_csv)
    subscribe_event('success', notify_console_success)
    subscribe_event('error', notify_console_error)
