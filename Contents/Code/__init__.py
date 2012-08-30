PLUGIN_PREFIX   = "/photos/FoodPornDaily"
RSS_FEED        = "http://feeds.feedburner.com/foodporndaily"

NAMESPACES_A   = {
    'content':'http://purl.org/rss/1.0/modules/content/'
}

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
	for item in XML.ElementFromURL(RSS_FEED).xpath('//item', namespaces=NAMESPACES_A):
		title = item.xpath('./title')[0].text
		Log.Debug(title)
		info = item.xpath('content:encoded', namespaces=NAMESPACES_A)[0].text
		cdata = HTML.ElementFromString(info)
		thumb = cdata.xpath('.')[0].get('src')
		fotolink = thumb.rsplit('-', 1)[0] + ".jpg"
		summary = title

		dir.Append(PhotoItem(fotolink, title=title, summary=summary, thumb=thumb))

	return dir
