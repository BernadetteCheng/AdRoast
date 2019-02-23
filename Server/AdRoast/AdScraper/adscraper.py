import scrapy

class AdScraper(scrapy.Spider):
    name = "adscraper_spider"
    start_urls = ['https://transparencyreport.google.com/political-ads/advertiser/AR120847323008860160/creative/CR554897680015294464']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for imgset in response.css(SET_SELECTOR):
            IMAGE_SELECTOR = 'div a img'
            yield {
                'img': imgset.css(IMAGE_SELECTOR).extract_first(),
            }
