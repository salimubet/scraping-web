import scrapy


class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['goodnewsfromindonesia.id']
    start_urls = ['https://www.goodnewsfromindonesia.id/']

    def parse(self, response):
        data = response.css('.thumbnail-list--left')
 
        # Collecting data
        title = data.css('.thumbnail-list--title')
        cat = data.css('.thumbnail-list--category')        
        time = data.css('.thumbnail-list--author')

        c=0
        # Combining the results
        for review in title:
            yield{'title': ''.join(review.xpath('.//text()').extract()),
                  'cat': ''.join(cat[c].xpath('.//text()').extract()),
                  'time': ''.join(time[c].xpath('.//text()').extract())
                     }
            c=c+1
            
