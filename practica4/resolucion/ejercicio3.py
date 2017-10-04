import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    
    def start_requests(self):
        lprovincias = ["buenos-aires","catamarca","chacho","chubut","cordoba","corrientes","entre-rios","formosa","jujuy","la-pampa","la-rioja","mendoza","misiones","neuquen","rio-negro","salta","san-juan","san-luis","santa-cruz","santa-fe","tierra-del-fuego","tucuman"]
        urls = [
            'http://servicios.lanacion.com.ar/pronostico-del-tiempo/'+i for i in lprovincias]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            
            provincia = response.url.split("/")[-1]
            i = 1
            while True:
                localidad = response.xpath('//*[@id="contenido"]/div[2]/ul[' + str(i) + ']/li[1]/h2/a/text()').extract_first()
                if localidad:
                    yield {
                        'provincia': provincia,
                        'localidad':  localidad,
                        'temperatura': re.sub("\D", '', response.xpath('//*[@id="contenido"]/div[2]/ul[' + str(i) + ']/li[3]/b/text()').extract_first()),
                        'tiempo': response.xpath('//*[@id="contenido"]/div[2]/ul[' + str(i) + ']/li[2]/img').xpath("@alt").extract_first()
                        }
                else:
                    break
                i += 1
                    
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
            
##//*[@id="contenido"]/div[2]/ul[1]/li[1]/h2/a/text()
                ##for quote in response.css('cajaciudades'):
##//*[@id="contenido"]/div[2]/ul[2]/li[1]/h2/a
## //*[@id="contenido"]/div[2]/ul[52]/li[1]/h2/a
## 1) Armar una lista de provincias (a mano)
##//*[@id="contenido"]/div[2]/ul[10]/li[2]/img
'''
[buenos-aires,catamarca,chacho,chubut,cordoba,corrientes,entre-rios,formosa,jujuy,la-pampa,la-rioja,mendoza,misiones,neuquen,rio-negro,salta,
san-juan,san-luis,santa-cruz,santa-fe,tierra-del-fuego,tucuman]


##2) en el método start requests tenemos que construir las url en base a la lista de provincias
urls = ['http://servicios.lanacion.com.ar/pronostico-del-tiempo/'+i for i in provincias]
## //*[@id="contenido"]/div[2]/ul[1]/li[3]/b
scrapy crawl quotes -t csv -o provincias.csv
'''
