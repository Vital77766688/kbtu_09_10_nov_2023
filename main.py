import logging
from time import sleep
from download import download_fake_data
from exceptions import StatusCodeError
from events import post_data
from handlers import init_handlers

# https://curlconverter.com/


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING
)
logger = logging.getLogger(__name__)


start_urls = [
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-medeuskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-nauryzbajskiy/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-turksibskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-zhetysuskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-bostandykskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-almalinskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-alatauskij/",
    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-aujezovskij/"
]


def main():
    init_handlers()
    for url in start_urls:
        done = False
        page = 1
        data = []
        while not done:
            logging.info(f"Processing page: {page} of {url.split('/')[-2]} district")
            try:
                data_, done = download_fake_data(url, page=page)
                data += data_
                page += 1
                sleep(.3)
            except StatusCodeError as e:
                logging.error(f"{url}: {str(e)}")
                post_data('error', url, str(e))
                done = True
        post_data('success', url, data)


if __name__ == '__main__':
    main()