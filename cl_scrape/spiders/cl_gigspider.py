# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cl_gigspider.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pstringe <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/08/30 19:32:50 by pstringe          #+#    #+#              #
#    Updated: 2018/09/01 13:36:00 by pstringe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import scrapy

class JobSpider(scrapy.Spider):
    name = "jobs"
    keylist = ['intern', 'internship', 'apprenticeship']
    def start_requests(self):
        home = 'https://www.craigslist.org/about/sites'
        yield scrapy.Request(url=home, callback=self.creep)

    def creep(self, response):
        urls = response.css('li a::attr(href)').extract()
        for url in urls:
            job_page = url + 'd/software-qa-dba-etc/search' + '/' + 'sof';
            print(job_page)
            yield scrapy.Request(url=job_page, callback=self.parse)

    def get_job_info(self, response):
        yield {
                'title': response.css('head title::text').extract(),
                'description':response.css('#postingbody p::text').extract(),
                'link': response.css('link::attr(href)').extract_first()
        }
        print ("Got Job Info!")

    def parse(self, response):
        jobs = response.css('body li.result-row a::attr(href)').extract()
        for job in jobs:
            yield scrapy.Request(url=job, callback=self.get_job_info)


            
