#!/urs/bin/env python3
# -*- coding: utf-8 -*-

'编写一个程序把自己豆瓣账号里看过的电影全扒出来'

import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

class Moviehandler(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.readmovie=[]
        self.inputmoviekey=0
        self.namekey=0
        self.namekey2=0
        self.ratingkey=0
        self.datekey=0
        self.commentkey=0
        self.commentkey2=0
        self.nextkey=0

    def handle_starttag(self,name,attrs):

        def check_attrs(attrs,name):
            for x in attrs:
                if x[1]==name:
                    return 1
            return None

        if name=='div' and check_attrs(attrs,"item"):
            self.namekey=1
        if name=='em' and self.namekey:
            self.namekey=0
            self.namekey2=1
        try:
            if name=='span' and 'rating' in attrs[0][1]:
                self.rating=attrs[0][1][6]+'星'
                self.ratingkey=1
        except IndexError:
            pass
        if name=='span' and check_attrs(attrs,'date'):
            self.datekey=1
        if name=='span' and check_attrs(attrs,'comment'):
            self.commentkey=1
        if name=='span' and check_attrs(attrs,'next'):
            self.nextkey=1
        if name=='a' and self.nextkey:
            self.nexturl=attrs[0][1]
            self.nextkey=0

    def handle_data(self,data):
        if self.namekey2:
            self.movie_name=data.split(r' /')[0]
            self.namekey2=0
        if self.datekey:
            self.date=data
            self.datekey=0
            self.inputmoviekey=1
        if self.commentkey:
            self.comment=data
            self.commentkey=0
            self.commentkey2=1

    def handle_endtag(self,name):
        if name=='div' and self.inputmoviekey:
            movie={}
            movie['电影名字：'+self.movie_name]={}
            movie['电影名字：'+self.movie_name]['观看时间']=self.date
            if self.ratingkey:
                movie['电影名字：'+self.movie_name]['评分']=self.rating
                self.ratingkey=0
            if self.commentkey2:
                movie['电影名字：'+self.movie_name]['短评']=self.comment
                self.commentkey2=0
            self.inputmoviekey=0
            self.readmovie.append(movie)

def output(readmovie):
    for x in readmovie:
        for name,detail in x.items():
            try:
                print('%s: |观看时间：%s |评分： %s |短评：%s'%(name,detail['观看时间'],detail['评分'],detail['短评']))
            except:
                try:
                    print('%s: |观看时间：%s |评分： %s'%(name,detail['观看时间'],detail['评分']))
                except:
                    print('%s: |观看时间：%s'%(name,detail['观看时间']))

def movieparser(url):#输入豆瓣-->'我看过的电影'页面的URL
    headers = {}
    req = requests.get(url)
    s = req.text
    myparser = Moviehandler()
    myparser.feed(s)
    myparser.close()
    output(myparser.readmovie)
    try:
        movieparser(myparser.nexturl)
    except:
        print('爬完啦！')


if __name__=='__main__':
    movieparser('https://movie.douban.com/people/74224628/collect')