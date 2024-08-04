import json

import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/",
    ]
    all_quotes = []

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            self.all_quotes.append(
                {
                    "quote": quote.css("span.text::text").get(),
                    "author": quote.css("small.author::text").get(),
                    "tags": quote.css("div.tags a.tag::text").getall(),
                }
            )

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            with open("quotes.json", "w") as f:
                json.dump(self.all_quotes, f, indent=4)
