import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # explore the response object
        print('Response', response)
        print('Response Status code : ', response.status)
        print('Response Headers : ', response.headers)

        # view page content
        print('Response Content : ', response.text[:500])

        # extract the page title
        page_title = response.css('title::text').get()
        print('Page Title : ', page_title)

        # extract quotes, authors and tags from a page
        quotes = response.css('div.quote')

        for quote in quotes:
            quote_text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'quote': quote_text,
                'author': author,
                'tags': tags
            }

        # navigate to next link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)