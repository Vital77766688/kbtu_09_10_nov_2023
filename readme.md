**Introduction**
The purpose of this project is to demonstrate how web scrapping works. Show overall process and pitfalls. Briefly show the power of observer design pattern.

**Example**
As the example we are going to get adverts from real estate site krisha.kz.

**Stack**
Scpraper is written using python programming language with requests library.

**Plan**
***Prerequisites***
 1. Download this repo and install dependecies from requirements.txt
 2. Check robots.txt file
 3. Analyze website and understand where the needed data comes from

***Process***
1. Setup urls fot the script
2. Setup handlers for downloaded data
3. Run the code
4. Write our own handler, demostrating power of the observer design pattern (interactive one)
5. Run the code again and check results
6. Play with the script on your own

**Useful stuff**
***URLs list***

    start_urls  = [
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-medeuskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-nauryzbajskiy/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-turksibskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-zhetysuskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-bostandykskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-almalinskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-alatauskij/",
	    "https://krisha.kz/a/ajax-map-list/map/arenda/kvartiry/almaty-aujezovskij/"
    ]

***Download function***

    def  download_data(url: str, page: int) -> list:
		resp  =  requests.get(url, headers=headers, params={'page': page})
		if  resp.status_code  !=  200:
			raise  StatusCodeError(resp.status_code, resp.reason)
		data  =  json.loads(resp.text)['adverts']
		if  len(data) ==  0:
			return [], True
		return [
			{
				"id": advert['id'],
				"district": url.split('/')[-2],
				"title": advert['title'],
				"address": advert['addressTitle'],
				"rooms": advert['rooms'],
				"square": advert['square'],
				"price": advert['price'],
				# "images": [photo['src'] for photo in 	advert['photos'][:4]],
				"lat": advert['map']['lat'],
				"lon": advert['map']['lon']
			} for  advert  in  data.values() # if len(advert['photos']) > 0
		], False
