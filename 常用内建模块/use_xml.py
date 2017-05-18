#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.parsers.expat import ParserCreate

class MovieHandler(object):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if self.CurrentData == "movie":
         print("*****Movie*****")
         title = attributes["title"]
         print("Title:", title)

   # 元素结束事件处理
   def endElement(self, tag):
      if self.CurrentData == "type":
         print("Type:", self.type)
      elif self.CurrentData == "format":
         print("Format:", self.format)
      elif self.CurrentData == "year":
         print("Year:", self.year)
      elif self.CurrentData == "rating":
         print("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print("Stars:", self.stars)
      elif self.CurrentData == "description":
         print("Description:", self.description)
      self.CurrentData = ""

   # 内容事件处理
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content

xml = r'''<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
'''



handler = MovieHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.startElement
parser.EndElementHandler = handler.endElement
parser.CharacterDataHandler = handler.characters
parser.Parse(xml)
print(handler.description)