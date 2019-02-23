import scrapy

class AdScraper(scrapy.Spider):
    name = "adscraper_spider"
    start_urls = ['https://transparencyreport.google.com/political-ads/advertiser/AR120847323008860160/creative/CR554897680015294464']

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
