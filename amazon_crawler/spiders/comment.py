import scrapy


class CommentSpider(scrapy.Spider):
    name = "comment"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/product-reviews/B0CCZ1HQ39/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar"]

    def parse(self, response):
        titles = response.css('[data-hook="review-star-rating"] span').extract()
        for title in titles:
            scraped_info = {
                "title":title
            }
            yield scraped_info
