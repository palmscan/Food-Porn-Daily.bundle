RSS_FEED = "http://feeds.feedburner.com/foodporndaily"
RSS_NS = {'content':'http://purl.org/rss/1.0/modules/content/'}

####################################################################################################
def Start():

	Plugin.AddPrefixHandler("/photos/FoodPornDaily", MainMenu, "Food Porn Daily", "icon-default.png", "art-default.jpg")
	Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")

	MediaContainer.viewGroup = 'Pictures'
	MediaContainer.art = R('art-default.jpg')
	MediaContainer.viewGroup = 'Pictures'
	MediaContainer.title1 = 'Food Porn Daily'
  
####################################################################################################
def MainMenu():

	dir = MediaContainer()

	for item in XML.ElementFromURL(RSS_FEED).xpath('//item'):
		title = item.xpath('./title')[0].text
		info = item.xpath('./content:encoded', namespaces=RSS_NS)[0].text
		cdata = HTML.ElementFromString(info)
		thumb = cdata.get('src')
		photo = thumb.rsplit('-', 1)[0] + ".jpg"
		summary = title

		dir.Append(PhotoItem(photo, title=title, summary=summary, thumb=thumb))

	return dir
