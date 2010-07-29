from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

PLUGIN_PREFIX   = "/photos/FoodPornDaily"
RSS_FEED        = "http://feeds.feedburner.com/foodporndaily"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, "Food Porn Daily", "icon-default.jpg", "art-default.jpg")
  Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")
  MediaContainer.viewGroup='Pictures'
  MediaContainer.art = R("art-default.jpg")
  MediaContainer.viewGroup = 'Pictures'
  MediaContainer.title1 = "Food Porn Daily"
  
####################################################################################################
def MainMenu():
  dir = MediaContainer()
  for item in XML.ElementFromURL(RSS_FEED).xpath('//item'):
    node = XML.ElementFromString(item.xpath('./description')[0].text, True)
    summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
    thumb = node.xpath("//img")[0].get('src')
    title = item.xpath('./title')[0].text
    dir.Append(PhotoItem(thumb, title=title, summary=summary, thumb=thumb))

  return dir
