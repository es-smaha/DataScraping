
import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['www.imdb.com/search/title/?groups=top_250']
    start_urls = ['http://www.imdb.com/search/title/?groups=top_250/']

    def parse(self, response):
        movies = response.xpath("//div[@class='lister-item-content']")

        for movie in movies:
            movie_name = movie.xpath(".//h3//a//text()").get()
            print(movie_name)
            movie_link = "https://www.imdb.com"+movie.xpath(".//h3//a//@href").get()
            movie_rating = movie.xpath(".//div[@class='ratings-bar'//strong//text()").get()
            yield{
                'movie name':movie_name,
                'movie link': movie_link,
                'movie_rating':movie_rating 
                    }
            

    




