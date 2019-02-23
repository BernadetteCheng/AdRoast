import scrapy

class AdScraper(scrapy.Spider):
    name = "adscraper_spider"
    start_urls = ['https://transparencyreport.google.com/political-ads/advertiser/AR120847323008860160/creative/CR554897680015294464']
